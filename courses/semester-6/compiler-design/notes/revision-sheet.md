---
title: Revision sheet
---

# Revision sheet — Compiler Design

This sheet follows the 2024-25 syllabus (BCS604C) and the two solved IA papers. The syllabus prints the module boundaries; questions come from the IA schemes.

## Exam pattern

The syllabus gives CIE 50 + SEE 50, 40 contact hours and a three-hour SEE. Each IA paper is headed 40 marks, with sub-parts of 3, 4, 5, 6, 7 or 10 marks.

## Module 1 — Language processors and lexical analysis

### Must know

- Analysis covers lexical, syntax and semantic analysis; synthesis covers intermediate code, optimisation and code generation.
- Phase order: lexical, syntax, semantic, intermediate code, optimisation, code generation.
- A token is a class, a lexeme the matched text, a pattern its lexeme rule.
- Double buffering loads two halves and handles a lexeme crossing the boundary; a sentinel removes an end-of-buffer test.

### Definitions to reproduce

> A compiler reads a program in one language and translates it into an equivalent program in another language.

> A lexeme is the sequence of characters matched for a token; the pattern is the rule that describes its form.

## Module 2 — Syntax analysis: top-down parsing

### Must know

- Left recursion makes recursive descent loop. `A → Aα | β` becomes `A → βA'`, `A' → αA' | ε`.
- Left factoring removes a common prefix: `A → αβ1 | αβ2` becomes `A → αA'`, `A' → β1 | β2`.
- FIRST(α) is the set of terminals that begin strings derived from α, plus ε if α derives ε. FOLLOW(A) is the set of terminals that can appear immediately after A.
- A grammar is LL(1) when its predictive table has at most one entry per cell. Use FIRST of each production and FOLLOW of the left side for ε-productions.
- Recursive descent uses one procedure per non-terminal; a non-recursive parser uses a stack, an input pointer and the table.

### Definitions to reproduce

> FIRST(α) is the set of terminals that begin strings derived from α.

> FOLLOW(A) is the set of terminals that can appear immediately to the right of A in some sentential form.

## Module 3 — Syntax analysis: bottom-up parsing

### Must know

- A handle matches a production body and can be reduced to its left side.
- Shift-reduce parsing uses a stack and four actions: shift, reduce, accept, error. Conflicts are shift-reduce or reduce-reduce.
- An LR(0) item is a production with a dot marking the current position. CLOSURE adds items for the symbol after the dot; GOTO moves the dot over a grammar symbol.
- SLR(1) uses FOLLOW sets to choose reductions. LR(1) items carry a lookahead. LALR(1) merges states with the same LR(0) core, which can create a conflict that LR(1) avoids.
- Yacc builds LALR(1) tables from a grammar and reports conflicts.

### Definitions to reproduce

> A handle is a substring that matches the right side of a production and whose reduction represents one step in a rightmost derivation.

> An LR(1) item is a production with a dot and a lookahead terminal.

## Module 4 — Syntax-directed translation and intermediate code

### Must know

- A syntax-directed definition attaches attributes and semantic rules to productions. Synthesised attributes flow from children to parent; inherited attributes flow from parent or siblings.
- An annotated parse tree shows attribute values; a dependency graph shows which values must be computed first.
- S-attributed definitions use only synthesised attributes and can be evaluated bottom-up. L-attributed definitions allow limited inherited attributes.
- Three-address code uses at most one operator per instruction, with temporaries: `x = y op z`, `x = op y`, `x = y`, jumps.
- A DAG removes common subexpressions by sharing nodes. Backpatching fills jump targets after the surrounding code is emitted.

### Definitions to reproduce

> A syntax-directed definition is a context-free grammar with attributes and semantic rules attached to productions.

> Three-address code is an intermediate representation in which each instruction has at most three operands.

## Module 5 — Code generation

### Must know

- Issues: input representation, target architecture, instruction selection, register allocation, storage management, evaluation order, control flow and phase integration.
- A basic block is a maximal straight-line sequence with one entry and one exit. Leaders are the first statement, jump targets and statements after a jump.
- A flow graph has basic blocks as nodes and control-flow edges as arcs.
- Basic-block optimisation includes common-subexpression elimination, dead-code elimination, constant folding and strength reduction.
- A simple code generator walks the three-address code and spills registers when they run out.

### Definitions to reproduce

> A basic block is a sequence of consecutive statements in which control enters at the beginning and leaves at the end without halt or branch.

> Register allocation decides which values stay in registers and which are stored in memory.

## Last 24 hours

1. Draw the six phases for `position = initial + rate * 60`.
2. Eliminate left recursion and left-factor one grammar.
3. Build FIRST, FOLLOW and the LL(1) table for the expression grammar.
4. Convert an expression to three-address code through a DAG.

## Question bank

**Module 1**

1. Explain the phases of a compiler and show the transition for `position = initial + rate * 60`, indicating each phase's output. [7]
2. The lexical analyser is slow because it reads characters one at a time. Identify the technique that addresses this, show why character-by-character reading is inefficient, and write the algorithm. [10]

**Module 2**

3. Define FIRST and FOLLOW, build both sets and the LL(1) table for the expression grammar, and decide whether it is LL(1). [10]

**Module 3**

4. Explain the shift-reduce parser, demonstrate shift-reduce and reduce-reduce conflicts, and suggest resolutions. [7]
5. Construct the SLR(1) item sets, GOTO and parsing table for `S → SS + | SS * | a`, test for conflicts and simulate `a a + a *`. [10]

**Module 4**

6. Explain inherited and synthesised attributes, define an SDD for a calculator, and draw the annotated tree and dependency graph for `4 + 6 * 2n`. [10]

**Module 5**

7. Identify the basic blocks in a short if-else program, draw the flow graph, and explain how it helps optimisation. [10]
8. What are the key issues in the design of a code generator? Explain each briefly. [10]

*Source: `CD IA1 Scheme 2024-25 May 2025.pdf` for questions 1–3; `CD IA2 Scheme 2024-25 June 2025.pdf` for questions 4–8. Marks are those printed in the schemes. The two `VTU paper/Aug-2022` files are scans and were not used.*
