"""
Interview question solutions.

Run the demos at the bottom with:  python3 solutions.py
"""

from typing import List


# ---------------------------------------------------------------------------
# Q1. Verifying an Alien Dictionary (LeetCode 953)
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
# Q2. Valid Palindrome II (LeetCode 680)
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
# Q3. Evaluate an arithmetic expression without parentheses
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
# Q4. vmstat-style line monitor
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


# ---------------------------------------------------------------------------
# Q14. Best Rating-to-Price Index
# ---------------------------------------------------------------------------
# Given equal-length arrays `rating` and `prices` (prices > 0), return the index
# that maximizes rating[i] / prices[i]. On ties, return the smallest index.
#
# Idea: never divide. Compare ratios by cross-multiplication --
#   rating[i]/prices[i] > rating[b]/prices[b]  <=>  rating[i]*prices[b] > rating[b]*prices[i]
# (valid because prices are positive). Update only on a STRICT improvement so
# the earliest index wins ties.
#
# Time O(n)   Space O(1)
def best_ratio_index(rating: List[int], prices: List[int]) -> int:
    best = 0
    for i in range(1, len(rating)):
        if rating[i] * prices[best] > rating[best] * prices[i]:
            best = i
    return best


# ---------------------------------------------------------------------------
# Q15. Complete Round-Trip Missions
# ---------------------------------------------------------------------------
# Complete `missions` round trips A<->B. `a2b` and `b2a` are ascending lists of
# departure times. Each leg boards the earliest departure not earlier than the
# current time. Return the time all missions finish.
#
# Idea: keep a running `current` time. For each mission binary-search a2b for the
# first time >= current (that becomes current), then do the same in b2a. Sorted
# input makes each lookup O(log n).
#
# Time O(missions * log n)   Space O(1)
import bisect


def round_trip_time(a2b: List[int], b2a: List[int], missions: int,
                    start: int = 0) -> int:
    current = start
    for _ in range(missions):
        current = a2b[bisect.bisect_left(a2b, current)]   # earliest A->B >= now
        current = b2a[bisect.bisect_left(b2a, current)]   # earliest B->A >= that
    return current


# ---------------------------------------------------------------------------
# Q16. Apply Matrix Commands
# ---------------------------------------------------------------------------
# Apply a list of commands to a 2D array and return the result. Commands:
#   ("swap_row", i, j) / ("swap_col", i, j) / ("reverse_row", i) /
#   ("reverse_col", i) / ("rotate",)  -- rotate 90 degrees clockwise.
#
# Idea: swaps and reversals are direct index work. A 90-degree clockwise
# rotation = transpose (swap rows with columns) then reverse each row.
#
# Time O(cells) per command   Space O(cells) for the working copy
def apply_matrix_commands(matrix: List[List[int]],
                          commands: List[tuple]) -> List[List[int]]:
    m = [row[:] for row in matrix]        # work on a copy
    for cmd in commands:
        op = cmd[0]
        if op == "swap_row":
            _, i, j = cmd
            m[i], m[j] = m[j], m[i]
        elif op == "swap_col":
            _, i, j = cmd
            for row in m:
                row[i], row[j] = row[j], row[i]
        elif op == "reverse_row":
            _, i = cmd
            m[i].reverse()
        elif op == "reverse_col":
            _, i = cmd
            col = [row[i] for row in m][::-1]
            for row, v in zip(m, col):
                row[i] = v
        elif op == "rotate":
            m = [list(row) for row in zip(*m)]   # transpose
            for row in m:
                row.reverse()                    # then reverse each row
        else:
            raise ValueError(f"unknown command: {op}")
    return m


# ---------------------------------------------------------------------------
# Q17. Count Access-Code Pairs
# ---------------------------------------------------------------------------
# Count ordered index pairs (i, j) with words[i] + words[j] == accesscode. The
# indices are chosen independently, so i == j is allowed when both halves match.
#
# Idea: count each string's frequency. Split accesscode at every position into
# (left, right); each split contributes count[left] * count[right] pairs. Sum
# over all splits.
#
# Time O(len(accesscode)^2) for slicing (or O(L) with rolling hashes)   Space O(n)
from collections import Counter


def count_access_pairs(words: List[str], accesscode: str) -> int:
    counts = Counter(words)
    total = 0
    for k in range(len(accesscode) + 1):
        total += counts[accesscode[:k]] * counts[accesscode[k:]]
    return total


# ---------------------------------------------------------------------------
# Q18. Merge Three Sorted Arrays, dedup (LeetCode 88 variant)
# ---------------------------------------------------------------------------
# Merge three ascending arrays into one ascending array with all duplicates
# removed (repeats within an array AND values shared across arrays).
#
# Idea (three pointers): repeatedly take the smallest of the three current
# heads. Advance every pointer whose head equals that value (drops cross-array
# dupes), and append it only if it differs from the last value written (drops
# within-array dupes).
#
# Time O(total elements)   Space O(unique elements) for the output
# (heapq.merge(a, b, c) + a consecutive-dedup pass is a one-line alternative.)
def merge_three_sorted(a: List[int], b: List[int], c: List[int]) -> List[int]:
    i = j = k = 0
    out: List[int] = []
    while i < len(a) or j < len(b) or k < len(c):
        heads = []
        if i < len(a):
            heads.append(a[i])
        if j < len(b):
            heads.append(b[j])
        if k < len(c):
            heads.append(c[k])
        smallest = min(heads)
        # Advance every array whose head equals the smallest (cross-array dedup).
        if i < len(a) and a[i] == smallest:
            i += 1
        if j < len(b) and b[j] == smallest:
            j += 1
        if k < len(c) and c[k] == smallest:
            k += 1
        # Append only if new (within-array dedup).
        if not out or out[-1] != smallest:
            out.append(smallest)
    return out


# ---------------------------------------------------------------------------
# Q19. Simplify Path (LeetCode 71)
# ---------------------------------------------------------------------------
# Given an absolute Unix-style path (always starts with '/'), return its
# canonical form: '.' = current dir, '..' = parent dir, collapse repeated
# slashes, and no trailing slash (except the root itself).
#
# Idea: canonicalize with a stack -- skip '' and '.', pop on '..' (unless
# already at root), push any real name.
#
# Time O(len of path)   Space O(len of path)
def simplify_path(path: str) -> str:
    stack: List[str] = []
    for part in path.split("/"):
        if part in ("", "."):
            continue
        if part == "..":
            if stack:                 # can't go above the root
                stack.pop()
        else:
            stack.append(part)
    return "/" + "/".join(stack)


