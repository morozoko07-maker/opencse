---
title: Revision sheet
---

# Revision sheet — Discrete Mathematical Structures

The model paper supplies marks and question shapes; the bank supplies extra practice. Work each proof before checking the source line.

## Exam pattern

The model paper confirms the SEE shape: 100 marks, 3 hours, five full questions, one from each module. Each full question is 20 marks: 7 + 7 + 6, with an OR. The README gives CIE 50 + SEE 50.

## Module 1 — Propositional logic and quantifiers

### Must know

- A proposition is declarative and is either true or false, not both.
- Connectives: ¬, ∧, ∨, →, ↔; negation binds tightest.
- A tautology is true for every assignment; a contradiction is never true.
- Converse q → p, inverse ¬p → ¬q, contrapositive ¬q → ¬p; only the contrapositive is equivalent.
- An argument is valid when no row makes all premises true and the conclusion false.
- Rules: modus ponens, modus tollens, hypothetical syllogism, disjunctive syllogism, resolution.
- Negate quantifiers by swapping ∀ and ∃ and negating the predicate.
- Proof methods: direct, contrapositive and contradiction.

### Definitions to reproduce

> A proposition is a declarative statement that is either true or false, but not both.

> A tautology is a compound proposition that is true under every truth assignment.

## Module 2 — Relations, equivalence and partial orders

### Must know

- A relation from A to B is a subset of A × B.
- Reflexive: (a, a) ∈ R for all a. Symmetric: (a, b) implies (b, a).
- Antisymmetric: (a, b) and (b, a) imply a = b. Transitive: (a, b) and (b, c) imply (a, c).
- Equivalence = reflexive + symmetric + transitive; its classes partition A.
- Partial order = reflexive + antisymmetric + transitive; (A, R) is a poset.
- A Hasse diagram drops loops and transitive edges and puts larger elements above smaller ones.
- Bounds: upper, lower, least upper, greatest lower; maximal and minimal need not be unique.
- A relation has a matrix and a digraph; degrees are read from the matrix.

### Definitions to reproduce

> An equivalence relation on A is reflexive, symmetric and transitive.

> A partial order on A is reflexive, antisymmetric and transitive.

## Module 3 — Functions, pigeonhole and counting arguments

### Must know

- f: A → B assigns exactly one element of B to each element of A.
- Domain is A, codomain is B, range is the set of actual images.
- Injective: f(a) = f(b) implies a = b. Surjective: every b has a preimage. Bijective: both.
- Composition is associative; (g ∘ f)⁻¹ = f⁻¹ ∘ g⁻¹ when both are invertible.
- A function is invertible exactly when it is bijective.
- For |A| = m and |B| = n: nᵐ functions and 2^(mn) relations.
- Pigeonhole: n items in m boxes puts at least ⌈n/m⌉ in one box.
- The generalised principle applies when each box has a capacity.

### Definitions to reproduce

> A function f: A → B assigns to each element of A exactly one element of B.

> A function is injective if distinct domain elements always have distinct images.

## Module 4 — Mathematical induction and recurrence relations

### Must know

- Induction: prove P(1), assume P(k), then prove P(k + 1).
- Strong induction assumes P(1) through P(k).
- A recurrence defines a term from earlier terms; its order is the number used.
- A linear homogeneous recurrence is solved by its characteristic equation.
- Distinct roots r₁, r₂ give A·r₁ⁿ + B·r₂ⁿ; a repeated root r gives (A + Bn)rⁿ.
- A non-homogeneous recurrence adds a particular solution.
- Recursive definitions cover factorial, Fibonacci, Ackermann and Hanoi.
- Hanoi: M(n) = 2M(n − 1) + 1, M(1) = 1, so M(n) = 2ⁿ − 1.

### Definitions to reproduce

> A recurrence relation expresses each term as a function of earlier terms.

> Mathematical induction proves a statement for all positive integers by a base case and an inductive step.

## Module 5 — Permutations, combinations and inclusion–exclusion

### Must know

- Sum rule: add disjoint cases. Product rule: multiply independent choices.
- ⁿPᵣ = n!/(n − r)! and ⁿCᵣ = n!/(r!(n − r)!).
- Permutations with repeated letters divide by the factorial of each repeat count.
- |A ∪ B| = |A| + |B| − |A ∩ B|, with a three-set form.
- Dₙ = n!(1 − 1/1! + 1/2! − … + (−1)ⁿ/n!); D₄ = 9.
- Stars and bars: n identical items into k boxes gives C(n + k − 1, k − 1).
- If every box is non-empty, the count is C(n − 1, k − 1).
- Forbidden patterns are handled by inclusion–exclusion over the patterns.

### Definitions to reproduce

> A permutation is an ordered arrangement of objects.

> A derangement leaves no object in its original position.

## Last 24 hours

1. Reproduce the truth table for {(p ∨ q) → r} ↔ {¬r → ¬(p ∨ q)}.
2. Draw the Hasse diagram for the positive divisors of 36.
3. Prove the mod-5 relation is an equivalence relation and list its classes.
4. Do one induction proof and one recurrence with repeated roots.
5. Do one pigeonhole and one stars-and-bars problem.

## Question bank

**Module 1**

1. Determine whether {(p ∨ q) → r} ↔ {¬r → ¬(p ∨ q)} is a tautology using a truth table. [7]
2. Define converse, inverse and contrapositive, and find them for ∀x, (x > 3) → (x² > 9). [6]

**Module 2**

3. For A = {1, 2, …, 11} and xRy iff x − y is a multiple of 5, verify that R is an equivalence relation. [7]
4. Draw the Hasse diagram representing the positive divisors of 36. [7]

**Module 3**

5. Shirts 1 to 20 are worn by 20 students. A team of 3 has code equal to the sum of its numbers. Show that any 8 students contain two teams with the same code. [7]

**Module 4**

6. Prove by induction that 1 + 2 + … + n = n(n + 1)/2 for all n ≥ 1. [7]
7. Virus-affected files start at 1000 and increase 250% every 2 hours. Use a recurrence to find the number after one day. [7]

**Module 5**

8. Find the permutations of MASSASAUGA; how many have all four As together, and how many begin with S? [7]

*Source: `7_Model Question Paper_DMS_BCS405A.pdf` and `5_DMS_BCS405A_Question Bank.pdf`. Marks are from the model paper.*
