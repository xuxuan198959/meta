"""
Interview question solutions.

Run the demos at the bottom with:  python3 solutions.py
"""

from typing import List


# ---------------------------------------------------------------------------
# Q1a. Verifying an Alien Dictionary (LeetCode 953)
# ---------------------------------------------------------------------------
# Given `words` and an alien alphabet `order`, return True iff `words` is
# sorted lexicographically according to `order`.
#
# Idea:
#   1. Map each letter -> its rank in `order` for O(1) comparison.
#   2. Compare each adjacent pair of words character by character.
#   3. Handle the prefix case: if a word is a prefix of the previous word
#      (previous is longer), the ordering is violated.
#
# Time  O(total number of characters)
# Space O(1) -- order has at most 26 letters.
def is_alien_sorted(words: List[str], order: str) -> bool:
    rank = {ch: i for i, ch in enumerate(order)}

    def in_order(a: str, b: str) -> bool:
        # True if a <= b under the alien order.
        for ca, cb in zip(a, b):
            if ca != cb:
                return rank[ca] < rank[cb]
        # All compared chars equal -> shorter (or equal) one must come first.
        return len(a) <= len(b)

    return all(in_order(words[i], words[i + 1]) for i in range(len(words) - 1))


# ---------------------------------------------------------------------------
# Q1b. Valid Palindrome II (LeetCode 680)
# ---------------------------------------------------------------------------
# Return True if `s` can become a palindrome after deleting at most one char.
#
# Idea:
#   Two pointers from both ends. On the first mismatch, try skipping the left
#   char OR the right char; if either remaining substring is a palindrome,
#   the whole string qualifies.
#
# Time  O(n)   Space O(1)
def valid_palindrome(s: str) -> bool:
    def is_pal(lo: int, hi: int) -> bool:
        while lo < hi:
            if s[lo] != s[hi]:
                return False
            lo += 1
            hi -= 1
        return True

    lo, hi = 0, len(s) - 1
    while lo < hi:
        if s[lo] != s[hi]:
            # Delete either the left or the right character.
            return is_pal(lo + 1, hi) or is_pal(lo, hi - 1)
        lo += 1
        hi -= 1
    return True


# ---------------------------------------------------------------------------
# Q2.1 Evaluate an arithmetic expression without parentheses
# ---------------------------------------------------------------------------
# Support + - * / on integers, e.g. "10/2+1*3+5" -> 13.
# The input may be invalid -> raise ValueError (or return an error marker).
#
# Idea (classic single-stack evaluator honoring precedence):
#   - Tokenize into numbers and operators.
#   - Scan left to right keeping the running operator (default '+').
#   - Push numbers for + / -, but for * and / combine immediately with the
#     top of the stack. The answer is sum(stack).
#
# Time  O(n)   Space O(n)
def calculate(expr: str) -> float:
    stack: List[float] = []
    num = 0
    have_digit = False
    op = "+"          # operator waiting to be applied to the current number
    i, n = 0, len(expr)

    def apply(op: str, value: float) -> None:
        if op == "+":
            stack.append(value)
        elif op == "-":
            stack.append(-value)
        elif op == "*":
            stack.append(stack.pop() * value)
        elif op == "/":
            prev = stack.pop()
            if value == 0:
                raise ValueError("division by zero")
            # Truncate toward zero, LeetCode-style integer division.
            stack.append(int(prev / value))
        else:
            raise ValueError(f"unknown operator: {op}")

    while i <= n:
        ch = expr[i] if i < n else ""
        if ch.isdigit():
            num = num * 10 + int(ch)
            have_digit = True
        elif ch == " ":
            pass
        elif ch in "+-*/" or ch == "":
            if not have_digit:                       # e.g. "10++2" or trailing op
                raise ValueError(f"invalid expression near index {i}")
            apply(op, num)
            op, num, have_digit = ch, 0, False
        else:
            raise ValueError(f"invalid character {ch!r} at index {i}")
        i += 1

    return sum(stack)


# ---------------------------------------------------------------------------
# Q2.2 vmstat-style line monitor
# ---------------------------------------------------------------------------
# Parse lines like the `vmstat` output. If the value in a chosen column
# exceeds a threshold a cumulative X times, print an error/warning.
#
# The header lines (non-numeric first field) are skipped. We track a running
# count of breaches and warn once the count reaches the required number of
# occurrences.
import argparse
import sys


