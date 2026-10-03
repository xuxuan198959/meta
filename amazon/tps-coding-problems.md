# Amazon TPS — Coding Problem List

The 28 coding problems from the recruiter deck
[`Latest good font Aug 13th 2026 first round of interview ppp.pptx`](<./Latest good font Aug 13th 2026 first round of interview ppp.pptx>)
(slides 10–16), mapped to LeetCode numbers and **sorted by Amazon frequency**.
The deck names the problems but gives no numbers and has no speaker notes, so
each mapping is inferred from the name plus the approach the slide lists.
Ambiguous ones are marked ⚠ and explained [below](#notes-on-the--mappings).

**Format reminder:** one problem, 30–35 minutes, in LiveCode — a plain text
editor with no autocomplete, no syntax highlighting, and no run button. Practice
in a plain editor against a 30-minute timer, talking aloud.

## Sorted by frequency

**Source:** LeetCode's Amazon company-tag frequency, via the public mirror
[liquidslr/leetcode-company-wise-problems](https://github.com/liquidslr/leetcode-company-wise-problems/tree/main/Amazon)
(last updated 2026-08-16). *Freq* is LeetCode's 0–100 score on the all-time
list; *Rank* is position among the 2,011 Amazon-tagged problems; *6-mo rank*
is position among the 725 asked in the last six months.

| # | Problem | LeetCode | Diff | Freq | Rank | 6-mo rank | Slide section | In Meta README? |
|---|---|---|---|---|---|---|---|---|
| 1 | Two Sum | **1** | Easy | 100.0 | 1 | 1 | Array & String | |
| 2 | LRU Cache | **146** | Med | 88.5 | 2 | 5 | Stack/Queue/Design | |
| 3 | Trapping Rain Water | **42** | Hard | 88.0 | 3 | 2 | Array & String | |
| 4 | Number of Islands | **200** | Med | 85.6 | 4 | 7 | Tree & Graph | ✅ [#51](../README.md#51-number-of-islands--shortest-path-in-a-grid) |
| 5 | Longest Substring w/o Repeats | **3** | Med | 84.5 | 5 | 4 | Array & String | |
| 6 | Group Anagrams | **49** | Med | 80.6 | 7 | 9 | Array & String | |
| 7 | Add Two Numbers | **2** | Med | 79.7 | 8 | 6 | Linked List | |
| 8 | Merge Intervals | **56** | Med | 76.6 | 14 | 12 | Array & String | [#27](../README.md#27-merge-two-sorted-interval-lists) is a variant |
| 9 | Course Schedule | **207** ⚠ | Med | 75.0 | 15 | 13 | Tree & Graph | [#50](../README.md#50-course-schedule-ii-topological-sort) is 210, same algorithm |
| 10 | Valid Parentheses | **20** | Easy | 74.4 | 17 | 36 | Stack/Queue/Design | [#6](../README.md#6-minimum-add-to-make-parentheses-valid) (921) is related |
| 11 | Most Popular Locker Size → Top K Frequent | **347** ⚠ | Med | 71.7 | 23 | 28 | Stack/Queue/Design | |
| 12 | Lowest Common Ancestor | **236** ⚠ | Med | 69.9 | 28 | 26 | Tree & Graph | [#45](../README.md#45-lowest-common-ancestor-iii) is 1650, a different variant |
| 13 | Copy List w/ Random Ptr | **138** | Med | 69.8 | 29 | 33 | Linked List | |
| 14 | Product Except Self | **238** | Med | 67.5 | 34 | 54 | Array & String | |
| 15 | Climbing Stairs | **70** | Easy | 67.0 | 36 | 37 | DP | |
| 16 | Merge Two Sorted Lists | **21** | Easy | 66.7 | 38 | 40 | Linked List | ✅ [#60](../README.md#60-linked-list-core-set) |
| 17 | Min Window Substring | **76** | Hard | 61.7 | 55 | 35 | Array & String | |
| 18 | Word Break | **139** | Med | 60.2 | 68 | 124 | DP | |
| 19 | Min Stack | **155** | Med | 58.6 | 80 | 108 | Stack/Queue/Design | |
| 20 | Serialize/Deserialize Tree | **297** | Hard | 56.5 | 96 | 165 | Tree & Graph | |
| 21 | Reverse in Groups of K | **25** | Hard | 56.0 | 98 | 141 | Linked List | |
| 22 | Level Order Traversal | **102** | Med | 54.4 | 109 | 225 | Tree & Graph | |
| 23 | Find Missing Number | **268** | Easy | 54.4 | 110 | 258 | Array & String | |
| 24 | Longest Increasing Subseq | **300** | Med | 52.7 | 127 | 148 | DP | |
| 25 | Validate BST | **98** | Med | 52.4 | 129 | 189 | Tree & Graph | ✅ [#53](../README.md#53-bst-search-insertion--validation) |
| 26 | Partition Equal Subset Sum | **416** | Med | 52.0 | 132 | 101 | DP | |
| 27 | Autocomplete System | **642** | Hard | 25.1 | 615 | — | Stack/Queue/Design | |
| 28 | MRU Queue | **1756** ⚠ | Med | — | — | — | Stack/Queue/Design | |

For reference, the related variants: **210** Course Schedule II — freq 65.8,
rank 39; **235** LCA of a BST — freq 45.1, rank 199.

## How to read this

- **Top 10 (rank ≤ 17)** are all among Amazon's most-asked problems overall.
  Do these first and do them until they're automatic.
- **Two disagreements with the deck.** It calls **Autocomplete (642)** an
  "Amazon favorite", but it ranks 615th all-time and doesn't appear in the
  six-month list. **MRU Queue (1756)** isn't on Amazon's tag list at all. Both
  are probably recruiter-side picks or Amazon-internal variants. Learn the
  approach, but they're last in priority.
- **Recent trend (6-mo rank):** 76 Min Window moved up (55 → 35). 238, 139, 102,
  98 and 268 moved down noticeably.

## Notes on the ⚠ mappings

- **LCA → 236.** The slide's approach is "recursive DFS, O(n)", which is the
  general binary-tree version. LC 235 (BST) is the easier follow-up worth knowing.
- **Course Schedule → 207.** Same Kahn's algorithm as 210; 207 returns a boolean
  instead of the order.
- **MRU Queue → 1756** (Design Most Recently Used Queue, premium). The closest
  match, but the slide's "Linked List + HashMap, O(1)" doesn't fit: LC 1756's
  `fetch(k)` can't be O(1) with that structure — good solutions are O(√n)
  bucketing or a Fenwick tree. It may be an Amazon-internal variant; prepare
  1756 and clarify the operations up front.
- **Most Popular Locker Size → no LeetCode problem.** Amazon-internal (Amazon
  Lockers). The slide's approach — "frequency count + max heap, O(n log k)" — is
  exactly **LC 347 Top K Frequent Elements**, so 347's frequency is used above.
- **Premium:** 642 and 1756 need LeetCode Premium.

## Status

4 of the 28 are already covered in the Meta [`README.md`](../README.md) (21, 98,
200, and 207 via 210), leaving **24 new problems**.
