---
title: Object Oriented Programming with C++
code: BCS306B
semester: 3
credits: 3
cie: 50
see: 50
summary: Classes, objects, constructors, dynamic memory and operator overloading — with 19 compiled programs and their real output.
---

# Object Oriented Programming with C++

Notes for the C++ paper, written around what the examiner actually awards marks
for: a definition **plus** an example, and a program **plus** its output.

## Marking pattern

| Question type | What earns the marks |
|---|---|
| 2 marks | Exact definition + one example line. No stories. |
| 5 marks | Definition → syntax → short program → 2–3 differences/advantages. |
| 10 marks | Definition → features in points → labelled program → output → conclusion. |

**Golden rule:** a program without its output, or a definition without an
example, loses marks. Every long answer in the notes follows that shape.

## Notes

- [Modules 1 & 2 — complete exam notes](cpp-modules-1-2.html) — classes, objects,
  constructors, destructors, dynamic memory, `this` pointer, static members,
  friend functions, operator overloading.

All programs in the notes were compiled with `g++ -std=c++17 -Wall -Wextra` and
run; the outputs shown are real.

## Terminology the slides sometimes get wrong

- `cout << x` — `<<` is the **insertion (output)** operator. `cin >> x` — `>>` is
  the **extraction (input)** operator.
- A constructor **initialises** an object. Memory is allocated by the object
  definition or `new`, not by the constructor.
- Headers are `<iostream>`, not `<iostream.h>`. `main` returns `int`, not `void`.
