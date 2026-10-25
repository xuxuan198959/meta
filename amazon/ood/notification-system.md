# Notification System

**Prompt.** Design a multi-channel notification system (email, SMS, push, ...). Urgent notifications go out on every channel the user has; otherwise follow the user's channel preferences. (★ 📣 2 reports: [8536211](https://leetcode.com/discuss/post/8536211/), [8423184](https://leetcode.com/discuss/post/8423184/))

## Clarifying questions

- **Which channels?** Email, SMS, push to start. Adding Slack or webhook must not change the core.
- **"All channels" for urgent?** Every channel with a verified address, ignoring preferences and quiet hours. Users can't mute a security alert.
- **Non-urgent?** Try the user's ordered preferences until one succeeds; no preferences means email. Quiet hours suppress it.
- **Channel failure?** Recorded per channel as data; the others still go out.
- **Sync or async?** Synchronous here; a queue with retries is an extension.
- **More rules later?** Likely (opt-outs, rate limits), so routing is an ordered list of rules, not an `if` chain.

## Core classes

| Class | Responsibility | Pattern |
|---|---|---|
| `Notification`, `User`, `Result` | Message + priority; addresses, preferences, quiet hours; per-channel outcome | Value objects |
| `Sender` (one per channel) | Deliver on one channel, raise `DeliveryError` on failure | Strategy |
| `RULES`: `urgent_all`, `quiet_hours`, `preferences` | Return a `Plan` or `None` to defer | Chain of Responsibility |
| `NotificationService` | Look up user, resolve plan, deliver, collect results | Facade |

## Code

```python
from __future__ import annotations

import itertools
from dataclasses import dataclass, field
from datetime import datetime, time
from enum import Enum

Channel = Enum("Channel", "EMAIL SMS PUSH")      # definition order = urgent fan-out order
Priority = Enum("Priority", "LOW NORMAL URGENT")


class DeliveryError(Exception): ...


@dataclass(frozen=True)
class Notification:
    user_id: str
    title: str
    priority: Priority = Priority.NORMAL


@dataclass
class User:
    user_id: str
    addresses: dict                               # Channel -> verified address
    preferences: list = field(default_factory=list)
    quiet_hours: tuple[time, time] | None = None

    def reachable(self, channels):
        return [c for c in channels if c in self.addresses]


@dataclass(frozen=True)
class Plan:
    channels: list
    first_success: bool = False                   # False = send on all channels
    reason: str = ""                              # why nothing is sent, if empty


@dataclass(frozen=True)
class Result:
    notification_id: str
    channel: str | None
    status: str                                   # sent | failed | suppressed
    detail: str = ""


class Sender:                                     # Strategy: one subclass per real provider
    def __init__(self, channel, fail=None):
        self.channel, self.fail = channel, fail

    def send(self, address: str, n: Notification) -> None:
        if self.fail:
            raise DeliveryError(self.fail)


def urgent_all(n, user, now):
    if n.priority is Priority.URGENT:
        return Plan(user.reachable(list(Channel)))

def quiet_hours(n, user, now):
    if user.quiet_hours:
        start, end, t = *user.quiet_hours, now.time()
        if (start <= t < end) if start <= end else (t >= start or t < end):  # wraps midnight
            return Plan([], reason="quiet hours")

def preferences(n, user, now):
    return Plan(user.reachable(user.preferences) or user.reachable([Channel.EMAIL]),
                first_success=True)

RULES = [urgent_all, quiet_hours, preferences]    # list order = precedence


class NotificationService:
    def __init__(self, users, senders, clock, rules=RULES):
        self.users, self.clock, self.rules = users, clock, rules
        self.senders = {s.channel: s for s in senders}
        self.ids = itertools.count(1)

    def send(self, n: Notification) -> list[Result]:
        nid = f"n-{next(self.ids)}"               # trace / idempotency key
        user = self.users.get(n.user_id)
        if user is None:
            return [Result(nid, None, "failed", "unknown user")]
        now = self.clock()
        plan = next((p for p in (r(n, user, now) for r in self.rules) if p), None)
        if plan is None or not plan.channels:
            reason = plan.reason if plan and plan.reason else "no reachable channel"
            return [Result(nid, None, "suppressed", reason)]
        results = []
        for ch in plan.channels:
            results.append(self._deliver_one(nid, ch, user.addresses[ch], n))
            if plan.first_success and results[-1].status == "sent":
                break
        return results

    def _deliver_one(self, nid, ch, address, n) -> Result:
        sender = self.senders.get(ch)
        if sender is None:
            return Result(nid, ch.name, "failed", "no sender configured")
        try:
            sender.send(address, n)
            return Result(nid, ch.name, "sent")
        except DeliveryError as e:
            return Result(nid, ch.name, "failed", str(e))


if __name__ == "__main__":
    aaron = User("u1", {Channel.EMAIL: "a@x.com", Channel.SMS: "+1555", Channel.PUSH: "tok"},
                 preferences=[Channel.PUSH, Channel.SMS], quiet_hours=(time(22), time(7)))
    now = [datetime(2026, 1, 1, 23, 30)]
    svc = NotificationService({"u1": aaron}, clock=lambda: now[0], senders=[
        Sender(Channel.EMAIL), Sender(Channel.SMS), Sender(Channel.PUSH, fail="token expired")])
    show = lambda rs: [(r.channel, r.status, r.detail) for r in rs]
    print(show(svc.send(Notification("u1", "Password changed", Priority.URGENT))))
    # [('EMAIL', 'sent', ''), ('SMS', 'sent', ''), ('PUSH', 'failed', 'token expired')]
    print(show(svc.send(Notification("u1", "Weekly digest", Priority.LOW))))
    # [(None, 'suppressed', 'quiet hours')]
    now[0] = datetime(2026, 1, 2, 12, 0)
    print(show(svc.send(Notification("u1", "Order shipped"))))
    # [('PUSH', 'failed', 'token expired'), ('SMS', 'sent', '')]  email never tried
```

## Design choices

- **Strategy for channels.** Each channel is a `Sender`; adding Slack is one class plus registration, and the service never branches on channel type (Open/Closed).
- **Routing as an ordered rule list.** "Urgent beats quiet hours beats preferences" is precedence, so it lives in list order; a new rule (marketing opt-out) is a function inserted at the right spot.
- **Failures are data.** One bad channel must not abort the others; returning `Result`s makes partial success visible to callers and metrics. The clock is injected so quiet hours test deterministically.

## Edge cases

- Unknown user returns a `failed` result, not an exception.
- No reachable preferred channel falls back to email; if that's missing too, `suppressed` "no reachable channel".
- Quiet hours wrapping midnight (22:00 to 07:00) are handled; `start == end` means no quiet window.
- Channel in the plan with no registered sender: `failed` "no sender configured", not a `KeyError`.

## Extensions

- **Async + retries.** Enqueue `(notification_id, channel, address, payload)` on per-channel queues; workers retry with exponential backoff, then dead-letter. `notification_id + channel` is the idempotency key, so retries don't double-send.
- **Rate limiting / digests.** A `rate_limit` rule before `preferences` that suppresses low priority past N per window (sliding-window counter per user).
- **Templates.** A renderer per channel (160-char SMS, HTML email) next to the sender.
- **Thread safety.** The only shared mutable state is the ID counter; use UUIDs or a lock and `send` is safe to call concurrently.
