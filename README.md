# Interview Questions

Each entry has a **problem statement**, an **example** where helpful,
**notes/constraints**, and a suggested **approach**. Reference solutions live
in [`solutions.py`](./solutions.py).

Full multi-round interview loops (a whole VO written up in one file) live under
[`interviews/`](./interviews/) — e.g.
[Product VO — 4-round AI-Enabled loop](./interviews/product-vo-ai-enabled.md).
Standalone system-design write-ups live under
[`system-design/`](./system-design/).

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
| 29 | [Banking System](#29-banking-system) | multi-level |
| 30 | [Diameter of Binary Tree](#30-diameter-of-binary-tree) | LeetCode 543 |
| 31 | [Palindromic Substrings](#31-palindromic-substrings) | LeetCode 647 |
| 32 | [System Design: Web Crawler](#32-system-design-web-crawler) | System design |
| 33 | [Remove Duplicates from Sorted Array](#33-remove-duplicates-from-sorted-array) | LeetCode 26 |
| 34 | [Longest Increasing Path in a Matrix](#34-longest-increasing-path-in-a-matrix) | LeetCode 329 |
| 35 | [Valid Number](#35-valid-number) | LeetCode 65 |
| 36 | [Best Time to Buy and Sell Stock](#36-best-time-to-buy-and-sell-stock) | LeetCode 121 |
| 37 | [Collapse Adjacent Duplicate Letters](#37-collapse-adjacent-duplicate-letters) | LeetCode 1047 (variant) |
| 38 | [System Design: Message Queue Service](#38-system-design-message-queue-service) | System design |
| 39 | [System Design: Taxi Request Service](#39-system-design-taxi-request-service) | System design |
| 40 | [Keypad Combinations with Grouped Presses](#40-keypad-combinations-with-grouped-presses) | LeetCode 17 (variant) |
| 41 | [System Design: Instagram](#41-system-design-instagram) | System design |
| 42 | [Diagonal Traverse](#42-diagonal-traverse) | LeetCode 498 |
| 43 | [Sum Root to Leaf Numbers](#43-sum-root-to-leaf-numbers) | LeetCode 129 |
| 44 | [Nested List Weight Sum](#44-nested-list-weight-sum) | LeetCode 339 |
| 45 | [Lowest Common Ancestor III](#45-lowest-common-ancestor-iii) | LeetCode 1650 |

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

---

## 29. Banking System

> **Multi-level assessment** (CodeSignal Industry Coding Framework)

**Problem.** Build a banking system that processes account operations. Every
operation carries an integer `timestamp` (strictly increasing across calls). The
assessment has four progressively harder levels; you must pass all tests in a
level before the next is revealed.

**Level 1 — accounts & transfers**

```text
create_account(timestamp, account_id)          -> True if created, False if it exists
deposit(timestamp, account_id, amount)          -> new balance, or None if no account
transfer(timestamp, source_id, target_id, amount)
    -> source's new balance, or None if: either account is missing, source ==
       target, or the source has insufficient funds
```

**Level 2 — spending analytics**

```text
top_spenders(timestamp, n)  -> the top n accounts by total OUTGOING amount
                               (money transferred/paid out), formatted
                               "id(total)", sorted by total desc then id asc
```

**Level 3 — scheduled payments & cashback**

```text
pay(timestamp, account_id, amount)
    -> withdraws `amount`, schedules a 2% cashback (floored) refunded 24h later
       (86_400_000 ms); returns a payment id like "payment1", or None if the
       account is missing or underfunded. Payment ids increment globally.
get_payment_status(timestamp, account_id, payment_id)
    -> "IN_PROGRESS" or "CASHBACK_RECEIVED", or None if the account/payment is
       invalid or the payment doesn't belong to that account
```

**Level 4 — merging accounts & historical balance**

```text
merge_accounts(timestamp, account_id1, account_id2)
    -> fold account2 into account1 (balances, outgoing totals, and pending
       cashbacks all combine); account2 ceases to exist. Returns True/False.
get_balance(timestamp, account_id, time_at)
    -> the balance of the account at `time_at`, or None if the account did not
       exist then
```

**Notes**

- Cashback is applied **lazily**: before handling any operation, process all
  scheduled cashbacks whose refund time is `<= current timestamp`. `pay` counts
  toward outgoing spend for `top_spenders`; the cashback refund does **not**.
- `merge` re-homes account2's pending cashbacks onto account1, and account2's
  historical balances remain queryable via account1 for times before the merge.

**Approach**

1. Store per-account balance plus a running `outgoing` total (for
   `top_spenders`) and a time-sorted balance history (for `get_balance`).
2. Keep scheduled cashbacks in a min-heap/queue keyed by refund time; drain the
   due ones at the start of every operation so state is current.
3. `top_spenders`: sort accounts by `(-outgoing, id)` and take `n`.
4. `merge`: sum balances/outgoing, reassign account2's pending cashbacks to
   account1, and keep account2's history so `get_balance` still resolves it.

---

## 30. Diameter of Binary Tree

> **LeetCode 543**

**Problem.** Given the root of a binary tree, return the length of its
**diameter** — the number of edges on the longest path between any two nodes.
The path may or may not pass through the root.

**Example**

```text
    1          ->  3   (path 4 -> 2 -> 1 -> 3, i.e. 3 edges)
   / \
  2   3
 / \
4   5
```

**Notes**

- Length is measured in **edges**, not nodes; a single-node tree has diameter 0.

**Approach**

1. DFS that returns the height (in edges) of each subtree.
2. At every node, the longest path *through* it is `left_height + right_height`;
   keep a running maximum of that across all nodes.
3. Return the maximum. Time `O(n)`, space `O(height)` for the recursion.

---

## 31. Palindromic Substrings

> **LeetCode 647**

**Problem.** Given a string `s`, return the number of **palindromic substrings**
in it. Substrings at different start/end positions count separately, even if they
are identical in content.

**Example**

```text
"abc"  ->  3   ("a", "b", "c")
"aaa"  ->  6   ("a", "a", "a", "aa", "aa", "aaa")
```

**Approach (expand around center)**

1. Every palindrome has a center: a single character (odd length) or the gap
   between two characters (even length) — `2n - 1` centers in all.
2. From each center, expand outward while the two ends match, counting one
   palindrome per successful expansion.
3. Time `O(n²)`, space `O(1)`. (A DP table is `O(n²)` time and space; Manacher's
   algorithm brings it down to `O(n)`.)

---

## 32. System Design: Web Crawler

> **System design** — full write-up in
> [`system-design/web-crawler.md`](./system-design/web-crawler.md)

**Problem.** Design a distributed web crawler that runs on a fleet of ~10,000
machines. It should fetch a large fraction of the web, extract links to keep
discovering new pages, store the crawled content, and periodically re-crawl to
stay fresh — all while behaving politely toward the sites it visits.

**Requirements**

- **Scale** — ~10k fetcher machines; target on the order of tens of billions of
  pages, hundreds of thousands of pages/sec aggregate.
- **Politeness** — respect `robots.txt` and per-host rate limits; never overload
  a site.
- **Coverage & de-duplication** — avoid re-fetching the same URL and avoid
  storing near-duplicate content.
- **Freshness** — re-crawl pages at a rate that tracks how often they change.
- **Fault tolerance** — survive machine failures with no lost or stuck work.

**Discussion areas.**

1. High-level architecture (URL Frontier → fetchers → parser → storage → link
   re-injection)
2. URL Frontier design (priority + politeness, host-based sharding)
3. De-duplication (URL Bloom filters, content SimHash/MinHash)
4. Storage (raw page blobs, metadata KV, link graph)
5. Adaptive re-crawl scheduling for freshness
6. Distributed coordination, sharding, and fault tolerance
7. Traps, JS-rendered pages, DNS caching, and anti-abuse

See the linked file for the detailed design.

---

## 33. Remove Duplicates from Sorted Array

> **LeetCode 26**

**Problem.** Given an integer array `nums` sorted in non-decreasing order, remove
the duplicates **in place** so each unique value appears once, keeping the
relative order. Return `k`, the number of unique elements; the first `k` slots of
`nums` must hold those values (whatever is left beyond `k` doesn't matter).

**Example**

```text
[0, 0, 1, 1, 1, 2, 2, 3, 3, 4]  ->  k = 5, nums[:5] = [0, 1, 2, 3, 4]
```

**Notes**

- Must run in place with `O(1)` extra space — no second array.

**Approach**

1. Two pointers: `slow` marks the last unique slot (starts at 0), `fast` scans
   ahead.
2. Since the array is sorted, `nums[fast]` is new exactly when it differs from
   `nums[slow]`; on that, advance `slow` and copy `nums[fast]` there.
3. After the scan, `slow + 1` is the count of unique elements. Time `O(n)`,
   space `O(1)`.

---

## 34. Longest Increasing Path in a Matrix

> **LeetCode 329**

**Problem.** Given an `m x n` integer matrix, return the length of the longest
**strictly increasing** path. From a cell you may step to an adjacent cell (up,
down, left, or right) with a strictly greater value; no diagonal moves and no
stepping off the grid.

**Example**

```text
[[9, 9, 4],
 [6, 6, 8],
 [2, 1, 1]]   ->  4   (path 1 -> 2 -> 6 -> 9)
```

**Notes**

- Because moves only go to strictly greater values, the graph of moves is a
  **DAG** (edges always point low → high) — no cycles — which is what makes
  memoization safe.

**Approach**

1. DFS from each cell for the longest increasing path **starting** there,
   memoizing the result per cell.
2. `best(r, c) = 1 + max(best(neighbor))` over neighbors with a strictly greater
   value (just `1` if none qualify).
3. Answer is the max of `best` over all cells. Each cell is computed once →
   `O(m·n)` time and space. (Equivalently, a topological / out-degree peeling
   BFS.)

---

## 35. Valid Number

> **LeetCode 65**

**Problem.** Given a string `s`, return `true` if `s` is a valid number. A valid
number is an optional sign, then an **integer** or a **decimal**, optionally
followed by an **exponent**:

- *integer* — optional `+`/`-`, then one or more digits.
- *decimal* — optional `+`/`-`, then digits with a `.`; at least one digit must
  appear on some side of the dot, e.g. `2.`, `.8`, `3.14`.
- *exponent* — `e` or `E`, then an integer (which carries its own optional sign).

**Example**

```text
"0" -> true    "-90E3" -> true    "3e+7" -> true    ".8" -> true
"." -> false   "1e"    -> false   "e3"   -> false   "99e2.5" -> false
```

**Notes**

- A lone `.`, a lone sign, or an exponent with no digits are all invalid.
- `2.` and `.8` are valid — you only need at least one digit on *some* side of
  the dot.

**Approach**

1. Single left-to-right scan with small helpers: skip an optional sign, then skip
   a run of digits (reporting whether any were seen).
2. Parse `[sign] digits? [. digits?]` and require at least one digit across the
   integer and fractional parts.
3. If an `e`/`E` follows, require a valid signed integer after it. Valid iff the
   scan consumes the whole string. Time `O(n)`, space `O(1)`.

---

## 36. Best Time to Buy and Sell Stock

> **LeetCode 121**

**Problem.** Given an array `prices` where `prices[i]` is the price of a stock on
day `i`, choose one day to buy and a later day to sell. Return the maximum profit
achievable, or `0` if no profitable trade exists.

**Example**

```text
[7, 1, 5, 3, 6, 4]  ->  5   (buy at 1, sell at 6)
[7, 6, 4, 3, 1]     ->  0   (prices only fall)
```

**Approach**

1. Track the minimum price seen so far and the best profit so far in one pass.
2. At each day, update the running minimum, then check whether selling today
   (`price - min_so_far`) beats the best profit.
3. Return the best profit. Time `O(n)`, space `O(1)`.

---

## 37. Collapse Adjacent Duplicate Letters

> **LeetCode 1047** (variant)

**Problem.** Given a string of lowercase letters `a`–`z`, repeatedly remove a
group of **adjacent identical** letters. Removing a group can bring its former
neighbors together, which may form a new removable group — so the order of
removals matters and **different orders can yield different final strings**. The
interviewer accepts *any* valid reduction.

**Example**

```text
"abbaa":
  alt 1 -> ""    ("abbaa" => "aaa" => "")    remove "bb", the three a's merge, then cancel
  alt 2 -> "a"   ("abbaa" => "abb" => "a")   remove the trailing "aa", then "bb"
```

**Notes**

- If the operation is "cancel **two** adjacent equal letters" (pairwise), the
  process is *confluent* — the result is unique (here `"a"`). Removing a whole
  **run** at a time introduces the ambiguity, because an odd-length merged run
  (`"aaa"`) can vanish entirely.

**Approach**

1. **Pairwise cancel (unique, `O(n)`):** push each letter on a stack; if it
   equals the top, pop instead. The leftover stack is the unique
   no-two-adjacent-equal string → `"abbaa"` gives `"a"`.
2. **Whole-run collapse (`O(n²)`):** repeatedly delete the leftmost maximal run
   of length `≥ 2`, restarting after each deletion so cascading merges are caught
   → `"abbaa"` gives `""`.
3. Both are valid under the interviewer's rule; pick one and state which
   semantics you implemented.

---

## 38. System Design: Message Queue Service

> **System design** — design write-up (**TODO**) in
> [`system-design/message-queue.md`](./system-design/message-queue.md)

**Problem.** Design a distributed, durable message/streaming queue service in the
style of **Apache Kafka**: producers publish messages to topics, consumers
subscribe and read them, with high throughput and strong durability.

**Requirements**

- **Pub/sub over topics** — producers write, consumers (in groups) read.
- **Durability & ordering** — messages persisted; ordered within a partition.
- **High throughput & horizontal scale** — partitioned across brokers.
- **Delivery semantics** — at-least-once (ideally exactly-once) options.
- **Fault tolerance** — replication so a broker loss doesn't lose data.
- **Retention** — time/size-based; consumers track their own offsets.

**Discussion areas.**

1. High-level architecture (topics, partitions, brokers, producers, consumers)
2. Partitioning strategy and per-partition ordering guarantees
3. Storage / commit-log design (append-only segments, retention, compaction)
4. Replication & consistency (leader/follower, in-sync replicas, acks)
5. Consumer groups and offset management
6. Delivery semantics (at-least-once vs. exactly-once, idempotent producers)
7. Scaling, partition rebalancing, backpressure, and fault tolerance

---

## 39. System Design: Taxi Request Service

> **System design** — design write-up (**TODO**) in
> [`system-design/taxi-request-service.md`](./system-design/taxi-request-service.md)

**Problem.** Design a ride/taxi request service (Uber-like) with a twist on the
matching flow: instead of the platform auto-assigning one driver, a rider's
request is broadcast to **many nearby drivers who can accept concurrently**; the
**rider then selects one** of the accepting drivers; and the **selected driver
must confirm** the rider's choice before the ride is booked.

**Requirements**

- **Fan-out** — broadcast a request to nearby available drivers.
- **Concurrent accepts** — multiple drivers can offer to take the ride at once.
- **Rider selection** — the rider picks one driver from those who accepted.
- **Driver confirmation** — the chosen driver must confirm; handle decline or
  timeout by falling back to the other responders.
- **No double-booking** — a driver (and a rider) ends up on at most one ride;
  resolve the races this creates.
- **Real-time & location** — nearby-driver lookup and low-latency notifications.

**Discussion areas.**

1. High-level architecture (rider app, driver app, dispatch, location service)
2. Driver-location ingestion and geo-indexing (nearby-driver queries)
3. Request fan-out and how concurrent driver accepts are recorded
4. Selection/confirmation **state machine** (requested → offered → selected →
   confirmed → booked; with decline/timeout transitions)
5. Concurrency & consistency (a driver bookable once; optimistic locking / atomic
   compare-and-set; handling a driver who accepted several requests)
6. Timeouts, declines, and fallback to remaining responders
7. Real-time delivery (push / WebSockets) and scaling / geo-sharding / fault
   tolerance

---

## 40. Keypad Combinations with Grouped Presses

> **LeetCode 17** (variant)

**Problem.** Given a string of digits `0`–`9` (phone key presses), return every
letter combination it can produce. Each digit maps to letters:

```text
1->ABC  2->DEF  3->GHI  4->JKL  5->MNO  6->PQR  7->ST  8->UVW  9->XY  0->Z
```

Unlike LeetCode 17, **consecutive identical digits may be grouped**: a group of
`k` identical presses of digit `d` selects the **k-th** letter of `d`'s mapping.
The group size may not exceed the number of letters for that digit (so `7` groups
at most 2, `0` only 1). Only *consecutive identical* digits can share a group.
Return the results in any order.

**Example**

```text
"7772"    ->  ["SSSD", "STD", "TSD"]
              (7|7|7 = S,S,S; 7|77 = S,T; 77|7 = T,S; then 2 = D. "777" is invalid: no 3rd letter for 7)
"2222"    ->  ["DDDD", "DDE", "DED", "DF", "EDD", "EE", "FD"]
"123456"  ->  ["ADGJMP"]   (all distinct digits -> one letter each)
```

**Notes**

- Group size is bounded by `len(mapping[d])`; e.g. `7` and `9` cap at 2, `0` at 1.
- Because groups can't cross a change of digit, each maximal run of identical
  digits is partitioned independently and the runs' results combine in order.

**Approach**

1. Backtracking over the string. At index `i`, open a group on digit `d = s[i]`
   and extend it while the next character is still `d` **and** the group size
   stays `≤ len(mapping[d])`.
2. A group of size `k` contributes `mapping[d][k-1]`; recurse from `i + k`.
3. When the index reaches the end, record the built string. Results can be
   exponential in the input length; each has length `≤ n`.

---

## 41. System Design: Instagram

> **System design** — design write-up (**TODO**) in
> [`system-design/instagram.md`](./system-design/instagram.md)

**Problem.** Design a photo/video-sharing service like **Instagram**: users
upload media, follow other users, and see a home feed of posts from the people
they follow, plus likes, comments, and an explore/search surface.

**Requirements**

- **Upload & serve media** — photos/videos stored durably and served fast
  (blob store + CDN, multiple resolutions/transcodes).
- **Follow graph** — users follow others; asymmetric relationships.
- **Home feed** — recent posts from followees, ranked/reverse-chronological.
- **Engagement** — likes and comments at scale.
- **Read-heavy** — far more feed reads than writes; optimize for read latency.
- **Extras to consider** — stories, explore/search, notifications.
- **Live-auction extension** — users place bids and watch the highest price
  update in real time; the interesting part is the concurrency control on the
  hot `current_max_bid` row (**optimistic vs. pessimistic locking** under
  celebrity-level contention). Written up in the linked file.

**Discussion areas.**

1. High-level architecture (upload service, media/blob store + CDN, feed service,
   graph service)
2. Media handling (upload flow, transcoding, thumbnails, CDN delivery)
3. Feed generation — **fan-out on write vs. fan-out on read**, and the hybrid for
   celebrity/hot accounts
4. Data model & storage choices (posts, follow graph, counters for likes)
5. Caching and read scaling for the feed
6. Notifications and the explore/search surface
7. Sharding, hot keys, and fault tolerance

---

## 42. Diagonal Traverse

> **LeetCode 498**

**Problem.** Given an `m x n` matrix, return all its elements in **zig-zag
diagonal order**: the first diagonal goes up-right, the next goes down-left, and
so on, alternating.

**Example**

```text
[[1, 2, 3],
 [4, 5, 6],   ->  [1, 2, 4, 7, 5, 3, 6, 8, 9]
 [7, 8, 9]]
```

**Notes**

- All cells on one diagonal share the same `row + col = d`; there are
  `m + n - 1` diagonals.

**Approach**

1. Iterate `d` from `0` to `m + n - 2`. Even `d` → traverse the diagonal
   up-right (row decreasing, col increasing); odd `d` → down-left.
2. Start each diagonal at its clamped endpoint so you never step out of bounds.
3. Time `O(m·n)`, `O(1)` extra space beyond the output.

---

## 43. Sum Root to Leaf Numbers

> **LeetCode 129**

**Problem.** Given a binary tree where every node holds a digit `0`–`9`, each
root-to-leaf path spells a number (digits concatenated top to bottom). Return the
sum of all those numbers.

**Example**

```text
    1          ->  25   (path 1->2 = 12, path 1->3 = 13; 12 + 13)
   / \
  2   3
```

**Approach**

1. DFS carrying the number built so far; at each node `cur = cur * 10 + val`.
2. At a leaf, contribute `cur`; otherwise sum the contributions of both children.
3. Time `O(n)`, space `O(height)`.

---

## 44. Nested List Weight Sum

> **LeetCode 339**

**Problem.** Given a nested list of integers, each integer has a **weight equal
to its depth** (integers at the top level have depth 1, one level deeper depth 2,
and so on). Return the sum of every integer multiplied by its depth.

**Example**

```text
[[1, 1], 2, [1, 1]]  ->  10   (2*(1+1) + 1*2 + 2*(1+1))
[1, [4, [6]]]        ->  27   (1*1 + 4*2 + 6*3)
```

**Approach**

1. DFS over the structure with the current `depth` (starts at 1).
2. For a sublist, recurse with `depth + 1`; for an integer, add `value * depth`.
3. Time `O(total elements)`, space `O(max depth)`.

---

## 45. Lowest Common Ancestor III

> **LeetCode 1650**

**Problem.** Given two nodes `p` and `q` in a binary tree where **each node has a
`parent` pointer** (and you are *not* given the root), return their lowest common
ancestor.

**Notes**

- With parent pointers, walking from a node toward the root traces its ancestor
  chain — the problem reduces to finding where two upward chains first meet.

**Approach**

1. Two pointers `a = p`, `b = q`, each walking up via `parent`.
2. When a pointer reaches the top (`None`), redirect it to the *other* start
   node. After each pointer has traversed its own chain plus the other's prefix,
   they've covered equal distance and meet at the LCA.
3. Time `O(h₁ + h₂)`, space `O(1)`. (Same trick as intersection of two linked
   lists; an alternative is collecting one chain into a set and walking the other
   up until a match.)
