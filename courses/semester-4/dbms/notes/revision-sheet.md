---
title: Revision sheet
---

# Revision sheet — Database Management Systems

This sheet covers all five units in the README table. The existing exam guide explains the introduction and SQL sections in depth; this is a shorter pass over the whole paper, with the definitions and question shapes worth carrying into the hall.

## Exam pattern

The README gives CIE 50 + SEE 50. The solved CIE-I paper in the existing guide is headed 40 marks across eight questions; its printed marks do not add up, so confirm the split against your handout.

## Module 1 — Introduction and architecture

### Must know

- Data are recorded facts; a database is related data; a DBMS manages both.
- A database system is the DBMS plus the data and applications.
- Characteristics: self-describing catalog, program–data independence, abstraction, multiple views, sharing.
- Actors: DBA, designer, four end-user types; workers behind the scene.
- Three levels: external views, conceptual schema, internal storage; mappings join them.
- Logical independence changes the conceptual schema; physical independence changes the internal schema.
- DDL defines the schema, DML manipulates data, SDL storage, VDL views.
- DBMS components: DDL compiler, parser and optimiser, runtime processor, storage manager, catalog.
- Query processing: parser, translator, optimiser, execution engine, storage manager.

### Definitions to reproduce

> A DBMS is software that defines, constructs, manipulates and shares a database.

> Logical data independence changes the conceptual schema without changing external views or programs.

## Module 2 — Entity–relationship model

### Must know

- Entity, attribute, entity set, key, domain; an entity is a mini-world object.
- Attributes may be simple or composite, single or multi-valued, stored or derived.
- A relationship has degree, role and constraints; recursive ones use one entity type twice.
- Cardinality is the maximum: 1:1, 1:N, M:N. Participation is the minimum: total or partial.
- A weak entity has no key of its own; a partial key plus the owner identifies it.
- Notation: rectangle entity, diamond relationship, oval attribute, double rectangle weak entity.
- Generalisation combines entity types; specialisation splits one; disjoint or overlapping, total or partial.
- Mapping: strong entity to table; 1:N puts the key on the N side; M:N needs a new table with both keys.

### Definitions to reproduce

> A weak entity has no key of its own; a partial key plus its owner identifies it.

> Cardinality ratio specifies the maximum number of relationship instances in which an entity can participate.

## Module 3 — Relational model, algebra and SQL

### Must know

- A relation is a set of tuples; degree counts attributes, cardinality counts tuples.
- Superkey identifies tuples; a candidate key is minimal; the primary key is the chosen candidate.
- A foreign key references a primary key and enforces referential integrity.
- Constraints: domain, key, entity integrity (no NULL primary key), referential, CHECK.
- Relational algebra: σ select, π project, ρ rename, ∪, ∩, −, ×, ⋈ join, ÷ division.
- Joins: theta, equi, natural, outer and self join.
- SQL groups: DDL, DML, DCL, TCL; SELECT evaluation is FROM, WHERE, GROUP BY, HAVING, SELECT, ORDER BY.
- WHERE filters rows; HAVING filters groups; aggregates ignore NULL except COUNT(*).
- A view is a stored query; it gives security and logical independence but may not be updatable.

### Definitions to reproduce

> A candidate key is a minimal set of attributes that uniquely identifies each tuple.

> A foreign key references a primary key in the same or another relation, or is NULL.

## Module 4 — Normalisation

### Must know

- Poor design causes redundancy, three anomaly types and NULL problems.
- A functional dependency X → Y means each X value determines one Y value.
- Armstrong's axioms: reflexivity, augmentation, transitivity; derive union, decomposition and pseudotransitivity.
- 1NF: atomic attributes. 2NF: no partial dependency on part of a candidate key.
- 3NF: no transitive dependency; every determinant is a superkey or the dependent is prime.
- BCNF: every non-trivial determinant is a superkey.
- 4NF removes multivalued dependencies; 5NF removes join dependencies.
- A good decomposition is lossless-join and dependency-preserving.

### Definitions to reproduce

> A relation is in BCNF if every non-trivial determinant is a superkey.

> A lossless-join decomposition reconstructs the original relation without spurious tuples.

## Module 5 — Transactions, concurrency and recovery

### Must know

- A transaction is a logical unit of work: read, write, commit or abort.
- ACID: atomicity, consistency, isolation, durability.
- States: active, partially committed, committed, failed, aborted; the log records every change.
- A schedule interleaves operations; a serial schedule runs transactions one after another.
- Conflict serialisable schedules have a precedence graph with no cycle.
- Recoverable schedules commit after their read-from transactions; cascadeless schedules avoid dirty reads.
- 2PL has a growing and a shrinking phase; strict 2PL holds exclusive locks until commit.
- Recovery uses UNDO/REDO and checkpoints; deadlock is handled by prevention, detection or timeout.

### Definitions to reproduce

> A transaction is a sequence of operations forming one logical unit of work.

> A schedule is conflict serialisable if swapping non-conflicting operations yields a serial schedule.

## Last 24 hours

1. Draw the three-schema architecture and label both mappings.
2. Draw the COMPANY ER diagram and convert it to tables.
3. Write the six COMPANY queries from the existing guide without looking.
4. Test one relation for 2NF, 3NF and BCNF, showing every candidate key.
5. Check one schedule for conflict serialisability with a precedence graph.

## Question bank

**Module 1**

1. Draw and analyse the components or modules of a DBMS and their interactions.
2. Analyse the three-schema architecture and give your thoughts on every layer.
3. Explain the characteristics of the database approach. [10]

**Module 2**

4. Draw an ER diagram for a library database and mark the keys appropriately.
5. Apply the concepts of entity types, entity sets, attributes, roles and structural constraints to a database design.

**Module 3**

6. Explain candidate key, super key, foreign key, prime attribute and key constraint with examples.
7. Describe the binary relational operation JOIN and its types.
8. Explain views with examples.

**Module 4**

9. Explain 1NF, 2NF, 3NF and BCNF with examples.

**Module 5**

10. Explain the state transition diagram of a transaction in DBMS.
11. Explain the ACID properties of transactions.
12. Explain the two-phase locking mechanism.

*Source: `DBMS_question_bank IA-1.pdf`, `imp ques ans ans.pdf`, and the solved CIE-I paper in `DBMS_Exam_Guide.html`. The 10-mark question is from that solved paper; the rest carry no printed marks.*
