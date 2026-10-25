# Pub/Sub

**Prompt.** Design an in-process pub/sub broker: subscribers register for event types, publishers publish events, and the broker must handle about 10k messages/s safely across threads. (★ 📣 2 reports: [8513742](https://leetcode.com/discuss/post/8513742/), [7600153](https://leetcode.com/discuss/post/7600153/))

## Clarifying questions

- **In-process or distributed?** In-process, one process. Kafka/SNS-style is an extension.
- **Does `publish` wait for handlers?** No. It enqueues and returns; worker threads deliver, so a slow subscriber never slows publishers.
- **Ordering?** FIFO per subscriber (per publishing thread). No global order across subscribers.
- **Delivery guarantee?** At-most-once, in memory. A handler that raises is logged and counted; the subscriber stays.
- **Slow subscriber?** Bounded queue per subscriber. When full, drop the newest and count it; blocking the publisher is an alternative policy.
- **Wildcards?** Exact type plus `"*"` for everything. Hierarchical topics are an extension.

## Core classes

| Class | Responsibility | Pattern |
|---|---|---|
| `Event` | Immutable type, payload, id | Value object |
| `Subscription` | One subscriber's handler, bounded queue, worker thread, counters | Observer + Active Object |
| `Broker` | Copy-on-write type → subscriptions map; subscribe, publish, shutdown | Facade / Registry |

## Code

```python
from __future__ import annotations

import itertools
import logging
import queue
import threading
from dataclasses import dataclass
from typing import Any, Callable

log = logging.getLogger("pubsub")
WILDCARD = "*"
_STOP = object()  # sentinel that tells a worker to exit


@dataclass(frozen=True)
class Event:
    event_type: str
    payload: Any
    event_id: int

class Subscription:
    """Own queue + worker: per-subscriber FIFO, and a slow handler only fills its own queue."""

    def __init__(self, event_type: str, handler: Callable[[Event], None], capacity: int):
        self.event_type, self.handler = event_type, handler
        self.queue: queue.Queue = queue.Queue(maxsize=capacity)
        self.delivered = self.failed = self.dropped = 0
        self.drop_lock = threading.Lock()  # many publishers bump `dropped`
        self.worker = threading.Thread(target=self._run, daemon=True)
        self.worker.start()

    def enqueue(self, event: Event) -> bool:
        try:
            self.queue.put_nowait(event)  # overflow policy: drop newest
            return True
        except queue.Full:
            with self.drop_lock:
                self.dropped += 1
            return False

    def stop(self, drain: bool) -> None:
        try:
            while not drain:               # unsubscribe: discard the backlog
                self.queue.get_nowait()
        except queue.Empty:
            pass
        self.queue.put(_STOP)              # blocking put: lands after any backlog
        if threading.current_thread() is not self.worker:  # handler may unsubscribe itself
            self.worker.join(5)

    def _run(self) -> None:
        while (event := self.queue.get()) is not _STOP:
            try:
                self.handler(event)
                self.delivered += 1        # only this thread writes delivered/failed
            except Exception:              # one bad event must not kill the worker
                log.exception("handler failed on event %s", event.event_id)
                self.failed += 1

class Broker:
    def __init__(self, capacity: int = 10_000):
        self.capacity = capacity
        self.by_type: dict[str, tuple[Subscription, ...]] = {}
        self.write_lock = threading.Lock()
        self.ids = itertools.count(1)
        self.closed = False

    def subscribe(self, event_type: str, handler: Callable[[Event], None]) -> Subscription:
        if self.closed:
            raise RuntimeError("broker is shut down")
        sub = Subscription(event_type, handler, self.capacity)
        with self.write_lock:              # copy-on-write: publishers never take this lock
            updated = dict(self.by_type)
            updated[event_type] = updated.get(event_type, ()) + (sub,)
            self.by_type = updated
        return sub

    def unsubscribe(self, sub: Subscription) -> None:
        with self.write_lock:
            current = self.by_type.get(sub.event_type, ())
            if sub not in current:
                return                     # already removed: no-op
            self.by_type = {**self.by_type, sub.event_type: tuple(s for s in current if s is not sub)}
        sub.stop(drain=False)

    def publish(self, event_type: str, payload: Any) -> int:
        if self.closed:
            raise RuntimeError("broker is shut down")
        snapshot = self.by_type            # one atomic read of an immutable snapshot
        subs = snapshot.get(event_type, ()) + (snapshot.get(WILDCARD, ()) if event_type != WILDCARD else ())
        event = Event(event_type, payload, next(self.ids))
        return sum(sub.enqueue(event) for sub in subs)  # how many accepted it

    def shutdown(self) -> None:
        self.closed = True
        for sub in {s for subs in self.by_type.values() for s in subs}:
            sub.stop(drain=True)

if __name__ == "__main__":
    logging.basicConfig(level=logging.CRITICAL)  # hide the faulty handler's tracebacks
    broker = Broker()
    received: list[int] = []
    orders = broker.subscribe("order.created", lambda e: received.append(e.payload))
    audit = broker.subscribe(WILDCARD, lambda e: None)
    faulty = broker.subscribe("order.created", lambda e: 1 / 0)
    pubs = [threading.Thread(target=lambda b=b: [broker.publish("order.created", b + i)
                                                 for i in range(2_500)]) for b in range(0, 10_000, 2_500)]
    for t in pubs: t.start()
    for t in pubs: t.join()
    print(broker.publish("user.signup", {}))  # 1 (only the wildcard audit)
    broker.shutdown()                         # drains every queue
    print(orders.delivered, audit.delivered, faulty.failed)  # 10000 10001 10000
    print(all(p == sorted(p) for p in ([x for x in received if x // 2_500 == k] for k in range(4))))  # True: FIFO per publisher
```

## Design choices

- **Observer with one queue and worker per subscriber (Active Object).** Per-subscriber ordering comes for free, publishers never run handler code, and a slow or broken subscriber only backs up its own queue.
- **Copy-on-write subscription map.** Publishing is the hot path (10k/s), subscribing is rare. Publishers read an immutable snapshot with no lock; writers copy and swap under a lock, like Java's `CopyOnWriteArrayList`.
- **Failure isolation.** The worker catches, logs, counts and keeps going. A worker thread dying silently is the classic pub/sub bug.

## Edge cases

- Queue full: `enqueue` returns `False` and bumps `dropped`; `publish` returns how many subscribers accepted the event.
- No subscribers: `publish` returns 0, not an error. Publishing to `"*"` doesn't deliver twice to wildcard subscribers.
- Unsubscribe clears the backlog and stops the worker; unsubscribing twice is a no-op, and a handler can unsubscribe itself without deadlocking on `join`.
- An event published concurrently with `unsubscribe` or `shutdown` may or may not be delivered. That's fine for at-most-once; say so out loud.
- A handler may publish from inside a handler (it only enqueues). With a blocking policy, a self-loop could deadlock, which is one reason drop-newest is the default.

## Extensions

- **Thousands of subscribers:** replace thread-per-subscriber with N workers and shard subscribers by `hash(sub_id) % N`. Ordering still holds, thread count is bounded.
- **Pluggable backpressure (Strategy):** move the `put_nowait` into an `OverflowPolicy` (drop newest, drop oldest, block with timeout) chosen per deployment.
- **At-least-once:** append-only log per topic, each subscription commits an offset after its handler succeeds, handlers dedupe on `event_id`. That's the Kafka consumer-group model.
- **Hierarchical topics** (`order.*`): replace the dict lookup in `publish` with a topic trie. Nothing else changes.
