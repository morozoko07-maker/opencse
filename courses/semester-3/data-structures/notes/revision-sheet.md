---
title: Revision sheet
---

# Revision sheet — Data Structures and Applications

A last-week sheet. Modules 1 and 2 have long chapters in [the notes](01-module-1-part-a.html); this page covers all five. Read a module, then answer its questions without looking.

## Exam pattern

CIE 50 + SEE 50. The model paper is **100 marks in 3 hours: five questions, one per module**, each with two 10-mark parts and an internal OR.

## Module 1 — Introduction, arrays and stacks

### Must know

- A data structure organises data for efficient operations.
- Operations: insert, delete, traverse, search, sort.
- Linear: array, stack, queue, list. Non-linear: tree, graph.
- An array is contiguous, fixed-size, with O(1) index access.
- A structure groups fields; `typedef` names the type.
- `malloc`, `calloc`, `realloc`, `free` manage heap memory.
- A stack is LIFO with push, pop and top; guard overflow.
- Precedence is `^`, then `* /`, then `+ −`.

### Definitions to reproduce

> A data structure organises data in memory so that it can be used efficiently.

> A stack inserts and deletes at one end, the top, in last-in-first-out order.

### Worked pattern — infix to postfix

Scan left to right: operands to output, `(` push, `)` pop to `(`, operator pops while the top has higher or equal precedence. Thus `(A+B*C)*((D+E−F)/J)` gives `A B C * + D E + F − J / *`.

## Module 2 — Recursion and queues

### Must know

- Recursion has a base case and a recursive case; each call gets a frame.
- Factorial: `n! = n × (n−1)!`, with `0! = 1`.
- Tower of Hanoi moves n discs in `2^n − 1` moves.
- A queue is FIFO; a linear queue wastes slots after deletion.
- Circular queue: `rear = (rear+1) % MAX`; full when the next rear equals front.
- A deque allows both ends; a priority queue serves highest priority first.
- Applications: CPU scheduling, BFS, buffers.
- Iteration avoids call overhead; recursion uses stack space.

### Definitions to reproduce

> Recursion is when a function calls itself with a smaller input until a base case is reached.

> A queue inserts at the rear and deletes at the front in first-in-first-out order.

## Module 3 — Linked lists

### Must know

- A linked list chains nodes, each holding data and a pointer to the next.
- Types: singly, doubly, circular and circular doubly.
- Insert and delete at the head are O(1); search is O(n).
- Size is dynamic, but there is no random access.
- A doubly linked list stores `prev` and `next`, easing deletion.
- In a circular list the last node points to the head.
- A queue on a list inserts at the rear, deletes at front.
- Concatenation links the first tail to the second head.

### Definitions to reproduce

> A linked list is a linear collection of nodes that need not be contiguous, each holding data and a link to the next node.

> A doubly linked list stores a pointer to both the previous and the next node.

## Module 4 — Trees

### Must know

- A tree has a root, parents, children, leaves, subtrees, degree, level, height.
- A binary tree allows at most two children; a complete tree fills levels left to right.
- Level i holds at most `2^i` nodes; height h holds at most `2^(h+1) − 1`.
- In a BST, left keys are smaller and right keys larger.
- Inorder of a BST is sorted; preorder root-left-right; postorder left-right-root.
- Insertion compares keys and adds a leaf.
- Deletion: leaf, one child, or two children (use the inorder successor).
- Traversals are naturally recursive.

### Definitions to reproduce

> A binary tree is a tree in which every node has at most two children.

> A binary search tree keeps smaller keys left and larger keys right.

### Worked pattern — BST build

Insert 20, 15, 30, 40, 25, 8, 17, 21, 100. 20 is the root; 15 and 30 its children; 8 and 17 left of 15; 25 and 40 under 30; 21 under 25; 100 right of 40. Inorder: 8, 15, 17, 20, 21, 25, 30, 40, 100.

## Module 5 — Hashing and graphs

### Must know

- A hash function maps a key to an index; a collision is two keys in one slot.
- Load factor is `n/m`, for n keys in m slots.
- Open addressing probes linearly, quadratically or by double hashing.
- Chaining keeps a list per slot, so the table never overflows.
- Linear probing clusters entries and slows search.
- A graph G = (V, E) may be directed or weighted.
- Adjacency matrix: O(V²) space; list: O(V + E).
- BFS uses a queue; DFS a stack; Warshall is O(n³).

### Definitions to reproduce

> Hashing computes a record's address directly from its key using a hash function.

> A graph is a collection of vertices and the edges connecting pairs of vertices.

## Last 24 hours

1. Trace infix to postfix for the model paper expression.
2. Dry-run `ABC-D*+E$F+`.
3. Rewrite circular-queue insert and delete; check full and empty.
4. Build the model paper BST and write all three traversals.
5. Work a linear-probing example and count probes.
6. Draw an adjacency matrix and list for a graph.

## Question bank

**Module 1**

1. Define data structures and explain the types with a neat diagram and their operations. [10]
2. Write a C program to evaluate a postfix expression and apply it to `ABC-D*+E$F+` with A=6, B=3, C=2, D=5, E=1, F=7. [10]

**Module 2**

3. Implement a circular queue with insert, delete and display routines. [10]
4. Define recursion and write recursive functions for factorial and Tower of Hanoi. [10]

**Module 3**

5. What is a linked list? Explain its types with diagrams. [10]
6. Write C functions to insert and delete at the beginning and end of a circular linked list. [10]

**Module 4**

7. Define tree, binary tree, level, complete binary tree and degree with examples. [10]
8. Write a C program to build a BST and traverse it for 20, 15, 30, 40, 25, 8, 17, 21, 100. [10]
9. Discuss BST insertion and deletion. [10]

**Module 5**

10. What is a collision? Explain the resolution methods and linear probing with an example. [10]
11. Define a graph and show its adjacency matrix and adjacency list. [10]
12. Write Warshall's algorithm with an example. [10]

*Source: `BCS304_Model Question Paper.pdf`. All parts carry 10 marks in that paper.*