def monitor_stream(stream, column: int, threshold: float, max_hits: int,
                   out=sys.stdout, err=sys.stderr) -> int:
    """
    Read `stream` line by line. For each data line, look at split()[column].
    Count how many times it exceeds `threshold`; once the cumulative count
    reaches `max_hits`, emit a warning. Returns total breach count.
    """
    breaches = 0
    warned = False
    for lineno, raw in enumerate(stream, 1):
        line = raw.strip()
        if not line:
            continue
        parts = line.split()
        # Skip header rows: a data row's target column must be numeric.
        if column >= len(parts):
            continue
        try:
            value = float(parts[column])
        except ValueError:
            continue  # header / non-numeric line

        if value > threshold:
            breaches += 1
            print(f"[line {lineno}] column {column} = {value} exceeds "
                  f"{threshold} ({breaches} times)", file=out)
            if breaches >= max_hits and not warned:
                print(f"ERROR: column {column} exceeded {threshold} "
                      f"{breaches} times (threshold hits reached)", file=err)
                warned = True
    return breaches


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        description="Warn when a column in vmstat-style input breaches a "
                    "threshold a cumulative number of times.")
    parser.add_argument("-c", "--column", type=int, required=True,
                        help="0-based index of the split() field to check")
    parser.add_argument("-t", "--threshold", type=float, required=True,
                        help="value above which a line counts as a breach")
    parser.add_argument("-x", "--max-hits", type=int, default=1,
                        help="warn once breaches reach this count (default 1)")
    parser.add_argument("file", nargs="?", default="-",
                        help="input file, or '-' for stdin (default)")
    args = parser.parse_args(argv)

    stream = sys.stdin if args.file == "-" else open(args.file)
    try:
        monitor_stream(stream, args.column, args.threshold, args.max_hits)
    finally:
        if stream is not sys.stdin:
            stream.close()
    return 0


# ---------------------------------------------------------------------------
# Demos / lightweight self-tests
# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
# Q5. Shortest Unique Prefix
# ---------------------------------------------------------------------------
# Given a list of words, for each word return the shortest prefix that
# uniquely identifies it among all the words. Return results in input order.
#
# Idea (Trie with counts):
#   1. Insert every word into a trie; each node stores how many words pass
#      through it (i.e. share that prefix).
#   2. For each word, walk down char by char. The shortest unique prefix ends
#      at the first node whose count == 1 (only this word passes through it).
#      If no such node exists (a duplicate word, or one word is a prefix of
#      another with the same count), the whole word is its own prefix.
#
# Assumes words are distinct (standard version of the problem). With N words
# of total length L: build O(L), query O(L) -> overall O(L).
def shortest_unique_prefixes(words: List[str]) -> List[str]:
    # Trie node: {child_char: node}, plus a "#count" of words through it.
    root: dict = {}

    def insert(word: str) -> None:
        node = root
        for ch in word:
            node = node.setdefault(ch, {})
            node["#count"] = node.get("#count", 0) + 1

    for w in words:
        insert(w)

    result = []
    for word in words:
        node = root
        prefix_len = len(word)          # fallback: entire word
        for i, ch in enumerate(word):
            node = node[ch]
            if node["#count"] == 1:
                prefix_len = i + 1
                break
        result.append(word[:prefix_len])
    return result


# ---------------------------------------------------------------------------
# Q6. Minimum Add to Make Parentheses Valid (LeetCode 921)
# ---------------------------------------------------------------------------
# Given a string of '(' and ')', return the minimum number of insertions
# needed to make it valid.
#
# Idea:
#   One pass tracking `open` = unmatched '('.
#   - '('        -> open += 1
#   - ')'        -> if open > 0 match it (open -= 1), else we must insert a
#                   '(' now: adds += 1
#   At the end, every remaining unmatched '(' needs a ')': adds += open.
#
# Time O(n)   Space O(1)
def min_add_to_make_valid(s: str) -> int:
    adds = 0      # insertions needed for unmatched ')'
    open_ = 0     # currently unmatched '('
    for ch in s:
        if ch == "(":
            open_ += 1
        elif ch == ")":
            if open_ > 0:
                open_ -= 1
            else:
                adds += 1
    return adds + open_


