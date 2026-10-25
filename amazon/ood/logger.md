# In-Memory Logger with a Fixed-Size Flash Buffer

**Prompt.** Design a logger that keeps recent log records in a fixed-size in-memory (flash) buffer, supports levels, and writes to pluggable sinks. (★ 📣 2 reports: [8523912](https://leetcode.com/discuss/post/8523912/), [8567817](https://leetcode.com/discuss/post/8567817/))

## Clarifying questions

- **Buffer full?** Overwrite the oldest record (ring buffer) and count it. It's "the last N records", like a flight recorder.
- **When do we flush to sinks?** On explicit `flush()`, at a high-water mark, and immediately on `ERROR`+ so the context before a crash is persisted.
- **Levels?** DEBUG < INFO < WARN < ERROR < FATAL. Records below the logger's minimum are dropped before buffering; each sink can also filter.
- **Which sinks?** Console and in-memory behind an interface. A sink failure must never crash the app.
- **Capacity in records or bytes?** Records. Bytes is an extension.
- **Thread safety?** Yes. Sink I/O happens outside the buffer lock.

## Core classes

| Class | Responsibility | Pattern |
|---|---|---|
| `Level`, `LogRecord` | Ordered severity; immutable entry that formats itself | IntEnum, value object |
| `RingBuffer` | Fixed capacity, O(1) append, overwrite oldest, drain | Data structure |
| `Sink` + `ConsoleSink`, `MemorySink` | Per-sink level filter, then write lines | Strategy + Template Method |
| `Logger` | Filter, buffer, decide when to flush, fan out to sinks | Facade |

## Code

```python
from __future__ import annotations

import itertools
import threading
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime
from enum import IntEnum


class Level(IntEnum):
    DEBUG, INFO, WARN, ERROR, FATAL = 10, 20, 30, 40, 50

@dataclass(frozen=True)
class LogRecord:
    timestamp: datetime
    level: Level
    name: str
    message: str
    context: dict = field(default_factory=dict)

    def format(self) -> str:
        ctx = " ".join(f"{k}={v}" for k, v in self.context.items())
        return f"{self.timestamp:%H:%M:%S} {self.level.name:<5} {self.name}: {self.message} {ctx}".rstrip()

class RingBuffer:
    """Fixed capacity, O(1) append, overwrites the oldest. Not thread-safe; Logger locks."""

    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("capacity must be positive")
        self.capacity, self.slots = capacity, [None] * capacity
        self.head = self.size = self.overwritten = 0  # head = index of the oldest

    def append(self, item) -> None:
        self.slots[(self.head + self.size) % self.capacity] = item
        if self.size == self.capacity:
            self.head = (self.head + 1) % self.capacity  # oldest overwritten
            self.overwritten += 1
        else:
            self.size += 1

    def snapshot(self) -> list:  # oldest first
        return [self.slots[(self.head + i) % self.capacity] for i in range(self.size)]

    def drain(self) -> list:
        items = self.snapshot()
        self.slots, self.head, self.size = [None] * self.capacity, 0, 0
        return items

class Sink(ABC):
    def __init__(self, min_level: Level = Level.DEBUG):
        self.min_level = min_level

    def write_batch(self, records: list[LogRecord]) -> None:  # template method
        lines = [r.format() for r in records if r.level >= self.min_level]
        if lines:
            self.write(lines)

    @abstractmethod
    def write(self, lines: list[str]) -> None: ...

class ConsoleSink(Sink):
    def write(self, lines): print("\n".join(lines))

class MemorySink(Sink):
    def __init__(self, min_level: Level = Level.DEBUG):
        super().__init__(min_level)
        self.lines: list[str] = []

    def write(self, lines): self.lines.extend(lines)

class Logger:
    def __init__(self, name: str, capacity: int, sinks: list[Sink], min_level: Level = Level.INFO,
                 flush_level: Level = Level.ERROR, watermark: float | None = 0.8, clock=datetime.now):
        self.name, self.sinks, self.min_level, self.clock = name, sinks, min_level, clock
        self.flush_level, self.watermark = flush_level, watermark  # watermark=None disables it
        self.buffer = RingBuffer(capacity)
        self.lock = threading.Lock()        # guards the buffer; held only briefly
        self.flush_lock = threading.Lock()  # keeps batches in order across flushing threads
        self.sink_errors = 0

    def log(self, level: Level, message: str, **context) -> None:
        if level < self.min_level:
            return                          # disabled levels are nearly free: no lock
        with self.lock:
            self.buffer.append(LogRecord(self.clock(), level, self.name, message, context))
            full = self.watermark is not None and self.buffer.size >= self.watermark * self.buffer.capacity
        if level >= self.flush_level or full:
            self.flush()

    def debug(self, msg, **ctx): self.log(Level.DEBUG, msg, **ctx)
    def error(self, msg, **ctx): self.log(Level.ERROR, msg, **ctx)

    def recent(self) -> list[LogRecord]:
        with self.lock:
            return self.buffer.snapshot()

    def flush(self) -> int:
        with self.flush_lock:
            with self.lock:                 # swap records out under the lock...
                batch = self.buffer.drain()
            for sink in self.sinks:         # ...and do slow I/O without blocking loggers
                try:
                    sink.write_batch(batch)
                except Exception:           # a logger must never crash its host
                    self.sink_errors += 1
            return len(batch)

if __name__ == "__main__":
    ticks, memory = itertools.count(), MemorySink()
    logger = Logger("orders", capacity=5, sinks=[ConsoleSink(Level.WARN), memory], min_level=Level.DEBUG,
                    watermark=None, clock=lambda: datetime(2026, 1, 1, 12, 0, next(ticks)))
    for i in range(7):
        logger.debug("cache miss", order_id=i)          # 7 records into 5 slots
    print("buffered:", [r.context["order_id"] for r in logger.recent()])  # [2, 3, 4, 5, 6]
    logger.error("payment declined", order_id=6)         # auto-flush; console (WARN+) prints only:
    # 12:00:07 ERROR orders: payment declined order_id=6
    print("memory got", len(memory.lines), "lines; buffer now", len(logger.recent()))  # 5 lines; 0
```

## Design choices

- **Ring buffer as the flash buffer.** Fixed memory however chatty the app is, O(1) append, and overflow loses the oldest (least useful) records. Head-plus-size index math avoids shifting a list.
- **Flush on severity (flight recorder).** DEBUG records are cheap while buffered; when an ERROR arrives, the last N records including debug context are persisted. That's the reason to buffer at all.
- **Sinks as Strategy, short critical section.** A new destination is a new `Sink`; the base class does level filtering (Template Method). The buffer lock covers only append or drain; `flush_lock` keeps concurrent flushes from interleaving batches.

## Edge cases

- Capacity ≤ 0 raises `ValueError`.
- Overflow overwrites the oldest and bumps `overwritten` (demo keeps orders 2–6; the ERROR then pushes out 2).
- Per-sink levels: console shows only WARN+, the memory sink gets the full debug context.
- Empty flush returns 0 and doesn't call sinks.
- A sink that raises is counted in `sink_errors`; other sinks still get the batch.

## Extensions

- **Async flushing:** `log()` sets a signal; a daemon thread waits on it (with a timeout for periodic flushes) and calls `flush()`. Add an `atexit` final flush.
- **More strategies:** `FileSink`, a JSON `Formatter`, or a `FlushPolicy` class ("every 5 s") once a second variant is needed.
- **Capacity in bytes:** track total bytes and evict from the head while `bytes + new > max`; truncate a single oversized record.
- **Real flash (survives crashes):** back the ring with a memory-mapped file of fixed-size slots and keep `head` in a header, as routers do for crash logs.
