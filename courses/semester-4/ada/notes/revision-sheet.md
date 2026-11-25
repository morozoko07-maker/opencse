---
title: Revision sheet
---

# Revision sheet — Analysis and Design of Algorithms

The banks give question shapes, the notes give traces. Module 3's bank is scanned, so its section quotes no question. Write each recurrence and tree.

## Exam pattern

The README gives CIE 50 + SEE 50. No model paper with usable text exists. Bank marks (4–10) and session labels belong to those papers, not a confirmed SEE pattern.

## Module 1 — Introduction to algorithms

### Must know

- An algorithm is finite, unambiguous, effective, and has defined inputs and outputs.
- Best, worst and average case differ by the input; average case assumes a distribution.
- Time counts basic operations; space counts extra memory.
- Growth: 1 < log n < n < n log n < n² < n³ < 2ⁿ < n!.
- O is an upper bound, Ω a lower bound, Θ a tight bound.
- Prove a bound by finding c and n₀; prove Θ by proving O and Ω.
- Non-recursive analysis counts loop executions; recursive analysis forms a recurrence.
- Brute force gives selection sort Θ(n²) and string matching O(mn).

### Definitions to reproduce

> An algorithm is a finite sequence of unambiguous instructions that, given inputs, produces outputs and terminates.

> f(n) = O(g(n)) if positive constants c and n₀ exist such that 0 ≤ f(n) ≤ c·g(n) for all n ≥ n₀.

## Module 2 — Divide and conquer

### Must know

- Divide, conquer, combine; the cost obeys T(n) = aT(n/b) + f(n).
- The master theorem compares n^(log_b a) with f(n) and gives three cases.
- Binary search halves a sorted array and runs in O(log n).
- Finding both maximum and minimum takes about 3n/2 − 2 comparisons.
- Merge sort is Θ(n log n) always, stable, and needs O(n) extra space.
- Quick sort is Θ(n log n) on average and Θ(n²) in the worst case.
- Topological sorting uses source removal or DFS and runs in O(V + E).
- Recursion and merging add overhead but suit parallel machines.

### Definitions to reproduce

> Divide and conquer splits a problem into smaller subproblems of the same type, solves them recursively, and combines their results.

> The master theorem solves T(n) = aT(n/b) + f(n) for a ≥ 1 and b > 1.

## Module 3 — Greedy method

### Must know

- Greedy takes the locally best choice and never reconsiders it.
- Fractional knapsack sorts by profit-to-weight ratio and takes a fraction of the last item.
- Correctness needs an exchange argument, not intuition.
- Greedy on 0/1 knapsack by profit, weight or ratio can be wrong.
- Job sequencing sorts by profit and fills the latest free slot before each deadline.
- Prim grows one tree; Kruskal sorts edges and uses union-find to avoid cycles.
- Dijkstra needs non-negative weights; it fails on negative edges.
- Huffman merges the two lowest frequencies to build an optimal prefix code.

### Definitions to reproduce

> A greedy algorithm builds a solution step by step, choosing the best option at that step and never undoing an earlier choice.

> A minimum spanning tree of a connected weighted graph is a spanning tree of minimum total edge weight.

## Module 4 — Dynamic programming

### Must know

- DP needs overlapping subproblems and optimal substructure.
- Memoisation is top-down with a cache; tabulation is bottom-up.
- Multistage graphs are solved stage by stage, forward or backward.
- Warshall finds transitive closure in Θ(n³); Floyd finds all-pairs paths in Θ(n³).
- Optimal BST chooses a root that minimises weighted search cost.
- 0/1 knapsack uses V[i][w] = max(V[i−1][w], vᵢ + V[i−1][w−wᵢ]).
- Bellman-Ford allows negative edges, runs in O(VE), and detects negative cycles.
- TSP has an O(n²2ⁿ) DP over subsets.

### Definitions to reproduce

> Dynamic programming combines solutions to overlapping subproblems, storing each result so it is computed once.

> The transitive closure of a directed graph is the set of pairs (u, v) for which a path exists from u to v.

## Module 5 — Backtracking and branch and bound

### Must know

- Backtracking is depth-first search of a state-space tree, pruned by constraints.
- N-queens places one queen per row and checks column and diagonals.
- Subset sum includes or excludes an item and prunes impossible remainders.
- Graph colouring rejects a colour already used by an adjacent vertex.
- A Hamiltonian cycle visits every vertex once and returns to the start.
- Branch and bound prunes with a bound; the queue may be FIFO, LIFO or least-cost.
- Knapsack bounding uses the fractional relaxation.
- P is polynomial-time solvable; NP is polynomial-time verifiable; NP-complete is in NP and NP-hard.

### Definitions to reproduce

> Backtracking builds candidates incrementally and abandons a partial candidate as soon as it cannot lead to a valid solution.

> A problem is NP-complete if it is in NP and every problem in NP reduces to it in polynomial time.

## Last 24 hours

1. Apply the master theorem to the Module 2 recurrences.
2. Trace merge sort on 70, 20, 30, 40, 10, 50, 60.
3. Trace quick sort on 65, 70, 75, 80, 85, 60, 55, 50, 45.
4. Solve one multistage graph and one 0/1 knapsack table.
5. Draw the 4-queens tree and mark both solutions.
6. Recite P, NP, NP-complete and NP-hard with one example each.

## Question bank

*The Module 3 bank (`Module -3QB.pdf`) is a scanned image: pdftotext returns five bytes, so no Module 3 question is reproduced below.*

**Module 1**

1. Define algorithm and discuss the criteria it must satisfy, with an example. [6]
2. Explain Big O, Big Ω and Big Θ with examples. [6]

**Module 2**

3. State and explain the master theorem. [5]
4. Write merge sort, illustrate it, and derive its best, average and worst case efficiencies. [8]
5. Trace quick sort for 65, 70, 75, 80, 85, 60, 55, 50, 45 and draw the recursion tree. [8]

**Module 4**

6. Explain a multistage graph with an example. [4]
7. Solve the 0/1 knapsack n = 3, weights {1, 2, 2}, profits {18, 16, 6}, capacity 4. [4]

**Module 5**

8. Explain 4-queens using a state-space tree. [6/8]
9. For w = {3, 5, 6, 7}, m = 15, find all subsets that sum to m and draw the tree. [9]
10. Explain P, NP, NP-complete and NP-hard with examples. [6/8]

*Source: `Module-1 QB.pdf`, `Module-2 QB.pdf`, `Module-4 QB.pdf`, `Module 5 QB.pdf` and module notes. Marks are as printed in the banks.*