# ---------------------------------------------------------------------------
# Q7. Meeting Rooms II (LeetCode 253)
# ---------------------------------------------------------------------------
# Given meeting intervals [[start, end], ...], return the minimum number of
# rooms required so no meetings overlap in the same room.
#
# Idea (min-heap of end times):
#   Sort meetings by start. Keep a min-heap of end times of ongoing meetings.
#   For each meeting, if the earliest-ending room has freed up (its end <=
#   current start), reuse it (pop). Then push this meeting's end. The heap
#   size = rooms in use; its max over the scan is the answer.
#
# Time O(n log n)   Space O(n)
import heapq


def min_meeting_rooms(intervals: List[List[int]]) -> int:
    if not intervals:
        return 0
    intervals.sort(key=lambda iv: iv[0])
    heap: List[int] = []          # end times of meetings currently in rooms
    for start, end in intervals:
        if heap and heap[0] <= start:
            heapq.heappop(heap)   # earliest room is free -> reuse it
        heapq.heappush(heap, end)
    return len(heap)


# ---------------------------------------------------------------------------
# Q8. Binary Tree Right Side View (LeetCode 199)
# ---------------------------------------------------------------------------
# Return the values of the nodes visible from the right side, top to bottom.
#
# Idea (BFS level order): for each level, the last node dequeued is the one
# visible from the right. Collect those.
#
# Time O(n)   Space O(width)
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def right_side_view(root) -> List[int]:
    if not root:
        return []
    view = []
    q = deque([root])
    while q:
        level_size = len(q)
        for i in range(level_size):
            node = q.popleft()
            if i == level_size - 1:      # last node of this level
                view.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    return view


# ---------------------------------------------------------------------------
# Q9. Jump Game II (LeetCode 45)
# ---------------------------------------------------------------------------
# nums[i] = max forward jump length from index i. Return the minimum number
# of jumps to reach the last index (guaranteed reachable).
#
# Idea (greedy BFS by "layers"): scan left to right tracking `farthest` (the
# max index reachable so far) and `cur_end` (the boundary of the current
# jump's reach). When i hits cur_end we must take another jump, so bump the
# count and extend cur_end to farthest.
#
# Time O(n)   Space O(1)
def jump(nums: List[int]) -> int:
    n = len(nums)
    jumps = 0
    cur_end = 0        # farthest index reachable with `jumps` jumps
    farthest = 0       # farthest index reachable with one more jump
    for i in range(n - 1):            # no need to jump from the last index
        farthest = max(farthest, i + nums[i])
        if i == cur_end:              # exhausted current jump's range
            jumps += 1
            cur_end = farthest
            if cur_end >= n - 1:
                break
    return jumps


# ---------------------------------------------------------------------------
# Q10. In-Memory Database (CodeSignal-style 4-level assessment)
# ---------------------------------------------------------------------------
# A key-value store where each key holds a record = a dict of field -> value.
# Implemented as four progressively harder levels. The public API mirrors the
# usual assessment signatures; all timestamps are integers.
#
# Level 1 - basic CRUD on fields within a record:
#     set(key, field, value)          -> None
#     get(key, field)                 -> value or None
#     delete(key, field)              -> bool (True if a field was removed)
#
# Level 2 - scanning a record's fields:
#     scan(key)                       -> "f1(v1), f2(v2), ..." sorted by field
#     scan_by_prefix(key, prefix)     -> same, but only fields starting prefix
#
# Level 3 - TTL: every write can carry a timestamp and a lifespan (ttl). A
#   field is alive at time t iff  created_at <= t < created_at + ttl. The
#   non-timestamped Level 1/2 methods above are treated as ttl = infinite at
#   time 0, so earlier tests keep working.
#     set_at(key, field, value, timestamp, ttl=None)
#     get_at(key, field, timestamp)
#     delete_at(key, field, timestamp)
#     scan_at(key, timestamp)
#     scan_by_prefix_at(key, prefix, timestamp)
#
# Level 4 - backup & restore:
#     backup(timestamp)  -> snapshot all live fields with their REMAINING ttl
#     restore(timestamp, timestamp_to_restore)
#         -> restore the most recent backup taken at-or-before
#            timestamp_to_restore; each field's expiry is re-anchored to the
#            current `timestamp` (new expiry = timestamp + remaining_ttl).
#
# Representation: db[key][field] = (value, created_at, expire_at)
#   expire_at is None for "never expires".
INF = float("inf")


