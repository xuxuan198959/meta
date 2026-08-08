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
