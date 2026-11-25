# DSA (BCS304) — Complete Study Guide

These notes cover all three PDFs in your Downloads folder, page by page:

| File | Covers |
|---|---|
| `01-Module-1-Part-A.md` | Introduction, classification, operations, pointers, memory allocation, arrays, structures |
| `02-Module-1-Part-B.md` | Stacks, system stack, expressions, infix/postfix/prefix, multiple stacks |
| `03-Module-2.md` | Recursion, queues, circular queues, deques, priority queues |

## How each chapter is written

- **Plain-English idea** — what the thing actually is, without jargon.
- **Exam definition** — the sentence you can reproduce in an answer sheet.
- **Worked example / trace** — exactly how the algorithm moves step by step.
- **Exam points** — the small facts that become 1–2 mark questions.
- **Check yourself** — a few questions with answers, placed right after the topic.
- **Question bank** — at the end of each file, exam-style questions.

## Suggested study order

1. Read a section once without memorising.
2. Close the file and explain it out loud in your own words.
3. Answer the "Check yourself" questions.
4. Only then look at the code/trace.
5. At the end, do the question bank without looking.

## The big picture (why these topics are in this order)

```
Data → how to store it → arrays (contiguous) / linked lists (links)
     → how to access it → pointers, addresses
     → how to grow it   → static vs dynamic memory
     → how to group it  → structures
     → how to process it→ stack (LIFO) / queue (FIFO)
     → how to repeat    → recursion
```

Every later data structure is built from these basics. If pointers and arrays are shaky, linked lists, trees and graphs will feel hard — so Part A is worth slowing down for.

## Formula / fact sheet (whole subject so far)

| Thing | Formula / fact |
|---|---|
| Array length | `UB - LB + 1` |
| Address of `a[i]` | `base + i * sizeof(element)` |
| Pointer arithmetic | `a + i = a + i * sizeof(one element)` |
| Stack | LIFO; push/pop at `top` |
| Queue | FIFO; insert at `rear`, delete at `front` |
| Circular queue next position | `(index + 1) % size` |
| Hanoi moves | `2^n - 1` |
| Factorial | `n! = n * (n-1)!`, `0! = 1` |
| Fibonacci | `F(n) = F(n-1) + F(n-2)` |
| GCD (subtraction) | `GCD(m,n) = m` if `m==n`; else subtract smaller from larger |
| Postfix evaluation | pop 2, apply operator, push result |
| Infix → postfix | pop while stack precedence > input precedence |