class InMemoryDB:
    def __init__(self):
        # key -> field -> (value, created_at, expire_at)
        self.db: dict = {}
        # timestamp -> snapshot dict (for backups), kept sorted-by-key on read
        self.backups: dict = {}

    # ---- helpers ----------------------------------------------------------
    @staticmethod
    def _alive(entry, t) -> bool:
        _, _, expire_at = entry
        return expire_at is None or t < expire_at

    def _live_fields(self, key, t) -> dict:
        """field -> value for all fields of key alive at time t."""
        rec = self.db.get(key, {})
        return {f: e[0] for f, e in rec.items() if self._alive(e, t)}

    @staticmethod
    def _format(fields: dict) -> str:
        return ", ".join(f"{f}({v})" for f, v in sorted(fields.items()))

    # ---- Level 3 (timestamped core; Levels 1/2 delegate here) ------------
    def set_at(self, key, field, value, timestamp, ttl=None):
        expire_at = None if ttl is None else timestamp + ttl
        self.db.setdefault(key, {})[field] = (value, timestamp, expire_at)

    def get_at(self, key, field, timestamp):
        entry = self.db.get(key, {}).get(field)
        if entry is None or not self._alive(entry, timestamp):
            return None
        return entry[0]

    def delete_at(self, key, field, timestamp) -> bool:
        rec = self.db.get(key)
        if not rec or field not in rec:
            return False
        if not self._alive(rec[field], timestamp):
            return False           # already expired -> nothing live to delete
        del rec[field]
        if not rec:
            del self.db[key]
        return True

    def scan_at(self, key, timestamp) -> str:
        return self._format(self._live_fields(key, timestamp))

    def scan_by_prefix_at(self, key, prefix, timestamp) -> str:
        fields = {f: v for f, v in self._live_fields(key, timestamp).items()
                  if f.startswith(prefix)}
        return self._format(fields)

    # ---- Level 1 & 2 (non-timestamped convenience wrappers) --------------
    def set(self, key, field, value):
        self.set_at(key, field, value, timestamp=0, ttl=None)

    def get(self, key, field):
        return self.get_at(key, field, timestamp=0)

    def delete(self, key, field) -> bool:
        return self.delete_at(key, field, timestamp=0)

    def scan(self, key) -> str:
        return self.scan_at(key, timestamp=0)

    def scan_by_prefix(self, key, prefix) -> str:
        return self.scan_by_prefix_at(key, prefix, timestamp=0)

    # ---- Level 4 (backup & restore) --------------------------------------
    def backup(self, timestamp) -> int:
        """Snapshot all live fields, storing REMAINING ttl (not absolute)."""
        snapshot: dict = {}
        live_count = 0
        for key, rec in self.db.items():
            saved = {}
            for field, (value, _created, expire_at) in rec.items():
                if self._alive((value, _created, expire_at), timestamp):
                    remaining = (None if expire_at is None
                                 else expire_at - timestamp)
                    saved[field] = (value, remaining)
                    live_count += 1
            if saved:
                snapshot[key] = saved
        self.backups[timestamp] = snapshot
        return live_count

    def restore(self, timestamp, timestamp_to_restore) -> None:
        """Restore the latest backup at-or-before timestamp_to_restore,
        re-anchoring each field's expiry to the current `timestamp`."""
        # Find most recent backup time <= timestamp_to_restore.
        candidates = [t for t in self.backups if t <= timestamp_to_restore]
        if not candidates:
            return
        snapshot = self.backups[max(candidates)]
        self.db = {}
        for key, saved in snapshot.items():
            rec = {}
            for field, (value, remaining) in saved.items():
                expire_at = None if remaining is None else timestamp + remaining
                rec[field] = (value, timestamp, expire_at)
            if rec:
                self.db[key] = rec