# ---------------------------------------------------------------------------
# Q20. Binary Tree Vertical Order Traversal (LeetCode 314)
# ---------------------------------------------------------------------------
# Group node values by column (left to right); within a column, top to bottom,
# and left to right for nodes sharing a row and column.
#
# Idea (DFS): carry (row, col) down the tree -- root is col 0, left child
# col-1, right child col+1. Record (row, value) per column. Pre-order with the
# left child first records same-depth nodes left to right, so a stable sort by
# row per column reproduces the required order. DFS uses the recursion stack
# (O(height)) instead of an explicit BFS queue (O(width)).
#
# Time O(n log n) (sorting each column)   Space O(n) map + O(height) stack
def vertical_order(root) -> List[List[int]]:
    cols: dict = {}          # col -> list of (row, value) in pre-order

    def dfs(node, row, col):
        if not node:
            return
        cols.setdefault(col, []).append((row, node.val))
        dfs(node.left, row + 1, col - 1)
        dfs(node.right, row + 1, col + 1)

    dfs(root, 0, 0)
    result = []
    for col in sorted(cols):
        # Stable sort by row; DFS already ordered ties left to right.
        ordered = sorted(cols[col], key=lambda rv: rv[0])
        result.append([val for _row, val in ordered])
    return result


# ---------------------------------------------------------------------------
# Q21. Find a Local Minimum (LeetCode 162 variant)
# ---------------------------------------------------------------------------
# Return the index of any local minimum (strictly smaller than both neighbors);
# out-of-bounds neighbors count as +inf, so one always exists. Adjacent
# elements are assumed to differ. Iterative binary search, O(log n).
#
# Idea: at mid, compare only nums[mid] vs nums[mid+1] (a single check).
#   nums[mid] > nums[mid+1] -> slope descends right, a min is in [mid+1, hi].
#   otherwise                -> a min is in [lo, mid].
# The window shrinks to one index -- a local minimum.
#
# Time O(log n)   Space O(1)
def find_local_min(nums: List[int]) -> int:
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] > nums[mid + 1]:
            lo = mid + 1
        else:
            hi = mid
    return lo


# O(n) alternative: a `prev` pointer (initially +inf) detects the first index
# whose value is below both its previous and next neighbor.
def find_local_min_linear(nums: List[int]) -> int:
    prev = INF
    for i, x in enumerate(nums):
        nxt = nums[i + 1] if i + 1 < len(nums) else INF
        if prev > x < nxt:
            return i
        prev = x
    return -1


# ---------------------------------------------------------------------------
# Q22. Randomized Container: insert / pop_random in O(1) (LeetCode 380 variant)
# ---------------------------------------------------------------------------
# insert(element)  -- add an element
# pop_random()     -- remove and return a uniformly random element
#
# Idea: keep a dynamic array of elements plus a hash map element -> its index in
# that array. pop_random picks a random index, swaps that element with the last
# one (fixing the moved element's stored index), then pops the tail -- O(1)
# removal instead of shifting. Assumes distinct elements (see LeetCode 381 for
# duplicates: map value -> set of indices).
import random


class RandomizedContainer:
    def __init__(self):
        self.items: List = []          # the elements
        self.index: dict = {}          # element -> position in self.items

    def insert(self, element) -> None:
        self.index[element] = len(self.items)
        self.items.append(element)

    def pop_random(self):
        if not self.items:
            raise IndexError("pop_random from empty container")
        i = random.randrange(len(self.items))
        value = self.items[i]
        last = self.items[-1]
        # Move the last element into slot i, then drop the tail.
        self.items[i] = last
        self.index[last] = i
        self.items.pop()
        del self.index[value]
        return value

    def __len__(self) -> int:
        return len(self.items)


# ---------------------------------------------------------------------------
# Q23. Count Distinct Values in a Sorted Array (K << n)
# ---------------------------------------------------------------------------
# The array is sorted with only K distinct values, K much smaller than n.
#
# Idea: for each distinct value, binary-search the first index whose value is
# strictly greater and jump there; K jumps, each O(log n) -> O(K log n). Landing
# on the first strictly-greater index prevents counting a value twice.
#
# Time O(K log n)   Space O(1)
def count_distinct(arr: List[int]) -> int:
    n = len(arr)
    count = 0
    i = 0
    while i < n:
        count += 1
        i = bisect.bisect_right(arr, arr[i], i, n)   # first index > arr[i]
    return count


# Baseline O(n): a prev pointer counts each time the value changes.
def count_distinct_linear(arr: List[int]) -> int:
    count = 0
    prev = None
    for x in arr:
        if count == 0 or x != prev:
            count += 1
        prev = x
    return count


# ---------------------------------------------------------------------------
# Q25. Plan Round Trip With Minimum Flight Cost
# ---------------------------------------------------------------------------
# Given departure costs D and return costs R (per day, same length), pick days
# i < j minimizing D[i] + R[j]. Return (departure_index, return_index, cost).
# Tie-break: minimum cost, then earliest departure, then latest return.
#
# Idea: scan the return day j left to right, keeping the minimum departure cost
# in D[0..j-1] (earliest index on ties). For each j the best trip returning on
# day j is min_dep + R[j]; compare against the global best with the tie-break
# rules. min_i is non-decreasing, so the "earlier departure" branch never fires
# for a later j, but it is kept for correctness/clarity.
#
# Time O(n)   Space O(1)
def plan_round_trip(D: List[int], R: List[int]):
    n = min(len(D), len(R))
    if n < 2:
        return None                    # need at least one valid pair i < j
    best = None                        # (cost, dep, ret)
    min_i = 0                          # earliest index of the running min in D
    for j in range(1, n):
        i = j - 1
        if D[i] < D[min_i]:            # strict '<' keeps the earliest on ties
            min_i = i
        cost = D[min_i] + R[j]
        if best is None:
            best = (cost, min_i, j)
        else:
            bc, bi, bj = best
            if (cost < bc
                    or (cost == bc and min_i < bi)
                    or (cost == bc and min_i == bi and j > bj)):
                best = (cost, min_i, j)
    cost, dep, ret = best
    return dep, ret, cost


