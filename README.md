# Interview Questions

Each entry has a **problem statement**, an **example** where helpful,
**notes/constraints**, and a suggested **approach**. Reference solutions live
in [`solutions.py`](./solutions.py).

## Contents

| # | Question | Reference |
|---|----------|-----------|
| 1 | [Verifying an Alien Dictionary](#1-verifying-an-alien-dictionary) | LeetCode 953 |
| 2 | [Valid Palindrome II](#2-valid-palindrome-ii) | LeetCode 680 |
| 3 | [Evaluate an Arithmetic Expression](#3-evaluate-an-arithmetic-expression) | — |
| 4 | [Threshold Monitor for vmstat-style Input](#4-threshold-monitor-for-vmstat-style-input) | — |
| 5 | [Shortest Unique Prefix](#5-shortest-unique-prefix) | — |
| 6 | [Minimum Add to Make Parentheses Valid](#6-minimum-add-to-make-parentheses-valid) | LeetCode 921 |
| 7 | [Meeting Rooms II](#7-meeting-rooms-ii) | LeetCode 253 |
| 8 | [Binary Tree Right Side View](#8-binary-tree-right-side-view) | LeetCode 199 |
| 9 | [Jump Game II](#9-jump-game-ii) | LeetCode 45 |
| 10 | [In-Memory Database](#10-in-memory-database) | multi-level |
| 11 | [Find the Container String](#11-find-the-container-string) | — |
| 12 | [Kth Largest Element in an Array](#12-kth-largest-element-in-an-array) | LeetCode 215 |
| 13 | [Subarray Sum Equals K](#13-subarray-sum-equals-k) | LeetCode 560 |
| 14 | [Best Rating-to-Price Index](#14-best-rating-to-price-index) | — |
| 15 | [Complete Round-Trip Missions](#15-complete-round-trip-missions) | — |
| 16 | [Apply Matrix Commands](#16-apply-matrix-commands) | — |
| 17 | [Count Access-Code Pairs](#17-count-access-code-pairs) | — |
| 18 | [Merge Three Sorted Arrays](#18-merge-three-sorted-arrays) | LeetCode 88 (variant) |
| 19 | [Simplify Path](#19-simplify-path) | LeetCode 71 |
| 20 | [Binary Tree Vertical Order Traversal](#20-binary-tree-vertical-order-traversal) | LeetCode 314 |
| 21 | [Find a Local Minimum](#21-find-a-local-minimum) | LeetCode 162 (variant) |
| 22 | [Randomized Container (Insert / Pop Random)](#22-randomized-container-insert--pop-random) | LeetCode 380 (variant) |
| 23 | [Count Distinct Values in a Sorted Array](#23-count-distinct-values-in-a-sorted-array) | — |
| 24 | [System Design: Design Twitter](#24-system-design-design-twitter) | System design |
| 25 | [Plan Round Trip With Minimum Flight Cost](#25-plan-round-trip-with-minimum-flight-cost) | — |
| 26 | [Maximum Characters From Non-Overlapping Words](#26-maximum-characters-from-non-overlapping-words) | AI-enabled |
| 27 | [Merge Two Sorted Interval Lists](#27-merge-two-sorted-interval-lists) | LeetCode 56 (variant) |
| 28 | [System Design: Trending Hashtags](#28-system-design-trending-hashtags) | System design |

---

## 1. Verifying an Alien Dictionary

> **LeetCode 953**

**Problem.** You are given a list of words `words` and a string `order` that
defines the alphabet of an alien language (a permutation of the letters).
Return `true` if `words` is sorted in lexicographic order according to `order`.

**Example**

```text
words = ["hello", "leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"  ->  true
```

**Notes**

- Watch the prefix case: if a word is a prefix of the previous (longer) word,
  e.g. `["apple", "app"]`, the list is **not** sorted.

**Approach**

1. Map each letter in `order` to its rank so comparisons are `O(1)`.
2. Compare each adjacent pair of words; at the first differing character,
   compare their ranks.
3. If no character differs, the shorter word must come first.

---

## 2. Valid Palindrome II

> **LeetCode 680**

**Problem.** Given a string `s`, return `true` if it can be turned into a
palindrome by deleting **at most one** character.

**Example**

```text
"abca"  ->  true   (delete 'c', leaving "aba")
```

**Approach**

1. Use two pointers from both ends moving inward, comparing characters.
2. On the first mismatch, try skipping the left character **or** the right
   character and check whether the remaining substring is a palindrome.
3. Return `true` if either option yields a palindrome.

---

## 3. Evaluate an Arithmetic Expression

**Problem.** Write a function that evaluates a basic arithmetic expression
given as a string and returns the result. The expression uses `+`, `-`, `*`,
`/` with standard operator precedence and contains **no parentheses**. The
input may be invalid — handle that case (e.g. raise an error).

**Example**

```text
"10/2+1*3+5"  ->  13
```

**Notes**

- `*` and `/` bind tighter than `+` and `-`.
- Invalid inputs include things like `"10++2"` or a trailing operator.

**Approach**

1. Scan left to right, building each number and tracking the pending operator
   (default `+`).
2. For `+`/`-`, push the (signed) number onto a stack; for `*`/`/`, pop the top
   and combine immediately so precedence is respected.
3. The answer is the sum of the stack.

---

## 4. Threshold Monitor for vmstat-style Input

**Problem.** Write a script that reads `vmstat`-style lines from stdin, for
example:

```text
procs -----------memory---------- ---swap-- -----io---- -system-- -------cpu-------
 r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st gu
 2  0 16777204 5630832  11664 31419024    9   26   245  1775 10371   11  4  1 94  1  0  0
```

For each data line, look at the value of the N-th whitespace-separated field.
Count how many times (cumulatively, across all lines) that value exceeds a
given threshold; once the count reaches `X`, print an error/warning.

**Requirements**

- Write the `main` function with argument parsing (column index, threshold,
  count) and reading from stdin.
- Skip header rows (lines whose target field is not numeric).

---

## 5. Shortest Unique Prefix

**Problem.** Given a list of words, for each word return the shortest prefix
that uniquely identifies it among all the words. Return the results in the
original input order.

**Example**

```text
["zebra", "dog", "duck", "dove"]  ->  ["z", "dog", "du", "dov"]
```

**Approach**

1. Insert every word into a trie; each node records how many words pass through
   it (i.e. share that prefix).
2. For each word, walk down its characters; the shortest unique prefix ends at
   the first node with a count of 1.

---

## 6. Minimum Add to Make Parentheses Valid

> **LeetCode 921**

**Problem.** Given a string `s` of only `(` and `)`, you may insert a `(` or
`)` at any position. Return the minimum number of insertions needed to make `s`
a valid (balanced) parenthesis string.

**Example**

```text
"())"     ->  1
"((("     ->  3
"()))(("  ->  4
```

**Approach**

1. Single pass tracking `open` = number of currently unmatched `(`.
2. On `(`, increment `open`. On `)`, if `open > 0` match it (decrement),
   otherwise you must insert a `(` (answer += 1).
3. After the pass, every remaining unmatched `(` needs a `)`: answer += `open`.

---

## 7. Meeting Rooms II

> **LeetCode 253**

**Problem.** Given a set of meeting intervals `intervals = [[start, end], ...]`,
return the minimum number of meeting rooms required so that no two meetings
overlap in the same room.

**Example**

```text
[[0, 30], [5, 10], [15, 20]]  ->  2
```

**Notes**

- Meetings that only touch at endpoints (e.g. `[1,5]` and `[5,10]`) do not
  overlap.

**Approach**

1. Sort meetings by start time; keep a min-heap of end times of ongoing
   meetings.
2. For each meeting, if the earliest-ending room is free (its end `<=` this
   start), reuse it (pop); then push this meeting's end.
3. The maximum heap size during the scan is the answer.

---

## 8. Binary Tree Right Side View

> **LeetCode 199**

**Problem.** Given a binary tree, imagine standing on its right side. Return
the values of the nodes visible from top to bottom.

**Example**

```text
    1            ->  [1, 3, 4]
   / \
  2   3
   \   \
    5   4
```

**Approach**

1. BFS level order: the last node visited on each level is the one visible from
   the right.
2. Or DFS visiting the right child first, recording the first node reached at
   each depth.

---

## 9. Jump Game II

> **LeetCode 45**

**Problem.** Given a non-negative integer array `nums`, you start at index 0.
`nums[i]` is the maximum number of steps you can jump forward from index `i`.
Return the minimum number of jumps to reach the last index (reaching it is
guaranteed).

**Example**

```text
[2, 3, 1, 1, 4]  ->  2   (index 0 -> 1 -> 4)
```

**Approach (greedy)**

1. Track `farthest` (max index reachable so far) and `cur_end` (the reach of
   the current jump).
2. While scanning, update `farthest = max(farthest, i + nums[i])`.
3. When `i` reaches `cur_end`, take another jump: increment the count and set
   `cur_end = farthest`.

---

## 10. In-Memory Database

> **Multi-level assessment**

**Problem.** Build a key-value store where each key holds a record (a set of
`field -> value` pairs). The assessment has four progressively harder levels;
you must pass all tests in a level before the next level's problem is revealed.

**Level 1 — basic CRUD on fields within a record**

```text
set(key, field, value)
get(key, field)
delete(key, field)
```

**Level 2 — scanning a record's fields**

```text
scan(key)                     -> fields sorted by name
scan_by_prefix(key, prefix)   -> only fields starting with prefix
```

**Level 3 — TTL.** Writes carry a timestamp and a time-to-live; a field is
alive at time `t` iff `created_at <= t < created_at + ttl`. Add timestamped
variants:

```text
set_at, get_at, delete_at, scan_at, scan_by_prefix_at
```

**Level 4 — backup & restore**

```text
backup(timestamp)                        -> snapshot live fields, storing
                                            REMAINING ttl
restore(timestamp, timestamp_to_restore) -> restore the most recent backup
                                            taken at-or-before
                                            timestamp_to_restore, re-anchoring
                                            each field's expiry to the current
                                            timestamp
```

**Interview note**

- 90 minutes, 4 levels, gated (all tests in a level must pass to advance).
- The practice test mirrors this format closely.
- It is fine not to finish: partial progress (e.g. failing a few Level 3 cases)
  can still advance to the full loop. Outcome is pass/fail; a fail means a
  1-year freeze.

---

## 11. Find the Container String

**Problem.** Given a list of strings, return the one string that contains every
other string in the list as a substring, or `None` if no such string exists.

**Example**

```text
["programming", "am", "pro"]  ->  "programming"
("am" is in progr[am]ming, "pro" is in [pro]gramming)
```

**Task.** A brute-force `O(n² · L)` solution is given. Provide 2–3 faster
approaches.

**Approaches**

> **Key insight:** a container must be at least as long as every string it
> contains and is itself in the list, so the only viable candidate is a longest
> string. This reduces the candidates from `O(n)` to `O(1)`.

1. Sort by length, then brute force — shorter strings skip the global check.
2. Trie of the candidate, then test each string as a walk.
3. Suffix automaton of the candidate: `O(total characters)` overall.

---

## 12. Kth Largest Element in an Array

> **LeetCode 215**

**Problem.** Given an integer array `nums` and an integer `k`, return the k-th
largest element in the array. This is the k-th largest in sorted order, **not**
the k-th distinct element.

**Example**

```text
nums = [3, 2, 1, 5, 6, 4], k = 2  ->  5
```

**Approach**

1. Min-heap of size `k`: keep the `k` largest seen so far; the root is the k-th
   largest. Time `O(n log k)`, space `O(k)`.
2. Alternative: Quickselect (partition around a pivot) for `O(n)` average time,
   `O(1)` extra space.

---

## 13. Subarray Sum Equals K

> **LeetCode 560** (variant)

**Problem.** Given an integer array `nums` and an integer `k`, return the total
number of contiguous subarrays whose elements sum to `k`. Values may be
negative.

**Example**

```text
nums = [1, 1, 1], k = 2  ->  2
```

**Approach**

1. Running prefix sum plus a hash map of `prefix-sum -> count` seen so far
   (seed with `{0: 1}` for subarrays starting at index 0).
2. At each index, a subarray ending here sums to `k` iff some earlier prefix
   equals `prefix - k`; add that count to the answer, then record the current
   prefix. Time `O(n)`, space `O(n)`.

---

## 14. Best Rating-to-Price Index

**Problem.** Given two equal-length integer arrays `rating` and `prices`, return
the index `i` that maximizes the ratio `rating[i] / prices[i]`. If several indices
tie for the maximum, return the **smallest** such index. Prices are positive.

**Example**

```text
rating = [4, 2, 7], prices = [2, 1, 5]  ->  0
(ratios 2.0, 2.0, 1.4; indices 0 and 1 tie, so keep the smaller index 0)
```

**Notes**

- Avoid floating-point division. Compare two ratios `a/b` and `c/d` by
  cross-multiplying: `a/b > c/d` iff `a*d > c*b` (valid because prices are
  positive, so the inequality direction is preserved).

**Approach**

1. Track the best index, starting at 0.
2. For each later index, compare it against the current best via
   cross-multiplication; update only on a **strict** improvement so ties keep the
   earlier (smaller) index.

---

## 15. Complete Round-Trip Missions

**Problem.** You must complete `missions` round trips between A and B. `a2b` lists
the A→B departure times and `b2a` the B→A departure times, each sorted ascending.
Starting at time `start`, each round trip boards the earliest A→B departure that
is **not earlier than** the current time, then the earliest B→A departure not
earlier than that. Return the time at which all missions are finished.

**Example**

```text
a2b = [1, 3, 5, 7], b2a = [2, 4, 6, 8], missions = 2, start = 0  ->  4
(trip 1: A->B at 1, B->A at 2; trip 2: A->B at 3, B->A at 4)
```

**Notes**

- "Not earlier than" means `>=`, so a connection may leave at the exact current
  time.
- Assumes enough departures exist to complete every mission.

**Approach**

1. Keep a running `current` time (initially `start`).
2. For each mission, binary-search `a2b` for the first time `>= current` and
   advance `current` to it; then do the same in `b2a`.
3. After `missions` iterations, `current` is the answer.

---

## 16. Apply Matrix Commands

**Problem.** Given a 2D array and a list of commands, apply the commands in order
and return the resulting matrix. Supported commands:

```text
("swap_row", i, j)     swap rows i and j
("swap_col", i, j)     swap columns i and j
("reverse_row", i)     reverse row i
("reverse_col", i)     reverse column i
("rotate",)            rotate the whole matrix 90 degrees clockwise
```

**Example**

```text
matrix = [[1, 2], [3, 4]], commands = [("rotate",), ("reverse_row", 0)]  ->  [[1, 3], [4, 2]]
(rotate -> [[3, 1], [4, 2]]; then reverse row 0)
```

**Approach**

1. Row/column swaps and reversals are direct index manipulations.
2. Implement a 90° clockwise rotation as a **transpose** (swap rows with columns)
   followed by **reversing each row**.

---

## 17. Count Access-Code Pairs

**Problem.** Given a list of strings `words` and a target string `accesscode`,
count the ordered pairs of indices `(i, j)` such that `words[i] + words[j]`
equals `accesscode`. The two indices are chosen independently, so a pair may
reuse the same index when both halves are equal.

**Example**

```text
words = ["a", "b", "ab", "c"], accesscode = "ab"  ->  1
("a" + "b" = "ab")
```

**Approach**

1. Count how many times each string appears in `words`.
2. Split `accesscode` at every position into a `left` and `right` part; each split
   is one way to form the code, contributing `count[left] * count[right]` pairs.
3. Sum those products over all split positions.

---

## 18. Merge Three Sorted Arrays

> **LeetCode 88** (variant)

**Problem.** Given three arrays sorted in ascending order, merge them into a
single ascending array with all duplicates removed — both repeats within one
array and values shared across arrays.

**Example**

```text
a = [1, 2, 5], b = [2, 3], c = [3, 6]  ->  [1, 2, 3, 5, 6]
```

**Approach**

1. Keep one index per array. Repeatedly take the smallest value among the three
   current heads.
2. Advance every pointer whose head equals that value (drops cross-array
   duplicates), and append it only if it differs from the last value written
   (drops within-array duplicates).
3. Continue until all three arrays are exhausted. (`heapq.merge(a, b, c)` plus a
   consecutive-dedup pass is an idiomatic one-line alternative.)

---

## 19. Simplify Path

> **LeetCode 71**

**Problem.** Given an absolute Unix-style `path` (it always begins with `/`),
return its canonical form. In the canonical path: a single `.` means the current
directory, `..` means the parent directory, multiple consecutive slashes collapse
to one, and there is no trailing slash (except the root `/` itself).

**Example**

```text
"/home/"            ->  "/home"
"/../"              ->  "/"
"/home//foo/"       ->  "/home/foo"
"/a/./b/../../c/"   ->  "/c"
```

**Notes**

- `..` at the root stays at the root.

**Approach**

1. Split on `/` and walk the parts with a stack: skip `""` and `.`, pop on `..`
   (if the stack is non-empty), otherwise push the name.
2. Join the stack with `/`, prefixed by a leading `/` (yielding `/` when empty).

---

## 20. Binary Tree Vertical Order Traversal

> **LeetCode 314**

**Problem.** Given the root of a binary tree, return its vertical order
traversal — node values grouped by column from leftmost to rightmost. Within a
column, order nodes top to bottom; when two nodes share the same row **and**
column, order them left to right.

**Example**

```text
    3            ->  [[9], [3, 15], [20], [7]]
   / \
  9  20
     / \
    15  7
```

**Notes**

- Assign the root column `0`; a left child is `col - 1`, a right child `col + 1`.
  The row (depth) increases by 1 each level.

**Approach**

1. DFS from the root carrying `(row, col)`, appending `(row, value)` into a map
   keyed by column. Visiting the left child before the right records same-depth
   nodes left to right.
2. Emit columns in increasing order; within each column, stable-sort by row (the
   DFS order already breaks ties left to right).
3. DFS uses the recursion stack (`O(height)`) instead of an explicit BFS queue
   (`O(width)`) — the memory trade-off noted in the prompt.

---

## 21. Find a Local Minimum

> **LeetCode 162** (variant)

**Problem.** Given an integer array `nums` in which adjacent elements differ,
return the index of any local minimum — an element strictly smaller than both
neighbors. Treat the out-of-bounds neighbors before index 0 and after the last
index as `+∞`, so a local minimum always exists. Solve **iteratively** in
`O(log n)`.

**Example**

```text
[3, 2, 1, 2, 3]  ->  2   (nums[2] = 1 is smaller than both neighbors)
```

**Notes**

- This mirrors Find Peak Element (LeetCode 162) with the comparison flipped to
  seek a valley instead of a peak.
- Each step needs only a single comparison (`nums[mid]` vs `nums[mid + 1]`),
  which minimizes the condition checks (the interview follow-up).

**Approach**

1. Binary search with `lo = 0`, `hi = n - 1`. At `mid`, if
   `nums[mid] > nums[mid + 1]` the slope descends to the right, so a local min
   lies in `[mid + 1, hi]` (`lo = mid + 1`); otherwise it lies in `[lo, mid]`
   (`hi = mid`).
2. The window shrinks to a single index, which is a local minimum.
3. Alternative `O(n)` scan: keep a `prev` value (initially `+∞`) and return the
   first index `i` where `prev > nums[i] < next`.

---

## 22. Randomized Container (Insert / Pop Random)

> **LeetCode 380** (variant)

**Problem.** Design a container supporting two operations, each in average
`O(1)`:

- `insert(element)` — add an element.
- `pop_random()` — remove and return one element, with every current element
  equally likely.

**Example**

```text
insert(1); insert(2); insert(3)
pop_random()  ->  one of 1, 2, 3 (uniformly), and it is removed from the container
```

**Notes**

- Assumes distinct elements (the LeetCode 380 baseline); to allow duplicates,
  map each value to a *set* of indices (LeetCode 381).

**Approach**

1. Keep a dynamic array of the elements plus a hash map from element to its index
   in that array.
2. `insert`: append to the array and record its index in the map.
3. `pop_random`: pick a uniformly random index; swap that element with the last
   one (updating the moved element's stored index), pop the last slot, and delete
   the map entry. Swapping to the end makes removal `O(1)` instead of `O(n)`.

---

## 23. Count Distinct Values in a Sorted Array

**Problem.** Given a sorted array holding only `K` distinct values, where `K` is
much smaller than the length `n`, return `K`. Aim to beat the obvious `O(n)`
scan.

**Example**

```text
[1, 1, 2, 2, 2, 3]  ->  3
```

**Notes**

- The `O(n)` baseline walks the array once, using a `prev` value to count each
  time the value changes.
- Watch the boundary: when jumping past a run of equal values, land on the
  **first** index strictly greater, or a value can get counted twice.

**Approach**

1. Baseline `O(n)`: scan once and increment the count whenever the current value
   differs from the previous one.
2. `O(K log n)`: for each distinct value at index `i`, binary-search the first
   index whose value is strictly greater (`bisect_right`), jump there, and
   repeat. Each of the `K` values costs one `O(log n)` search.
3. Since `K << n`, galloping/exponential search from each boundary refines this
   to `O(K log(n/K))`.

---

## 24. System Design: Design Twitter

> **System design** (discussion only — no reference solution)

**Problem.** Design a simplified Twitter-like service that supports three core
operations:

- **add a post** — a user publishes a post,
- **retrieve posts** — e.g. a user's timeline / feed,
- **search posts** — find posts matching a query.

**Discussion areas.** Work through the design roughly in this order:

1. High-level architectural design
2. API design
3. Data streaming
4. Database selection
5. Service scaling
6. Feature workflow walk-through

---

## 25. Plan Round Trip With Minimum Flight Cost

**Problem.** Given a departure-cost array `D` and a return-cost array `R` (both
indexed by day, same length), plan a round trip whose departure day is strictly
before the return day. Return:

1. the minimum total cost `D[i] + R[j]` over all `i < j`, and
2. the chosen departure index `i` and return index `j`. If several pairs tie for
   the minimum cost, prefer the **earliest departure**; if still tied, the
   **latest return**.

**Example**

```text
D = [4, 1, 3], R = [5, 2, 4]  ->  cost 5 at (departure = 1, return = 2)
```

**Notes**

- Requires `i < j` — you must depart before you return.
- Tie-break precedence: (1) minimum cost, (2) earliest departure index, (3)
  latest return index.

**Approach**

1. Scan the return day `j` from left to right while maintaining the minimum
   departure cost seen in `D[0..j-1]`, keeping its **earliest** index on ties.
2. For each `j`, the best round trip returning on day `j` is
   `min_departure + R[j]`; compare it against the global best using the tie-break
   rules above.
3. One pass — `O(n)` time, `O(1)` space.

---

## 26. Maximum Characters From Non-Overlapping Words

> **AI-enabled coding** (related to LeetCode 1239)

**Problem.** Given a list of lowercase words, choose a subset in which no two
words share any common character (their letter sets are pairwise disjoint), so
that the subset captures the maximum total number of distinct characters. Return
that maximum count.

**Example**

```text
["ab", "cd", "abc"]  ->  4   (pick "ab" + "cd"; "abc" overlaps both)
```

**Notes**

- "Not overlapping" is defined on letter *sets*: two words conflict if they share
  any letter. A word with repeated letters (e.g. `"aa"`) contributes only its
  distinct letters.
- Assumes the 26 lowercase letters, so each word fits in a 26-bit mask.

**Approach**

1. Encode each word as a 26-bit bitmask of its letters; its contribution is the
   popcount (number of distinct letters).
2. Backtrack over the words, keeping a `used` mask of letters already taken. A
   word can be added only if `used & mask == 0`.
3. Track the best total distinct-character count across all reachable subsets.
   (Reconstructing the actual subset is a small extension.)

---

## 27. Merge Two Sorted Interval Lists

> **LeetCode 56** (variant)

**Problem.** Given two lists of intervals `A` and `B`, each already sorted by
start and internally non-overlapping, merge them into a single list sorted by
start with all overlapping (or touching) intervals coalesced.

**Example**

```text
A = [[1, 3], [5, 7]], B = [[2, 4], [6, 8]]  ->  [[1, 4], [5, 8]]
```

**Notes**

- Intervals that only touch at an endpoint (e.g. `[1, 3]` and `[3, 5]`) are
  merged into `[1, 5]`. Switch the comparison to strict `<` if touching intervals
  should stay separate.

**Approach**

1. Two-pointer merge of `A` and `B` by start into one start-sorted sequence (like
   merging two sorted arrays) — `O(n + m)`.
2. Sweep the sequence, extending the last kept interval's end when the next
   interval starts at or before it, otherwise appending a new interval.

---

## 28. System Design: Trending Hashtags

> **System design** (discussion only — no reference solution)

**Problem.** Design a backend system that detects and serves trending hashtags
from Facebook posts. Requirements:

- **Timeliness** — a trend should surface while the real-world event is still
  happening; target end-to-end latency of ~1 minute.
- **Recency window** — consider posts from the last 24 hours, weighting more
  recent posts more heavily.
- **Popularity** — a trend should be of interest to many people in the community.
- **Novelty** — a trend should be about something new: people were not posting
  about it before, or at least not with the same intensity.

**Discussion areas.**

1. High-level architecture (ingestion → stream processing → scoring → serving)
2. Streaming ingestion of posts and hashtag extraction
3. Windowed counting over a 24-hour horizon with recency weighting (time-decay /
   sliding windows)
4. Scoring model combining popularity and novelty (spike/velocity vs. a
   historical baseline)
5. Storage choices for counts, baselines, and the ranked trend list
6. Serving the top trends with ~1-minute freshness; caching and read scaling
7. Scaling, sharding by hashtag, fault tolerance, and handling hot keys / spam