# ---------------------------------------------------------------------------
# Q11. Find the string that contains all other strings as substrings
# ---------------------------------------------------------------------------
# Given a list of strings, return the one string that contains EVERY other
# string in the list as a substring, or None if no such string exists.
#   ["programming", "am", "pro"] -> "programming"
#   ("am" is in progr[am]ming, "pro" is in [pro]gramming)
#
# --- Why this is optimal --------------------------------------------------
# 1. A container must be at least as long as every string it contains, and it
#    is itself in the list, so its length must equal the GLOBAL max length.
#    Hence the only viable candidate is a longest string -> O(1) candidates
#    instead of O(n). (If two DISTINCT longest strings exist, neither can
#    contain the other, so the substring check below naturally returns None.)
# 2. To test many patterns against one text in linear total time, build a
#    Suffix Automaton (SAM) of the candidate: O(L) build, and each pattern is
#    a membership walk in O(len(pattern)). Any path from the SAM's initial
#    state spells a substring of the text, so the walk succeeds iff the
#    pattern is a substring.
#
# Overall time O(total characters), space O(L). This beats the brute force
# O(n^2 * L) and the suffix-*trie* variant (O(L^2) space).
class _SuffixAutomaton:
    def __init__(self, s: str):
        self.next: List[dict] = [dict()]   # transitions per state
        self.link: List[int] = [-1]        # suffix links
        self.length: List[int] = [0]       # longest substring len in state
        self.last = 0
        for ch in s:
            self._extend(ch)

    def _extend(self, c: str) -> None:
        cur = len(self.length)
        self.length.append(self.length[self.last] + 1)
        self.link.append(-1)
        self.next.append(dict())
        p = self.last
        while p != -1 and c not in self.next[p]:
            self.next[p][c] = cur
            p = self.link[p]
        if p == -1:
            self.link[cur] = 0
        else:
            q = self.next[p][c]
            if self.length[p] + 1 == self.length[q]:
                self.link[cur] = q
            else:
                clone = len(self.length)
                self.length.append(self.length[p] + 1)
                self.next.append(dict(self.next[q]))
                self.link.append(self.link[q])
                while p != -1 and self.next[p].get(c) == q:
                    self.next[p][c] = clone
                    p = self.link[p]
                self.link[q] = clone
                self.link[cur] = clone
        self.last = cur

    def contains(self, pattern: str) -> bool:
        state = 0
        for ch in pattern:
            state = self.next[state].get(ch, -1)
            if state == -1:
                return False
        return True


def find_container(strings: List[str]):
    if not strings:
        return None
    # The only viable candidate is a longest string.
    cand_idx = max(range(len(strings)), key=lambda i: len(strings[i]))
    candidate = strings[cand_idx]
    sam = _SuffixAutomaton(candidate)
    for i, t in enumerate(strings):
        if i == cand_idx:
            continue                 # a string trivially contains itself
        if not sam.contains(t):      # includes the distinct-equal-length case
            return None
    return candidate


# --- Practical note: SAM vs. the simple version ----------------------------
# find_container above is the asymptotically OPTIMAL answer: O(total chars).
# But in a real interview, the Suffix Automaton is easy to get subtly wrong
# under time pressure. The version below keeps the same key insight (only the
# longest string can be the container) but delegates the substring test to
# Python's built-in `in`. CPython implements `in` with a tuned two-way string
# search in C, so it is effectively linear per check and extremely fast in
# practice. Worst-case time is O(candidate_len * n), yet it almost always
# wins on real inputs and is far less bug-prone. Prefer this unless the
# interviewer explicitly wants the linear-time-guaranteed structure.
def find_container_simple(strings: List[str]):
    if not strings:
        return None
    candidate = max(strings, key=len)            # only a longest string works
    return candidate if all(t in candidate for t in strings) else None
    # Note: `t in candidate` is True for t == candidate and for "", so the
    # candidate itself and empty strings are handled without special cases.