# ---------------------------------------------------------------------------
# Q26. Maximum Characters From Non-Overlapping Words (AI-enabled; cf. LC 1239)
# ---------------------------------------------------------------------------
# Choose a subset of lowercase words whose letter sets are pairwise disjoint,
# maximizing the total number of distinct characters captured.
#
# Idea: encode each word as a 26-bit letter mask; its value is the popcount.
# Backtrack over the words with a `used` mask -- a word fits iff used & mask == 0
# -- tracking the best total popcount reached.
#
# Time O(2^n) worst case   Space O(n) recursion
def max_captured_chars(words: List[str]) -> int:
    masks = []
    for w in words:
        m = 0
        for ch in w:
            m |= 1 << (ord(ch) - ord("a"))
        masks.append(m)

    best = 0

    def dfs(idx: int, used: int, count: int) -> None:
        nonlocal best
        best = max(best, count)
        for k in range(idx, len(words)):
            if used & masks[k] == 0:            # no shared letters
                dfs(k + 1, used | masks[k], count + bin(masks[k]).count("1"))

    dfs(0, 0, 0)
    return best


# ---------------------------------------------------------------------------
# Q27. Merge Two Sorted Interval Lists (LeetCode 56 variant)
# ---------------------------------------------------------------------------
# A and B are each sorted-by-start and internally non-overlapping. Merge into
# one sorted list with overlapping (or touching) intervals coalesced.
#
# Idea: two-pointer merge by start into one start-sorted sequence, then a single
# sweep that extends the last kept interval when the next starts at or before its
# end.
#
# Time O(n + m)   Space O(n + m)
def merge_two_interval_lists(a: List[List[int]],
                             b: List[List[int]]) -> List[List[int]]:
    ordered = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i][0] <= b[j][0]:
            ordered.append(a[i])
            i += 1
        else:
            ordered.append(b[j])
            j += 1
    ordered.extend(a[i:])
    ordered.extend(b[j:])

    merged: List[List[int]] = []
    for start, end in ordered:
        if merged and start <= merged[-1][1]:   # overlaps/touches -> extend
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged


# ---------------------------------------------------------------------------
# Q29. Banking System (CodeSignal-style 4-level assessment)
# ---------------------------------------------------------------------------
# A banking system processing timestamped account operations. Timestamps are
# strictly increasing across calls; get_balance may query the past (time_at).
# Built in four progressively harder levels.
#
# Level 1 - accounts & transfers:
#     create_account(timestamp, account_id)      -> bool (False if it exists)
#     deposit(timestamp, account_id, amount)     -> new balance, or None
#     transfer(timestamp, src, dst, amount)      -> src balance, or None
#         (None if either account is missing, src == dst, or funds too low)
#
# Level 2 - spending analytics:
#     top_spenders(timestamp, n)                 -> ["id(total)", ...] by total
#         OUTGOING amount desc, ties by id asc (all active accounts, top n)
#
# Level 3 - scheduled payments & cashback:
#     pay(timestamp, account_id, amount)         -> "paymentN", or None
#         withdraws amount; schedules a 2% (floored) cashback refunded 24h
#         (86_400_000 ms) later. Counts as outgoing spend; the refund does not.
#     get_payment_status(timestamp, account_id, payment_id)
#         -> "IN_PROGRESS" / "CASHBACK_RECEIVED", or None if invalid / not owned
#
# Level 4 - merging & historical balance:
#     merge_accounts(timestamp, id1, id2)        -> bool
#         fold id2 into id1 (balances, outgoing totals, pending cashbacks all
#         combine); id2 is absorbed. id2's history stays queryable for times
#         before the merge.
#     get_balance(timestamp, account_id, time_at) -> balance at time_at, or None
#
# Design: cashbacks are applied LAZILY -- before every operation, drain all
# scheduled refunds whose time is <= the current timestamp (a min-heap keyed by
# refund time). Each account keeps a running `outgoing` total and a time-sorted
# balance history so get_balance is a binary search.
class BankingSystem:
    CASHBACK_DELAY = 86_400_000        # 24 hours in milliseconds

    def __init__(self):
        # account_id -> {balance, outgoing, created_at, merged_at, history}
        self.accounts: dict = {}
        self.cashbacks: list = []       # min-heap of (refund_time, seq, payment_id)
        self.payments: dict = {}        # payment_id -> {account, amount, status}
        self._payment_seq = 0
        self._heap_seq = 0

    # ---- helpers ----------------------------------------------------------
    def _active(self, account_id):
        rec = self.accounts.get(account_id)
        return rec if rec and rec["merged_at"] is None else None

    def _record(self, rec: dict, when: int, balance: int) -> None:
        rec["balance"] = balance
        rec["history"].append((when, balance))

    def _process_cashbacks(self, timestamp: int) -> None:
        """Apply every scheduled cashback due at-or-before `timestamp`."""
        while self.cashbacks and self.cashbacks[0][0] <= timestamp:
            refund_time, _seq, pid = heapq.heappop(self.cashbacks)
            pay = self.payments[pid]
            rec = self._active(pay["account"])   # re-homed by merges if needed
            if rec is not None:
                self._record(rec, refund_time, rec["balance"] + pay["amount"])
            pay["status"] = "CASHBACK_RECEIVED"

    # ---- Level 1 ----------------------------------------------------------
    def create_account(self, timestamp: int, account_id: str) -> bool:
        self._process_cashbacks(timestamp)
        if account_id in self.accounts:
            return False
        self.accounts[account_id] = {
            "balance": 0, "outgoing": 0, "created_at": timestamp,
            "merged_at": None, "history": [(timestamp, 0)],
        }
        return True

    def deposit(self, timestamp: int, account_id: str, amount: int):
        self._process_cashbacks(timestamp)
        rec = self._active(account_id)
        if rec is None:
            return None
        self._record(rec, timestamp, rec["balance"] + amount)
        return rec["balance"]

    def transfer(self, timestamp: int, source_id: str, target_id: str,
                 amount: int):
        self._process_cashbacks(timestamp)
        src = self._active(source_id)
        dst = self._active(target_id)
        if src is None or dst is None or source_id == target_id:
            return None
        if src["balance"] < amount:
            return None
        self._record(src, timestamp, src["balance"] - amount)
        self._record(dst, timestamp, dst["balance"] + amount)
        src["outgoing"] += amount
        return src["balance"]

    # ---- Level 2 ----------------------------------------------------------
    def top_spenders(self, timestamp: int, n: int) -> List[str]:
        self._process_cashbacks(timestamp)
        ranked = sorted(
            ((aid, rec["outgoing"]) for aid, rec in self.accounts.items()
             if rec["merged_at"] is None),
            key=lambda pair: (-pair[1], pair[0]),
        )
        return [f"{aid}({total})" for aid, total in ranked[:n]]

    # ---- Level 3 ----------------------------------------------------------
    def pay(self, timestamp: int, account_id: str, amount: int):
        self._process_cashbacks(timestamp)
        rec = self._active(account_id)
        if rec is None or rec["balance"] < amount:
            return None
        self._record(rec, timestamp, rec["balance"] - amount)
        rec["outgoing"] += amount
        self._payment_seq += 1
        pid = f"payment{self._payment_seq}"
        cashback = amount * 2 // 100            # 2%, floored
        self.payments[pid] = {"account": account_id, "amount": cashback,
                              "status": "IN_PROGRESS"}
        heapq.heappush(self.cashbacks,
                       (timestamp + self.CASHBACK_DELAY, self._heap_seq, pid))
        self._heap_seq += 1
        return pid

    def get_payment_status(self, timestamp: int, account_id: str,
                           payment_id: str):
        self._process_cashbacks(timestamp)
        if self._active(account_id) is None:
            return None
        pay = self.payments.get(payment_id)
        if pay is None or pay["account"] != account_id:
            return None
        return pay["status"]

    # ---- Level 4 ----------------------------------------------------------
    def merge_accounts(self, timestamp: int, account_id1: str,
                       account_id2: str) -> bool:
        self._process_cashbacks(timestamp)
        a1 = self._active(account_id1)
        a2 = self._active(account_id2)
        if a1 is None or a2 is None or account_id1 == account_id2:
            return False
        # Re-home account2's pending cashbacks onto account1.
        for pay in self.payments.values():
            if pay["account"] == account_id2 and pay["status"] == "IN_PROGRESS":
                pay["account"] = account_id1
        a1["outgoing"] += a2["outgoing"]
        self._record(a1, timestamp, a1["balance"] + a2["balance"])
        a2["merged_at"] = timestamp        # absorbed; history kept for the past
        return True

    def get_balance(self, timestamp: int, account_id: str, time_at: int):
        self._process_cashbacks(timestamp)
        rec = self.accounts.get(account_id)
        if rec is None or time_at < rec["created_at"]:
            return None
        if rec["merged_at"] is not None and time_at >= rec["merged_at"]:
            return None                    # absorbed by then
        # Latest history entry with event time <= time_at.
        idx = bisect.bisect_right(rec["history"], (time_at, INF)) - 1
        return rec["history"][idx][1] if idx >= 0 else None


