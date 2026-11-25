---
title: Revision sheet
---

# Revision sheet — Artificial Intelligence

This sheet follows the five modules of the January 2025 question bank. Learn the definitions, then practise the translations and calculations that recur.

## Module 1 — Introduction and intelligent agents

### Must know

- Four views of AI: thinking humanly (cognitive modelling), acting humanly (Turing Test), thinking rationally (laws of thought) and acting rationally (rational agent).
- The Turing Test needs natural language processing, knowledge representation, automated reasoning and machine learning; the Total Turing Test adds vision and robotics.
- Agent types: simple reflex, model-based reflex, goal-based, utility-based and learning.
- Environment properties: observable, deterministic, episodic, static, discrete and single-agent, or their opposites.

### Definitions to reproduce

**Agent** — anything that perceives its environment through sensors and acts on it through actuators.

**Rational agent** — one that acts to achieve the best outcome, or the best expected outcome under uncertainty.

**PEAS** — Performance measure, Environment, Actuators, Sensors; the checklist for a task environment.

### Worked pattern

For an automatic taxi: performance is safety, time, comfort, legality and profit; environment is roads, traffic, pedestrians and weather; actuators are steering, accelerator, brake and horn; sensors are cameras, lidar, speedometer and GPS. It is partially observable, stochastic, sequential, dynamic, continuous and multi-agent.

## Module 2 — Problem solving and uninformed search

### Must know

- A problem has five parts: initial state, actions, transition model, goal test and path cost. These define the state space.
- BFS: complete, optimal for equal step costs, time and space O(b^d).
- DFS: not complete in infinite spaces, not optimal, time O(b^m), space O(bm).
- Uniform-cost search expands the lowest g(n); complete and optimal for non-negative costs.

### Definitions to reproduce

**Completeness** — the guarantee of finding a solution if one exists.

**Optimality** — the guarantee of finding the lowest-cost solution.

**State space** — all states reachable from the initial state by any sequence of actions.

### Worked pattern

In the vacuum world, two squares with two dirt states each give 2 × 2² = 8 states. Actions are Left, Right and Suck; the goal test checks that both squares are clean; each step costs 1.

## Module 3 — Informed search, local search and logical agents

### Must know

- h(n) estimates the cost from n to a goal; h(goal) = 0. Greedy best-first orders by h and is neither complete nor optimal.
- A* uses f(n) = g(n) + h(n); complete and optimal if h is admissible, more efficient if h is consistent.
- A knowledge-based agent uses TELL and ASK. Entailment, inference, soundness and completeness are the key ideas.
- Propositional logic: atoms, five connectives, truth tables, equivalence, validity and satisfiability. Resolution works on CNF; Horn clauses support chaining.

### Definitions to reproduce

**Heuristic function** — a non-negative estimate of the cost from a node to the nearest goal.

**Admissible heuristic** — one that never overestimates the true remaining cost.

### Worked pattern

In A*, tabulate g, h and f, expand the smallest f, and stop when the goal leaves the frontier. On the Romania map, f(Arad) = 0 + 366 and Bucharest has h = 0.

## Module 4 — First-order logic and inference

### Must know

- FOL adds objects, relations, functions and quantifiers to propositional logic.
- A term names an object; a predicate returns true or false.
- Forward chaining is data-driven; backward chaining is goal-driven; both suit Horn clauses.
- CNF conversion: remove implications and biconditionals, move negations inwards, standardise variables, Skolemise, drop universals and distribute ∨ over ∧.

### Definitions to reproduce

**Term** — a constant, variable or function applied to terms.

**Unification** — finding a substitution that makes two atomic sentences identical.

**CNF** — a conjunction of clauses, each clause a disjunction of literals.

### Worked pattern

"Every student loves at least one course" becomes ∀x (Student(x) → ∃y (Course(y) ∧ Loves(x, y))). "Some dogs are pets" becomes ∃x (Dog(x) ∧ Pet(x)). Keep quantifier order: swapping ∀ and ∃ changes the meaning.

## Module 5 — Quantifying uncertainty

### Must know

- Probability axioms: 0 ≤ P(ω) ≤ 1 and the sample-point probabilities sum to 1.
- Marginalisation sums out a variable; normalisation makes the remaining values sum to 1.
- Product rule: P(a ∧ b) = P(a | b)P(b). Independence: P(a ∧ b) = P(a)P(b).
- Bayes' rule: P(a | b) = P(b | a)P(a) / P(b).

### Definitions to reproduce

**Sample space** — the set of all possible worlds, Ω.

**Random variable** — a function from sample points to a value.

**Marginalisation** — obtaining a probability by summing the joint distribution over an unwanted variable.

### Worked pattern

Meningitis causes a stiff neck 70% of the time; P(meningitis) = 1/50,000 and P(stiff neck) = 0.01. Then P(meningitis | stiff neck) = (0.7 × 0.00002) / 0.01 = 0.0014, or about 1 in 714.

## Last 24 hours

- Rehearse the four AI views, PEAS and the agent types.
- Write the five-part problem formulation and the BFS, DFS, UCS and A* properties from memory.
- Practise one FOL translation, one unification and the meningitis calculation.

## Question bank

**Module 1**

1. Define an intelligent agent. Make use of Architectures in AI to explain different types of agents.
2. Choose the PEAS for the task environment of Automatic Taxi Driver. Summarize the properties of this task environment.
3. Choose Performance measure, Environment, Actuators and Sensors for Satellite Image analysis system.

**Module 2**

4. List all uninformed search strategies. Write the differences between them.
5. What is Uniform-cost search? write an algorithm/function for the same.

**Module 3**

6. Apply the Greedy Best first Search (or A* Search) strategy to solve the Romania Problem and find the cost of the solution path from Arad to Bucharest.
7. Distinguish backward and forward chaining with examples.

**Module 4**

8. Compare the differences between terms and predicate in First order logic.
9. How would you represent the following statements in FOL? (a) Every student loves at least one course. (b) If a person is a professor, then they teach a course. (c) Some dogs are pets.
10. Prove that Colonel West is a criminal by using forward-chaining and backward chaining algorithm.

**Module 5**

11. Consider two medical tests, A and B, for a virus. Which test returning positive is more indicative of someone really carrying the virus? Justify mathematically.
12. Apply Bayes' rule to the meningitis and stiff neck scenario.

*Source: `material/AI/question bank .pdf` (BCS505B Question Bank, January 2025). The IA papers in the folder are scans and gave no usable text, so no questions were taken from them.*
