# File Search with Composable Filters (Unix `find`)

**Prompt.** Implement a `find`-like file search that walks a directory tree and returns files matching composable filters (name, extension, size, ...) combined with AND / OR / NOT. (★ 📣 AWS Dublin, Aug 2026; 2 reports + variant: [8464434](https://leetcode.com/discuss/post/8464434/), [8522985](https://leetcode.com/discuss/post/8522985/), [8353900](https://leetcode.com/discuss/post/8353900/))

## Clarifying questions

- **Real disk or in-memory?** A small `FileSystem` interface (`stat`, `list_dir`) with an in-memory version for the interview; an `os.scandir` adapter is a few lines.
- **Do directories match?** Only files are returned; directories are traversed.
- **Which filters?** Name glob, extension, size range. Modified time, owner, etc. must be addable without touching existing code.
- **How are filters combined?** Arbitrary nesting of AND / OR / NOT, like `find \( -name "*.log" -o -size +5M \) ! -name "tmp*"`.
- **Huge trees? Symlinks?** Lazy results, iterative walk, optional `max_depth`. Symlinks not followed.

## Core classes

| Class | Responsibility | Pattern |
|---|---|---|
| `FileEntry` | Immutable metadata: path, size, is_dir; derived name/extension | Value object |
| `InMemoryFileSystem` | `stat` + `list_dir`; swappable for a real-disk adapter | Adapter / port |
| `Spec` + `NameGlob`, `ExtensionIs`, `SizeRange` | `matches(entry)`, with `&`, `\|`, `~` operators | Specification |
| `AllOf`, `AnyOf`, `Not` | Specs built from specs | Composite |
| `FileSearcher` | BFS over directories, yields matching files | Service |

## Code

```python
from __future__ import annotations

import fnmatch
from collections import deque
from dataclasses import dataclass


@dataclass(frozen=True)
class FileEntry:
    path: str
    size: int = 0
    is_dir: bool = False

    @property
    def name(self) -> str:
        return self.path.rsplit("/", 1)[-1]

    @property
    def extension(self) -> str:
        stem, dot, ext = self.name.rpartition(".")
        return ext.lower() if dot and stem else ""   # ".bashrc" has no extension


class InMemoryFileSystem:
    def __init__(self):
        self.entries = {"/": FileEntry("/", is_dir=True)}

    def add_file(self, path: str, size: int) -> None:
        parts = path.strip("/").split("/")
        for i in range(1, len(parts)):                    # create missing parent dirs
            d = "/" + "/".join(parts[:i])
            self.entries.setdefault(d, FileEntry(d, is_dir=True))
        self.entries[path] = FileEntry(path, size)

    def stat(self, path: str) -> FileEntry:
        if path not in self.entries:
            raise FileNotFoundError(path)
        return self.entries[path]

    def list_dir(self, path: str) -> list[FileEntry]:     # O(n) scan: fine for a test double
        return [e for p, e in self.entries.items()
                if p != "/" and (p.rsplit("/", 1)[0] or "/") == path]


class Spec:
    def matches(self, e: FileEntry) -> bool:
        raise NotImplementedError

    def __and__(self, other): return AllOf(self, other)
    def __or__(self, other): return AnyOf(self, other)
    def __invert__(self): return Not(self)


@dataclass(frozen=True)
class NameGlob(Spec):
    pattern: str
    def matches(self, e): return fnmatch.fnmatchcase(e.name, self.pattern)

@dataclass(frozen=True)
class ExtensionIs(Spec):
    ext: str
    def matches(self, e): return e.extension == self.ext.lower().lstrip(".")

@dataclass(frozen=True)
class SizeRange(Spec):
    lo: int = 0
    hi: float = float("inf")
    def matches(self, e): return self.lo <= e.size <= self.hi


class AllOf(Spec):
    def __init__(self, *specs): self.specs = specs
    def matches(self, e): return all(s.matches(e) for s in self.specs)  # empty -> True

class AnyOf(AllOf):
    def matches(self, e): return any(s.matches(e) for s in self.specs)  # empty -> False

class Not(Spec):
    def __init__(self, spec): self.spec = spec
    def matches(self, e): return not self.spec.matches(e)


class FileSearcher:
    def __init__(self, fs):
        self.fs, self.skipped = fs, []        # skipped: unreadable dirs

    def search(self, root: str, spec: Spec, max_depth: int | None = None):
        start = self.fs.stat(root)            # missing root fails before any yield
        if not start.is_dir:
            if spec.matches(start):
                yield start
            return
        queue = deque([(start, 0)])           # iterative BFS: no recursion limit
        while queue:
            d, depth = queue.popleft()
            try:
                children = self.fs.list_dir(d.path)
            except PermissionError:
                self.skipped.append(d.path)   # partial results beat a crash
                continue
            for c in children:
                if c.is_dir:
                    if max_depth is None or depth < max_depth:
                        queue.append((c, depth + 1))
                elif spec.matches(c):
                    yield c


if __name__ == "__main__":
    fs = InMemoryFileSystem()
    fs.add_file("/var/log/app.log", 8_000_000)
    fs.add_file("/var/log/tmp_debug.log", 9_000_000)
    fs.add_file("/var/log/old/app.1.log", 1_000)
    fs.add_file("/home/aaron/notes.txt", 200)
    fs.add_file("/home/aaron/video.mp4", 700_000_000)
    query = (ExtensionIs("log") | SizeRange(lo=100_000_000)) & ~NameGlob("tmp*")
    searcher = FileSearcher(fs)
    print([e.path for e in searcher.search("/", query)])  # BFS order:
    # ['/var/log/app.log', '/home/aaron/video.mp4', '/var/log/old/app.1.log']
    print([e.name for e in searcher.search("/var", ExtensionIs("LOG"), max_depth=1)])
    # ['app.log', 'tmp_debug.log']   (/var/log/old is depth 2, not entered)
```

## Design choices

- **Specification + Composite.** Every criterion is a `Spec`; `AllOf`/`AnyOf`/`Not` are also `Spec`s, so any tree of conditions works and `(ext | big) & ~tmp` reads like the query. A new filter (`ModifiedAfter`) is one class (Open/Closed).
- **Traversal separate from matching.** `FileSearcher` walks, specs decide. BFS vs DFS, or memory vs disk, change without touching filters.
- **Generator + iterative walk.** Lazy results let "first 10" stop the walk early; an explicit queue avoids Python's recursion limit on deep trees.

## Edge cases

- Missing root raises `FileNotFoundError` before any yield; a file root is tested directly.
- Dotfiles: `.bashrc` has no extension, matching Unix convention. Extension match is case-insensitive; glob is case-sensitive like `find -name`.
- Empty `AllOf()` matches everything, empty `AnyOf()` nothing (vacuous truth). Say it out loud.
- Unreadable directories are skipped and recorded in `skipped`, so the search returns partial results. `max_depth=0` means root's direct files only.

## Extensions

- **Symlinks.** Add `is_symlink`/`real_path` and a `follow_symlinks` flag; keep a `visited` set of real paths to break cycles.
- **Expensive filters (content hash, grep).** Give `Spec` a `cost` and sort `AllOf` children cheapest first so short-circuiting skips the costly check.
- **Prune directories** (`-prune`, skip `node_modules`). An optional `descend_into: Spec` checked before enqueuing a directory.
- **Parallel search.** Thread pool where each task lists one directory and submits subdirectories; results flow through a queue. Specs are immutable, so they're shared without locks.