# ---------------------------------------------------------------------------
# Q30. Diameter of Binary Tree (LeetCode 543)
# ---------------------------------------------------------------------------
# Return the length (in edges) of the longest path between any two nodes. The
# path need not pass through the root.
#
# Idea: one post-order DFS returning each subtree's height in edges. The longest
# path THROUGH a node is left_height + right_height; track the max of that over
# all nodes while the same recursion computes heights.
#
# Time O(n)   Space O(height)
def diameter_of_binary_tree(root) -> int:
    best = 0

    def height(node) -> int:               # height in edges of this subtree
        nonlocal best
        if not node:
            return 0
        lh = height(node.left)
        rh = height(node.right)
        best = max(best, lh + rh)          # path through `node`
        return 1 + max(lh, rh)

    height(root)
    return best


# ---------------------------------------------------------------------------
# Q31. Palindromic Substrings (LeetCode 647)
# ---------------------------------------------------------------------------
# Count the palindromic substrings of s. Different positions count separately
# even when the substrings are identical.
#
# Idea (expand around center): each palindrome is centered on a character (odd
# length) or on a gap between two characters (even length) -- 2n-1 centers. From
# each center expand while the ends match, counting one palindrome per expansion.
#
# Time O(n^2)   Space O(1)
def count_palindromic_substrings(s: str) -> int:
    n = len(s)

    def expand(lo: int, hi: int) -> int:
        count = 0
        while lo >= 0 and hi < n and s[lo] == s[hi]:
            count += 1
            lo -= 1
            hi += 1
        return count

    total = 0
    for i in range(n):
        total += expand(i, i)              # odd-length centers
        total += expand(i, i + 1)          # even-length centers
    return total


# ---------------------------------------------------------------------------
# Q33. Remove Duplicates from Sorted Array (LeetCode 26)
# ---------------------------------------------------------------------------
# Remove duplicates in place from a non-decreasing array so each value appears
# once, preserving order; return k, the number of uniques (nums[:k] holds them).
#
# Idea (two pointers): `slow` is the write index of the last unique kept; `fast`
# scans ahead. Because the array is sorted, a value differs from nums[slow] iff
# it is new, so we bump `slow` and write it there.
#
# Time O(n)   Space O(1)
def remove_duplicates(nums: List[int]) -> int:
    if not nums:
        return 0
    slow = 0                               # nums[:slow + 1] are the uniques so far
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
    return slow + 1


# ---------------------------------------------------------------------------
# Q34. Longest Increasing Path in a Matrix (LeetCode 329)
# ---------------------------------------------------------------------------
# Return the length of the longest strictly increasing path, moving only up /
# down / left / right.
#
# Idea (DFS + memo): best(r, c) = longest increasing path STARTING at (r, c).
# Since moves only go to strictly greater values, the move graph is a DAG, so a
# cached best(r, c) never changes -- memoize it. Answer is the max over cells.
#
# Time O(m * n)   Space O(m * n)
def longest_increasing_path(matrix: List[List[int]]) -> int:
    if not matrix or not matrix[0]:
        return 0
    rows, cols = len(matrix), len(matrix[0])
    memo: dict = {}

    def best(r: int, c: int) -> int:
        if (r, c) in memo:
            return memo[(r, c)]
        longest = 1                        # the cell on its own
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols \
                    and matrix[nr][nc] > matrix[r][c]:
                longest = max(longest, 1 + best(nr, nc))
        memo[(r, c)] = longest
        return longest

    return max(best(r, c) for r in range(rows) for c in range(cols))