# ---------------------------------------------------------------------------
# Q12. Kth Largest Element in an Array (LeetCode 215)
# ---------------------------------------------------------------------------
# Return the k-th largest element (k-th in sorted order, not k-th distinct).
#
# Idea (min-heap of size k): keep the k largest elements seen so far in a
# min-heap. Its root is the smallest of those k -> the k-th largest overall.
# For each remaining element, if it beats the root, replace the root.
#
# Time O(n log k)   Space O(k)
# (Quickselect gives O(n) average time / O(1) space but is longer to write.)
def find_kth_largest(nums: List[int], k: int) -> int:
    heap = nums[:k]
    heapq.heapify(heap)
    for x in nums[k:]:
        if x > heap[0]:
            heapq.heapreplace(heap, x)   # pop smallest, push x
    return heap[0]


# ---------------------------------------------------------------------------
# Q13. Subarray Sum Equals K (LeetCode 560)
# ---------------------------------------------------------------------------
# Count contiguous subarrays whose sum equals k. Values may be negative.
#
# Idea (prefix sum + hash map): a subarray (i, j] sums to k iff
# prefix[j] - prefix[i] == k, i.e. prefix[i] == prefix[j] - k. Scan once
# keeping counts of every prefix sum seen; at each step add how many earlier
# prefixes equal (current_prefix - k). Seed {0: 1} for subarrays from index 0.
#
# Time O(n)   Space O(n)
def subarray_sum(nums: List[int], k: int) -> int:
    counts = {0: 1}          # prefix sum -> number of times it has occurred
    prefix = 0
    total = 0
    for x in nums:
        prefix += x
        total += counts.get(prefix - k, 0)
        counts[prefix] = counts.get(prefix, 0) + 1
    return total


