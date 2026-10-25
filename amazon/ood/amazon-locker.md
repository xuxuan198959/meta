# Amazon Locker

**Prompt.** Design an Amazon Locker system: assign a package to the smallest compartment that fits, give the customer a pickup code, and expire uncollected packages. (★ 📣 5 reports: [7754949](https://leetcode.com/discuss/post/7754949/), [7228788](https://leetcode.com/discuss/post/7228788/), [6623435](https://leetcode.com/discuss/post/6623435/), [6585102](https://leetcode.com/discuss/post/6585102/), [8499681](https://leetcode.com/discuss/post/8499681/))

## Clarifying questions

- **One station or many?** One `LockerStation`. Choosing a station across a city is a separate service.
- **How is size defined?** Discrete S < M < L < XL. A package fits any compartment of its size or larger.
- **No compartment fits?** Raise an error; the caller redirects to another station.
- **Pickup code?** 6 digits, unique among active codes at the station, single use.
- **Expiry?** 3 days, configurable. Expired packages are flagged for return; the compartment is freed when the courier pulls them.
- **Concurrency?** Couriers and customers act at once, so assign/pickup are atomic (one lock).

## Core classes

| Class | Responsibility | Pattern |
|---|---|---|
| `Compartment` | Physical slot: size + `AVAILABLE / OCCUPIED / OUT_OF_SERVICE` | Entity |
| `Assignment` | Package-to-compartment binding with deadline, `AWAITING / EXPIRED` | Entity / lifecycle |
| `smallest_fit` (allocator) | Choose a compartment for a size | Strategy |
| `LockerStation` | assign, pickup, expire, release; owns the lock | Facade |

## Code

```python
from __future__ import annotations

import random
import threading
from dataclasses import dataclass
from datetime import datetime, timedelta
from enum import Enum, IntEnum


class Size(IntEnum):
    S = 1; M = 2; L = 3; XL = 4

Slot = Enum("Slot", "AVAILABLE OCCUPIED OUT_OF_SERVICE")
Status = Enum("Status", "AWAITING EXPIRED")   # picked-up assignments are deleted


class LockerError(Exception): ...


@dataclass
class Compartment:
    compartment_id: str
    size: Size
    state: Slot = Slot.AVAILABLE


@dataclass
class Assignment:
    package_id: str
    compartment: Compartment
    expires_at: datetime
    status: Status = Status.AWAITING

    def overdue(self, now: datetime) -> bool:
        return self.status is Status.AWAITING and now >= self.expires_at


def smallest_fit(compartments: list[Compartment], size: Size) -> Compartment | None:
    fits = [c for c in compartments if c.state is Slot.AVAILABLE and c.size >= size]
    return min(fits, key=lambda c: c.size, default=None)


class LockerStation:
    def __init__(self, compartments, clock, allocator=smallest_fit,
                 hold=timedelta(days=3), rng=None):
        self.compartments, self.clock, self.hold = compartments, clock, hold
        self.allocator = allocator          # Strategy: swap for "keep one XL free", etc.
        self.rng = rng or random.SystemRandom()   # unpredictable codes in prod
        self.active: dict[str, Assignment] = {}   # code -> assignment (awaiting or expired)
        self.lock = threading.Lock()

    def assign(self, package_id: str, size: Size) -> str:
        with self.lock:
            comp = self.allocator(self.compartments, size)
            if comp is None:
                raise LockerError(f"no free compartment fits {size.name}")
            code = self._unique_code()
            comp.state = Slot.OCCUPIED
            self.active[code] = Assignment(package_id, comp, self.clock() + self.hold)
            return code

    def pickup(self, code: str) -> str:
        with self.lock:
            a = self.active.get(code)
            if a is None:
                raise LockerError("unknown or used code")
            if a.overdue(self.clock()):
                a.status = Status.EXPIRED       # don't trust the sweep to have run
            if a.status is Status.EXPIRED:
                raise LockerError("code expired")
            a.compartment.state = Slot.AVAILABLE
            del self.active[code]
            return a.package_id

    def expire_overdue(self) -> list[Assignment]:
        with self.lock:
            overdue = [a for a in self.active.values() if a.overdue(self.clock())]
            for a in overdue:
                a.status = Status.EXPIRED       # compartment stays occupied until pulled
            return overdue

    def release_expired(self, compartment_id: str) -> None:
        with self.lock:
            for code, a in self.active.items():
                if a.compartment.compartment_id == compartment_id and a.status is Status.EXPIRED:
                    a.compartment.state = Slot.AVAILABLE
                    del self.active[code]
                    return
            raise LockerError(f"no expired package in {compartment_id}")

    def _unique_code(self) -> str:
        for _ in range(20):                     # bounded retry on collision
            code = f"{self.rng.randrange(10**6):06d}"
            if code not in self.active:
                return code
        raise LockerError("could not generate a unique code")


if __name__ == "__main__":
    now = [datetime(2026, 1, 1, 9)]
    station = LockerStation([Compartment("S1", Size.S), Compartment("M1", Size.M),
                             Compartment("L1", Size.L)], clock=lambda: now[0],
                            rng=random.Random(42))
    a = station.assign("pkg-a", Size.S)                 # -> S1
    station.assign("pkg-b", Size.S)                     # S1 taken -> M1
    print(station.pickup(a))                            # pkg-a
    now[0] += timedelta(days=4)
    print([x.package_id for x in station.expire_overdue()])  # ['pkg-b']
    station.release_expired("M1")                       # courier pulled it; M1 free
    try:
        station.assign("pkg-c", Size.XL)
    except LockerError as e:
        print(e)                                        # no free compartment fits XL
```

## Design choices

- **Strategy for allocation.** "Smallest fit" is one injected function; "spread wear" or "reserve one XL" is a new function, `LockerStation` unchanged (Open/Closed).
- **Codes key the assignment, not the compartment.** `Compartment` holds physical state and `Assignment` holds the package lifecycle, so a reused compartment never leaks an old code.
- **Injected clock and RNG.** Expiry and codes are the only nondeterminism; injecting them tests "4 days later" without sleeping and makes codes reproducible.

## Edge cases

- Pickup exactly at the deadline counts as expired (`now >= expires_at`). Say the boundary out loud.
- Late pickup before `expire_overdue` ran: `pickup` checks the deadline itself, so a missed sweep can't let it through.
- Code collision: bounded retry, then fail loudly instead of looping forever.
- Reused code fails: it is deleted on pickup. `OUT_OF_SERVICE` compartments are never chosen.
- No fit: raise; never fall back to a smaller compartment.

## Extensions

- **Returns (drop-off) flow.** Generalise `Assignment` to `Reservation` with `RESERVED -> DEPOSITED -> COLLECTED`; drop-off code for the customer, courier code for collection. Allocator, clock and RNG reused.
- **Faster allocation.** One free list per size; walk sizes upward from the package size: O(#sizes) instead of O(#compartments).
- **Notifications.** Inject a sender called after `assign` and `expire_overdue`, outside the lock so a slow SMS provider doesn't block the station.
- **Many stations / shared DB.** Per-station locks; occupy with a conditional `UPDATE ... WHERE id=? AND state='AVAILABLE'` so two servers can't take one slot.