# ---------------------------------------------------------------------------
# Q35. Valid Number (LeetCode 65)
# ---------------------------------------------------------------------------
# Return whether s is a valid number: [sign] (integer | decimal) [exponent].
#
# Idea: one left-to-right scan with two helpers -- skip an optional sign, and
# skip a run of digits (reporting whether any were seen). Parse the mantissa
# ([sign] digits? [. digits?], needing a digit somewhere), then an optional
# e/E followed by a signed integer. Valid iff the scan consumes the whole string.
#
# Time O(n)   Space O(1)
def is_number(s: str) -> bool:
    n = len(s)
    if n == 0:
        return False

    def skip_sign(j: int) -> int:
        return j + 1 if j < n and s[j] in "+-" else j

    def skip_digits(j: int) -> tuple:
        start = j
        while j < n and s[j].isdigit():
            j += 1
        return j, j > start                # (new index, saw >= 1 digit)

    i = skip_sign(0)
    i, int_digits = skip_digits(i)
    frac_digits = False
    if i < n and s[i] == ".":
        i += 1
        i, frac_digits = skip_digits(i)
    if not (int_digits or frac_digits):    # e.g. ".", "+", "e"
        return False
    if i < n and s[i] in "eE":             # optional exponent
        i = skip_sign(i + 1)
        i, exp_digits = skip_digits(i)
        if not exp_digits:
            return False
    return i == n


# ---------------------------------------------------------------------------
# Q36. Best Time to Buy and Sell Stock (LeetCode 121)
# ---------------------------------------------------------------------------
# One buy then a later sell; return the max profit (0 if none is profitable).
#
# Idea: sweep once, tracking the cheapest price seen so far; the best sale today
# is price - min_so_far. Keep the running maximum of that.
#
# Time O(n)   Space O(1)
def max_profit(prices: List[int]) -> int:
    min_price = float("inf")
    best = 0
    for p in prices:
        if p < min_price:                  # cheaper day to have bought
            min_price = p
        elif p - min_price > best:         # better day to sell
            best = p - min_price
    return best


# ---------------------------------------------------------------------------
# Q37. Collapse Adjacent Duplicate Letters (open-ended; cf. LeetCode 1047)
# ---------------------------------------------------------------------------
# Repeatedly remove a group of adjacent identical letters. Removing a group can
# merge its former neighbors into a new group, so the order matters and different
# orders give different results -- the interviewer accepts either. Two semantics:
#
#   collapse_pairs: cancel two equal adjacent letters (confluent -> unique).
#                   "abbaa" -> "a".  Time O(n), space O(n).
#   collapse_runs:  delete the leftmost maximal run of length >= 2, restarting so
#                   cascading merges are caught.  "abbaa" -> "".  Time O(n^2).
def collapse_pairs(s: str) -> str:
    stack: List[str] = []
    for ch in s:
        if stack and stack[-1] == ch:      # meets its twin -> both vanish
            stack.pop()
        else:
            stack.append(ch)
    return "".join(stack)


def collapse_runs(s: str) -> str:
    chars = list(s)
    changed = True
    while changed:
        changed = False
        i = 0
        while i < len(chars):
            j = i
            while j < len(chars) and chars[j] == chars[i]:
                j += 1
            if j - i >= 2:                 # a whole run of length >= 2
                del chars[i:j]
                changed = True
                break                      # restart -- a merge may have formed
            i = j
    return "".join(chars)


# ---------------------------------------------------------------------------
# Q40. Keypad Combinations with Grouped Presses (LeetCode 17 variant)
# ---------------------------------------------------------------------------
# Each digit maps to letters (1->ABC ... 7->ST, 9->XY, 0->Z). A run of k
# consecutive identical digits d may be split into groups; a group of size k
# picks the k-th letter of d's mapping, with k <= len(mapping[d]). Return every
# string formed by a valid partition (any order).
#
# Idea (backtracking): at index i, open a group on digit d = s[i] and extend it
# while the next char stays d and the group size <= letters available; a size-k
# group emits mapping[d][k-1]. Recurse past the group; record at the end. Groups
# can only span identical consecutive digits, so runs are handled naturally.
#
# Time O(#combinations * n)   Space O(n) recursion (+ output)
def keypad_combinations(digits: str) -> List[str]:
    mapping = {
        "1": "ABC", "2": "DEF", "3": "GHI", "4": "JKL", "5": "MNO",
        "6": "PQR", "7": "ST", "8": "UVW", "9": "XY", "0": "Z",
    }
    n = len(digits)
    results: List[str] = []
    path: List[str] = []

    def backtrack(i: int) -> None:
        if i == n:
            results.append("".join(path))
            return
        d = digits[i]
        letters = mapping[d]
        k = 1
        # extend the group while digits stay identical and size <= available
        while i + k <= n and digits[i + k - 1] == d and k <= len(letters):
            path.append(letters[k - 1])        # a size-k group -> the k-th letter
            backtrack(i + k)
            path.pop()
            k += 1

    backtrack(0)
    return results


# ---------------------------------------------------------------------------
# Q42. Diagonal Traverse (LeetCode 498)
# ---------------------------------------------------------------------------
# Return all elements of an m x n matrix in zig-zag diagonal order.
#
# Idea: cells on one diagonal share r + c = d. Walk d from 0..m+n-2; even
# diagonals go up-right (row decreasing), odd diagonals go down-left, which gives
# the alternating zig-zag. Start each diagonal at its clamped endpoint.
#
# Time O(m * n)   Space O(1) extra (excluding output)
def find_diagonal_order(mat: List[List[int]]) -> List[int]:
    if not mat or not mat[0]:
        return []
    m, n = len(mat), len(mat[0])
    result: List[int] = []
    for d in range(m + n - 1):
        if d % 2 == 0:                     # going up-right
            r = min(d, m - 1)
            c = d - r
            while r >= 0 and c < n:
                result.append(mat[r][c])
                r -= 1
                c += 1
        else:                              # going down-left
            c = min(d, n - 1)
            r = d - c
            while c >= 0 and r < m:
                result.append(mat[r][c])
                r += 1
                c -= 1
    return result