def _run_self_tests() -> None:
    # Q1a
    assert is_alien_sorted(["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz")
    assert not is_alien_sorted(["word", "world", "row"],
                               "worldabcefghijkmnpqstuvxyz")
    assert not is_alien_sorted(["apple", "app"],
                               "abcdefghijklmnopqrstuvwxyz")  # prefix case

    # Q1b
    assert valid_palindrome("aba")
    assert valid_palindrome("abca")      # delete 'c' (or 'b')
    assert not valid_palindrome("abc")

    # Q2.1
    assert calculate("10/2+1*3+5") == 13
    assert calculate("3+2*2") == 7
    assert calculate(" 3/2 ") == 1
    try:
        calculate("10++2")
        raise AssertionError("expected ValueError")
    except ValueError:
        pass

    # Q5
    assert shortest_unique_prefixes(["zebra", "dog", "duck", "dove"]) == \
        ["z", "dog", "du", "dov"]
    assert shortest_unique_prefixes(["flower", "flow", "flight"]) == \
        ["flowe", "flow", "fli"]
    # "flow" is a prefix of "flower", so the "flow" node has count 2 ->
    # "flower" must extend to "flowe", and "flow" falls back to itself.
    assert shortest_unique_prefixes(["cat"]) == ["c"]
    assert shortest_unique_prefixes(["abc", "abcd"]) == ["abc", "abcd"]

    # Q6
    assert min_add_to_make_valid("())") == 1
    assert min_add_to_make_valid("(((") == 3
    assert min_add_to_make_valid("()") == 0
    assert min_add_to_make_valid("()))((") == 4

    # Q7
    assert min_meeting_rooms([[0, 30], [5, 10], [15, 20]]) == 2
    assert min_meeting_rooms([[7, 10], [2, 4]]) == 1
    assert min_meeting_rooms([]) == 0
    assert min_meeting_rooms([[1, 5], [2, 6], [3, 7]]) == 3
    # Meetings that only touch at endpoints don't overlap.
    assert min_meeting_rooms([[1, 5], [5, 10]]) == 1

    # Q8   tree:      1
    #               /   \
    #              2     3
    #               \     \
    #                5     4
    root = TreeNode(1,
                    TreeNode(2, None, TreeNode(5)),
                    TreeNode(3, None, TreeNode(4)))
    assert right_side_view(root) == [1, 3, 4]
    assert right_side_view(None) == []
    assert right_side_view(TreeNode(1, TreeNode(2))) == [1, 2]  # left-only lvl

    # Q9
    assert jump([2, 3, 1, 1, 4]) == 2      # 0->1->4
    assert jump([2, 3, 0, 1, 4]) == 2
    assert jump([0]) == 0                   # already at the end
    assert jump([1, 1, 1, 1]) == 3

    # Q10 - Level 1 & 2
    db = InMemoryDB()
    db.set("a", "f1", "1")
    db.set("a", "f2", "2")
    db.set("a", "bar", "9")
    assert db.get("a", "f1") == "1"
    assert db.get("a", "missing") is None
    assert db.scan("a") == "bar(9), f1(1), f2(2)"
    assert db.scan_by_prefix("a", "f") == "f1(1), f2(2)"
    assert db.delete("a", "f1") is True
    assert db.delete("a", "f1") is False
    assert db.scan("a") == "bar(9), f2(2)"

    # Q10 - Level 3 (TTL)
    db = InMemoryDB()
    db.set_at("x", "f", "v", timestamp=10, ttl=5)   # alive for t in [10, 15)
    assert db.get_at("x", "f", 10) == "v"
    assert db.get_at("x", "f", 14) == "v"
    assert db.get_at("x", "f", 15) is None          # expired
    db.set_at("x", "g", "w", timestamp=10)          # no ttl -> never expires
    assert db.scan_at("x", 14) == "f(v), g(w)"
    assert db.scan_at("x", 15) == "g(w)"            # f gone

    # Q10 - Level 4 (backup & restore)
    db = InMemoryDB()
    db.set_at("k", "a", "1", timestamp=0, ttl=10)   # expires at 10
    db.set_at("k", "b", "2", timestamp=0)           # never expires
    assert db.backup(5) == 2                         # both live at t=5
    # 'a' had remaining ttl = 10 - 5 = 5 at backup time.
    db.set_at("k", "c", "3", timestamp=6)           # extra write after backup
    db.restore(timestamp=100, timestamp_to_restore=5)
    assert db.get_at("k", "c", 100) is None         # not in the backup
    assert db.get_at("k", "b", 100) == "2"          # never-expire survives
    assert db.get_at("k", "a", 104) == "1"          # re-anchored: 100 + 5 = 105
    assert db.get_at("k", "a", 105) is None          # expires at 105
    # Restoring with no eligible backup is a no-op.
    db.restore(timestamp=200, timestamp_to_restore=1)
    assert db.get_at("k", "a", 104) == "1"

    # Q11
    assert find_container(["programming", "am", "pro"]) == "programming"
    assert find_container(["hello", "ell", "he", "lo"]) == "hello"
    assert find_container(["abcd", "bc", "cd", "a"]) == "abcd"
    assert find_container(["abc", ""]) == "abc"          # "" is a substring
    assert find_container(["x"]) == "x"                  # no others to contain
    assert find_container(["aa", "aa"]) == "aa"          # duplicate of longest
    assert find_container([]) is None
    assert find_container(["abc", "d"]) is None          # "d" not in "abc"
    assert find_container(["abc", "abd"]) is None         # distinct, same length
    assert find_container(["hello", "ell", "z"]) is None  # "z" missing

    # Q11 - the simple version must agree with the optimal one.
    for case in (["programming", "am", "pro"], ["hello", "ell", "he", "lo"],
                 ["abcd", "bc", "cd", "a"], ["abc", ""], ["x"], ["aa", "aa"],
                 [], ["abc", "d"], ["abc", "abd"], ["hello", "ell", "z"]):
        assert find_container_simple(case) == find_container(case)

    # Q12
    assert find_kth_largest([3, 2, 1, 5, 6, 4], 2) == 5
    assert find_kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
    assert find_kth_largest([1], 1) == 1
    assert find_kth_largest([7, 7, 7], 2) == 7      # duplicates, not distinct

    # Q13
    assert subarray_sum([1, 1, 1], 2) == 2
    assert subarray_sum([1, 2, 3], 3) == 2
    assert subarray_sum([1, -1, 0], 0) == 3          # negatives / zero sums
    assert subarray_sum([3, 4, 7, 2, -3, 1, 4, 2], 7) == 4

    print("All self-tests passed.")


if __name__ == "__main__":
    # With CLI args -> run the vmstat monitor (Q2.2). No args -> self-tests.
    # Q2.2 usage, e.g.
    #   vmstat 1 | python3 solutions.py --column 3 --threshold 1000000 --max-hits 3
    # (column 3 is 'free' in the sample header)
    if len(sys.argv) > 1:
        sys.exit(main())
    else:
        _run_self_tests()
