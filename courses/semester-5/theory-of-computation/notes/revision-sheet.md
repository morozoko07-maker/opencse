---
title: Revision sheet
---

# Revision sheet — Theory of Computation

The notes divide the course into five modules: finite automata, regular languages, context-free grammars and pushdown automata, normal forms, and Turing machines with decidability. The previous-year bank is typed and gives marks, so practise the standard constructions.

## Exam pattern

The IA schemes show 40 marks in 1 hour 30 minutes with four full questions, split into 5 + 5 or 4 + 6 parts. The IA-1 scheme is a poor scan; the IA-2 scheme and the previous-year bank are readable.

## Module 1 — Finite automata

### Must know

- An alphabet is a finite set of symbols; a string is a finite sequence; a language is a set of strings.
- A DFA is a five-tuple (Q, Σ, δ, q0, F) with exactly one transition per state–symbol pair.
- An NFA may have zero, one or many transitions; an ε-NFA allows empty-string moves.
- Subset construction converts an NFA to a DFA using ε-closures.
- DFA minimisation uses table filling: mark pairs with different acceptance, then propagate distinguishability.

### Definitions to reproduce

**DFA** — a finite automaton with a single deterministic transition for every state and input symbol.

**ε-closure** — the set of states reachable from a state by zero or more ε-transitions.

## Module 2 — Regular expressions and regular-language properties

### Must know

- A regular expression is built from ∅, ε, symbols and union, concatenation and Kleene star.
- Every regular expression has an equivalent ε-NFA (Thompson construction); every DFA has an equivalent regular expression (state elimination or Arden's theorem).
- The pumping lemma proves non-regularity: assume regularity, choose a string, pump it and derive a contradiction.
- Typical non-regular languages: {aⁿbⁿ}, {wwᴿ}, palindromes and {aⁿ | n is prime}.

### Definitions to reproduce

**Regular expression** — an expression denoting a regular language using union, concatenation and Kleene star.

**Pumping lemma** — every regular language has a pumping length p such that any string of length at least p splits into xyz, with |xy| ≤ p, |y| > 0, and xyⁱz in L for all i ≥ 0.

## Module 3 — Context-free grammars and pushdown automata

### Must know

- A CFG is a four-tuple (V, T, P, S); productions replace one variable by a string of variables and terminals.
- Derivations are leftmost or rightmost; a parse tree records the derivation.
- A grammar is ambiguous if a string has two distinct parse trees or leftmost derivations.
- A PDA is a seven-tuple (Q, Σ, Γ, δ, q0, Z0, F) with an input tape, a stack and a finite control.
- A PDA accepts by final state or empty stack; the two modes are equivalent. CFGs and PDAs define the same class.

### Definitions to reproduce

**Context-free grammar** — a grammar whose productions have a single variable on the left.

**Ambiguous grammar** — a grammar with at least one string that has two different parse trees.

## Module 4 — Simplification and normal forms

### Must know

- Useless symbols are non-generating or unreachable; remove both.
- Nullable variables derive ε. Eliminate ε-productions, then unit productions, then useless symbols.
- Unit productions have the form A → B; replace them with the productions of B.
- CNF allows A → BC or A → a, with no ε except possibly S → ε.
- The CFL pumping lemma proves that languages such as {aⁿbⁿcⁿ} are not context-free.

### Definitions to reproduce

**CNF** — Chomsky normal form; every production is A → BC or A → a.

**Nullable variable** — a variable from which ε can be derived.

## Module 5 — Turing machines and decidability

### Must know

- A Turing machine is a seven-tuple (Q, Σ, Γ, δ, q0, qaccept, qreject) with an infinite tape and a read/write head.
- An instantaneous description records the state, tape contents and head position.
- Multi-tape and non-deterministic TMs are equivalent to the basic TM.
- A language is recursive if a TM decides it; it is recursively enumerable if a TM accepts it.
- The halting problem is undecidable. If both L and its complement are RE, then L is recursive.

### Definitions to reproduce

**Recursive language** — a language for which a TM always halts with yes or no.

**Recursively enumerable language** — a language accepted by a TM that may loop on strings not in it.

### Worked pattern

For L = {0ⁿ1ⁿ | n ≥ 1}, repeatedly replace the leftmost 0 by X and the corresponding 1 by Y, moving right and left. If the counts match, the tape ends with X…XY…Y and the machine accepts; a mismatch rejects.

## Last 24 hours

- Practise NFA → DFA and DFA minimisation on small tables.
- Write the pumping-lemma proof for {aⁿbⁿ} from memory.
- Convert one grammar through ε-removal, unit-removal and CNF.
- Draw a TM for 0ⁿ1ⁿ and trace its ID.

## Question bank

**Module 1**

1. Write the DFA for the set of all strings over {a, b} ending with abb. (8 marks, Jan 2013)
2. What are the differences between DFA, NFA and ε-NFA? (4 marks, May 2010)
3. Design a DFA to accept the binary number which is divisible by 5. (6 marks, Dec 2009)

**Module 2**

4. State and prove pumping lemma for regular languages. Show that L = {0ⁿ | n is prime} is not regular. (10 marks, July 2011)
5. Minimize the given DFA using the table filling algorithm. (10 marks, Jun 2010)

**Module 3**

6. Show that the following grammar is ambiguous: S → iCtS | iCtSeS | a, C → b. (7 marks, Jan 2014)
7. Define PDA. Design PDA for L = {wCwᴿ | w ∈ (a + b)*}. Show the IDs for abcba and draw the transition diagram. (10 marks, Dec 2012)

**Module 4**

8. Remove useless symbols from the given grammar. (8 marks, Dec 2018)
9. Define CNF. Convert E → E + E | E * E | (E) | id to CNF. (8 marks, Dec 2017)
10. State and prove pumping lemma for context-free languages. (8 marks, Jan 2010)

**Module 5**

11. Design a Turing machine to add two numbers, with input 0ᵐ10ⁿ and output 0ᵐ⁺ⁿ. (12 marks, Jun 2018)
12. Write a detailed note on the halting problem of a Turing machine. (8 marks, Jul 2013)

*Source: `material/TOC/TOC PEVIOUS YEAR QUESTIONS.pdf`. Marks and years are those printed in the bank. The IA-1 answer scheme is a poor scan, so questions were taken from the typed bank instead.*