# ---------------------------------------------------------------------------
# Q43. Sum Root to Leaf Numbers (LeetCode 129)
# ---------------------------------------------------------------------------
# Each root-to-leaf path spells a number (concatenated digits); return their sum.
#
# Idea: DFS carrying the number built so far; at each node do cur = cur*10 + val,
# and at a leaf contribute cur. (Reuses TreeNode from Q8.)
#
# Time O(n)   Space O(height)
def sum_numbers(root) -> int:
    def dfs(node, cur: int) -> int:
        if node is None:
            return 0
        cur = cur * 10 + node.val
        if node.left is None and node.right is None:     # leaf
            return cur
        return dfs(node.left, cur) + dfs(node.right, cur)

    return dfs(root, 0)


# ---------------------------------------------------------------------------
# Q44. Nested List Weight Sum (LeetCode 339)
# ---------------------------------------------------------------------------
# Each integer has a weight equal to its depth (top level = 1). Return the sum
# of every integer times its depth. Here a nested list is modeled as a Python
# list holding ints and/or further lists.
#
# Idea: DFS; recurse into sublists with depth + 1, add int * depth for integers.
#
# Time O(total elements)   Space O(max depth)
def depth_sum(nested: list) -> int:
    def dfs(items: list, depth: int) -> int:
        total = 0
        for x in items:
            if isinstance(x, list):
                total += dfs(x, depth + 1)
            else:
                total += x * depth
        return total

    return dfs(nested, 1)


# ---------------------------------------------------------------------------
# Q45. Lowest Common Ancestor of a Binary Tree III (LeetCode 1650)
# ---------------------------------------------------------------------------
# Nodes carry a parent pointer and you're given only the two nodes (no root).
# Find their lowest common ancestor.
#
# Idea (two pointers, like linked-list intersection): walk a and b up via parent;
# when one hits the top (None), redirect it to the OTHER start node. After each
# has walked its own path + the other's prefix, they meet at the LCA (both have
# travelled the same total distance).
#
# Time O(h1 + h2)   Space O(1)
class ParentTreeNode:
    def __init__(self, val: int = 0):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


def lowest_common_ancestor(p, q):
    a, b = p, q
    while a is not b:
        a = a.parent if a else q
        b = b.parent if b else p
    return a


def _run_self_tests() -> None:
    # Q1
    assert is_alien_sorted(["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz")
    assert not is_alien_sorted(["word", "world", "row"],
                               "worldabcefghijkmnpqstuvxyz")
    assert not is_alien_sorted(["apple", "app"],
                               "abcdefghijklmnopqrstuvwxyz")  # prefix case

    # Q2
    assert valid_palindrome("aba")
    assert valid_palindrome("abca")      # delete 'c' (or 'b')
    assert not valid_palindrome("abc")

    # Q3
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

    # Q14
    assert best_ratio_index([4, 2, 7], [2, 1, 5]) == 0   # 2.0 == 2.0 -> smaller
    assert best_ratio_index([1, 2, 3], [3, 2, 1]) == 2   # 1/3, 1, 3
    assert best_ratio_index([5], [10]) == 0
    assert best_ratio_index([3, 3], [1, 1]) == 0         # exact tie -> index 0

    # Q15
    assert round_trip_time([1, 3, 5, 7], [2, 4, 6, 8], 2) == 4
    assert round_trip_time([1, 3, 5, 7], [2, 4, 6, 8], 1) == 2
    assert round_trip_time([10, 20], [15, 25], 1, start=0) == 15
    # "not earlier than" is >=, so a leg may leave at the exact current time.
    assert round_trip_time([0, 5], [0, 5], 1, start=0) == 0

    # Q16
    assert apply_matrix_commands([[1, 2], [3, 4]], [("rotate",)]) == \
        [[3, 1], [4, 2]]
    assert apply_matrix_commands([[1, 2], [3, 4]],
                                 [("rotate",), ("reverse_row", 0)]) == \
        [[1, 3], [4, 2]]
    assert apply_matrix_commands([[1, 2], [3, 4]], [("swap_row", 0, 1)]) == \
        [[3, 4], [1, 2]]
    assert apply_matrix_commands([[1, 2], [3, 4]], [("swap_col", 0, 1)]) == \
        [[2, 1], [4, 3]]
    assert apply_matrix_commands([[1, 2, 3]], [("reverse_row", 0)]) == \
        [[3, 2, 1]]
    assert apply_matrix_commands([[1], [2], [3]], [("reverse_col", 0)]) == \
        [[3], [2], [1]]

    # Q17
    assert count_access_pairs(["a", "b", "ab", "c"], "ab") == 1
    assert count_access_pairs(["a", "a", "aa"], "aa") == 4   # i == j allowed
    assert count_access_pairs(["ab", "cd", "abcd"], "abcd") == 1
    assert count_access_pairs(["x", "y"], "ab") == 0

    # Q18
    assert merge_three_sorted([1, 2, 5], [2, 3], [3, 6]) == [1, 2, 3, 5, 6]
    assert merge_three_sorted([1, 1, 2], [2, 2], []) == [1, 2]  # within + across
    assert merge_three_sorted([], [], []) == []
    assert merge_three_sorted([1, 4], [2, 4], [4, 5]) == [1, 2, 4, 5]

    # Q19
    assert simplify_path("/home/") == "/home"
    assert simplify_path("/../") == "/"                   # can't go above root
    assert simplify_path("/home//foo/") == "/home/foo"   # collapse slashes
    assert simplify_path("/a/./b/../../c/") == "/c"
    assert simplify_path("/") == "/"

    # Q20   tree:      3
    #                /   \
    #               9    20
    #                    / \
    #                   15  7
    vt = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert vertical_order(vt) == [[9], [3, 15], [20], [7]]
    assert vertical_order(None) == []
    #       1        columns: [2] | [1, 4, 5] | [3]
    #      / \       4 and 5 share row+col -> left to right.
    #     2   3
    #      \  /
    #      4 5
    vt2 = TreeNode(1, TreeNode(2, None, TreeNode(4)),
                   TreeNode(3, TreeNode(5), None))
    assert vertical_order(vt2) == [[2], [1, 4, 5], [3]]

    # Q21
    assert find_local_min([3, 2, 1, 2, 3]) == 2
    assert find_local_min([1, 2, 3]) == 0        # boundary: +inf on the left
    assert find_local_min([3, 2, 1]) == 2        # boundary: +inf on the right
    assert find_local_min([5]) == 0
    # Whatever index is returned must really be a local minimum.
    for nums in ([3, 2, 1, 2, 3], [1, 2, 3], [3, 2, 1], [5], [2, 1],
                 [5, 4, 3, 4, 1, 2]):
        i = find_local_min(nums)
        left = nums[i - 1] if i - 1 >= 0 else INF
        right = nums[i + 1] if i + 1 < len(nums) else INF
        assert left > nums[i] < right
    assert find_local_min_linear([3, 2, 1, 2, 3]) == 2

    # Q22
    random.seed(0)
    c = RandomizedContainer()
    for v in [10, 20, 30, 40, 50]:
        c.insert(v)
    assert len(c) == 5
    drained = sorted(c.pop_random() for _ in range(5))
    assert drained == [10, 20, 30, 40, 50]      # every element comes out once
    assert len(c) == 0
    try:
        c.pop_random()
        raise AssertionError("expected IndexError")
    except IndexError:
        pass

    # Q23
    assert count_distinct([1, 1, 2, 2, 2, 3]) == 3
    assert count_distinct([]) == 0
    assert count_distinct([5]) == 1
    assert count_distinct([1, 1, 1]) == 1
    assert count_distinct([1, 2, 3, 4]) == 4
    for a in ([1, 1, 2, 2, 2, 3], [], [5], [1, 1, 1], [1, 2, 3, 4],
              [0, 0, 0, 7, 7, 9, 9, 9, 9]):
        assert count_distinct(a) == count_distinct_linear(a)

    # Q25
    assert plan_round_trip([4, 1, 3], [5, 2, 4]) == (1, 2, 5)
    # All pairs tie at cost 4 -> earliest departure (0), then latest return (2).
    assert plan_round_trip([1, 1, 5], [5, 3, 3]) == (0, 2, 4)
    # Conflict: (0,1) and (2,3) both cost 10 -> earliest departure wins.
    assert plan_round_trip([6, 100, 3, 100], [100, 4, 100, 7]) == (0, 1, 10)
    assert plan_round_trip([2, 5], [9, 1]) == (0, 1, 3)
    assert plan_round_trip([3], [3]) is None          # no valid i < j

    # Q26
    assert max_captured_chars(["ab", "cd", "abc"]) == 4    # "ab" + "cd"
    assert max_captured_chars(["un", "iq", "ue"]) == 4     # "un" + "iq"
    assert max_captured_chars(["cha", "r", "act", "ers"]) == 6
    assert max_captured_chars(["aa", "bb"]) == 2           # distinct letters
    assert max_captured_chars([]) == 0
    assert max_captured_chars(["abc"]) == 3

    # Q27
    assert merge_two_interval_lists([[1, 3], [5, 7]], [[2, 4], [6, 8]]) == \
        [[1, 4], [5, 8]]
    assert merge_two_interval_lists([[1, 2], [3, 4]], [[5, 6]]) == \
        [[1, 2], [3, 4], [5, 6]]
    assert merge_two_interval_lists([], [[1, 5]]) == [[1, 5]]
    assert merge_two_interval_lists([[1, 10]], [[2, 3], [4, 5]]) == [[1, 10]]
    assert merge_two_interval_lists([[1, 3]], [[3, 5]]) == [[1, 5]]  # touching

    # Q29 - Level 1 & 2
    bank = BankingSystem()
    assert bank.create_account(1, "a") is True
    assert bank.create_account(2, "a") is False        # already exists
    assert bank.deposit(3, "a", 100) == 100
    assert bank.deposit(4, "b", 10) is None            # no account b
    assert bank.create_account(5, "b") is True
    assert bank.deposit(6, "b", 50) == 50
    assert bank.transfer(7, "a", "b", 30) == 70        # a:70  b:80
    assert bank.transfer(8, "a", "c", 5) is None       # target missing
    assert bank.transfer(9, "a", "a", 5) is None       # same account
    assert bank.transfer(10, "a", "b", 1000) is None   # insufficient funds
    assert bank.top_spenders(11, 5) == ["a(30)", "b(0)"]

    # Q29 - Level 3 (payments & cashback); use big amounts for nonzero cashback
    b3 = BankingSystem()
    b3.create_account(1, "a")
    b3.deposit(2, "a", 1000)
    pid = b3.pay(3, "a", 300)                           # cashback = 300*2//100 = 6
    assert pid == "payment1"
    assert b3.pay(4, "a", 100000) is None              # underfunded
    assert b3.get_payment_status(5, "a", pid) == "IN_PROGRESS"
    assert b3.get_payment_status(5, "x", pid) is None  # account missing
    assert b3.get_payment_status(5, "a", "payment9") is None
    assert b3.top_spenders(6, 1) == ["a(300)"]         # pay counts as outgoing
    # Cashback lands lazily once an op occurs at-or-after the refund time.
    refund_t = 3 + BankingSystem.CASHBACK_DELAY
    assert b3.get_payment_status(refund_t + 1, "a", pid) == "CASHBACK_RECEIVED"
    assert b3.get_balance(refund_t + 2, "a", refund_t + 1) == 706  # 700 + 6

    # Q29 - Level 4 (merge & historical balance)
    b4 = BankingSystem()
    b4.create_account(1, "x")
    b4.deposit(2, "x", 100)
    b4.create_account(3, "y")
    b4.deposit(4, "y", 50)
    b4.transfer(5, "x", "y", 20)                        # x:80  y:70 ; x out 20
    assert b4.get_balance(6, "x", 2) == 100             # right after deposit
    assert b4.get_balance(6, "x", 1) == 0               # at creation
    assert b4.get_balance(6, "x", 0) is None            # before it existed
    assert b4.get_balance(6, "z", 1) is None            # unknown account
    assert b4.merge_accounts(7, "x", "y") is True       # x:150
    assert b4.merge_accounts(8, "x", "nope") is False
    assert b4.merge_accounts(9, "x", "x") is False
    assert b4.get_balance(10, "x", 7) == 150            # combined balance
    assert b4.get_balance(10, "y", 4) == 50            # y's history pre-merge
    assert b4.get_balance(10, "y", 7) is None           # absorbed by t=7
    assert b4.top_spenders(11, 5) == ["x(20)"]          # y no longer active

    # Q29 - Level 4: a merged account's pending cashback follows it
    b5 = BankingSystem()
    b5.create_account(1, "a")
    b5.deposit(2, "a", 1000)
    b5.create_account(3, "b")
    b5.deposit(4, "b", 500)
    p = b5.pay(5, "b", 100)                             # b:400 ; cashback = 2
    assert b5.merge_accounts(6, "a", "b") is True       # a:1400 (1000+400)
    rt = 5 + BankingSystem.CASHBACK_DELAY
    assert b5.get_payment_status(rt + 1, "a", p) == "CASHBACK_RECEIVED"
    assert b5.get_payment_status(rt + 2, "b", p) is None  # b absorbed
    assert b5.get_balance(rt + 3, "a", rt + 1) == 1402   # 1400 + 2 cashback
    assert b5.top_spenders(rt + 4, 5) == ["a(100)"]      # b's outgoing folded in

    # Q30   tree:      1
    #                /   \
    #               2     3
    #              / \
    #             4   5
    dt = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    assert diameter_of_binary_tree(dt) == 3      # 4 -> 2 -> 1 -> 3
    assert diameter_of_binary_tree(None) == 0
    assert diameter_of_binary_tree(TreeNode(1)) == 0            # single node
    assert diameter_of_binary_tree(TreeNode(1, TreeNode(2))) == 1
    # Longest path entirely within the left subtree (not through the root).
    skew = TreeNode(1,
                    TreeNode(2, TreeNode(3, TreeNode(4)), TreeNode(3, None,
                             TreeNode(4))),
                    None)
    assert diameter_of_binary_tree(skew) == 4

    # Q31
    assert count_palindromic_substrings("abc") == 3
    assert count_palindromic_substrings("aaa") == 6
    assert count_palindromic_substrings("aba") == 4       # a, b, a, aba
    assert count_palindromic_substrings("") == 0
    assert count_palindromic_substrings("a") == 1

    # Q33
    a = [1, 1, 2]
    assert remove_duplicates(a) == 2 and a[:2] == [1, 2]
    b = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    assert remove_duplicates(b) == 5 and b[:5] == [0, 1, 2, 3, 4]
    assert remove_duplicates([]) == 0
    assert remove_duplicates([7]) == 1

    # Q34
    assert longest_increasing_path([[9, 9, 4], [6, 6, 8], [2, 1, 1]]) == 4
    assert longest_increasing_path([[3, 4, 5], [3, 2, 6], [2, 2, 1]]) == 4
    assert longest_increasing_path([[1]]) == 1
    assert longest_increasing_path([]) == 0

    # Q35
    for ok in ("0", "0.1", "2.", ".8", "-90E3", "3e+7", "+6e-1", "53.5e93"):
        assert is_number(ok), ok
    for bad in ("", ".", "e", "1e", "e3", "99e2.5", "--6", "-+3", "+", "abc"):
        assert not is_number(bad), bad

    # Q36
    assert max_profit([7, 1, 5, 3, 6, 4]) == 5
    assert max_profit([7, 6, 4, 3, 1]) == 0
    assert max_profit([]) == 0
    assert max_profit([3]) == 0

    # Q37
    assert collapse_pairs("abbaa") == "a"       # pairwise -> unique result
    assert collapse_runs("abbaa") == ""         # whole-run -> full cancellation
    assert collapse_pairs("abbaca") == "ca" == collapse_runs("abbaca")
    assert collapse_pairs("") == "" == collapse_runs("")

    # Q40
    assert sorted(keypad_combinations("7772")) == ["SSSD", "STD", "TSD"]
    assert sorted(keypad_combinations("2222")) == \
        ["DDDD", "DDE", "DED", "DF", "EDD", "EE", "FD"]
    assert keypad_combinations("123456") == ["ADGJMP"]
    assert keypad_combinations("1") == ["A"]
    assert sorted(keypad_combinations("77")) == ["SS", "T"]

    # Q42
    assert find_diagonal_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == \
        [1, 2, 4, 7, 5, 3, 6, 8, 9]
    assert find_diagonal_order([[1, 2], [3, 4]]) == [1, 2, 3, 4]
    assert find_diagonal_order([]) == []

    # Q43
    assert sum_numbers(TreeNode(1, TreeNode(2), TreeNode(3))) == 25   # 12 + 13
    # 495 + 491 + 40 = 1026
    t129 = TreeNode(4, TreeNode(9, TreeNode(5), TreeNode(1)), TreeNode(0))
    assert sum_numbers(t129) == 1026
    assert sum_numbers(None) == 0

    # Q44
    assert depth_sum([[1, 1], 2, [1, 1]]) == 10          # 2*(1+1) + 1*2 + 2*(1+1)
    assert depth_sum([1, [4, [6]]]) == 27                # 1 + 4*2 + 6*3
    assert depth_sum([]) == 0

    # Q45
    nodes = {v: ParentTreeNode(v) for v in (3, 5, 1, 6, 2, 0, 8, 7, 4)}

    def _link(par, left, right):
        nodes[par].left = nodes.get(left)
        nodes[par].right = nodes.get(right)
        if left is not None:
            nodes[left].parent = nodes[par]
        if right is not None:
            nodes[right].parent = nodes[par]

    _link(3, 5, 1)
    _link(5, 6, 2)
    _link(1, 0, 8)
    _link(2, 7, 4)
    assert lowest_common_ancestor(nodes[5], nodes[1]) is nodes[3]
    assert lowest_common_ancestor(nodes[5], nodes[4]) is nodes[5]   # 5 is an ancestor
    assert lowest_common_ancestor(nodes[6], nodes[4]) is nodes[5]
    assert lowest_common_ancestor(nodes[7], nodes[8]) is nodes[3]

    print("All self-tests passed.")


if __name__ == "__main__":
    # With CLI args -> run the vmstat monitor (Q4). No args -> self-tests.
    # Q4 usage, e.g.
    #   vmstat 1 | python3 solutions.py --column 3 --threshold 1000000 --max-hits 3
    # (column 3 is 'free' in the sample header)
    if len(sys.argv) > 1:
        sys.exit(main())
    else:
        _run_self_tests()
