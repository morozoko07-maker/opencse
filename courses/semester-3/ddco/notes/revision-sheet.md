---
title: Revision sheet
---

# Revision sheet — Digital Design and Computer Organisation

A last-week sheet for BCS302. The first half is circuit minimisation and VHDL, the second processor organisation. Most answers need a truth table, simplified expression, labelled circuit and, where asked, VHDL, so practise in that order.

## Exam pattern

CIE 50 + SEE 50. The model paper is **100 marks in 3 hours: five questions, one per module**, each with two 10-mark parts and an internal OR.

## Module 1 — Boolean algebra, K-map and VHDL

### Must know

- Identities: `A + A' = 1`, `A·A' = 0`, De Morgan's laws.
- Canonical SOP uses minterms `Σm`; POS uses maxterms `ΠM`.
- K-map groups of 1, 2, 4, 8 or 16; edges wrap.
- A prime implicant cannot combine further; an essential one covers a unique 1.
- Don't-care cells may be grouped or ignored.
- Quine–McCluskey tabulates by number of 1s and combines one-bit differences.
- NAND is universal; SOP maps to NAND, POS to NOR.
- VHDL has an `entity` for ports and an `architecture` for behaviour.

### Definitions to reproduce

> A combinational circuit's output depends only on the present inputs.

> A prime implicant is a product term that cannot be combined further.

### Worked pattern — K-map

Plot 1s and don't cares; group adjacent cells in powers of two, allowing wrap-around; each group gives a product of the variables that stay constant. Take essentials, then the fewest groups for the rest.

## Module 2 — Combinational and sequential circuits

### Must know

- Half adder: sum `A ⊕ B`, carry `AB`; a full adder adds carry-in.
- Ripple carry is simple but slow; look-ahead computes generate and propagate in parallel.
- A 2^n-to-1 multiplexer selects one input using n select lines.
- An n-to-2^n decoder asserts one output per code.
- A latch is level-sensitive; a flip-flop is edge-triggered.
- SR latch: `Q+ = S + R'Q`, with `SR = 0`.
- JK removes the invalid state; D is transparent; T toggles.
- VHDL uses concurrent assignment or a `process`.

### Definitions to reproduce

> A multiplexer passes one of several inputs to a single output.

> A flip-flop is a bistable element whose output changes only at a clock edge.

## Module 3 — Basic computer organisation and addressing

### Must know

- A computer has a processor, memory and I/O joined by a bus.
- Registers: PC, IR, MAR, MDR and general-purpose registers.
- The instruction cycle is fetch, decode, execute, then check interrupts.
- Modes: immediate, register, direct, indirect, indexed, base, relative, autoincrement, autodecrement.
- Indexed adds an index register; relative adds the PC.
- Byte addressability and word alignment affect operand fetch.
- Big-endian stores the most significant byte first; little-endian the least.
- Performance is execution time, clock rate, CPI and SPEC rating.

### Definitions to reproduce

> An addressing mode specifies how the operand of an instruction is located.

> Performance is the time a program takes to execute, not clock frequency alone.

## Module 4 — I/O, interrupts, DMA and cache

### Must know

- Memory-mapped I/O uses load/store; I/O-mapped I/O has separate addresses.
- Programmed I/O polls; interrupt-driven I/O lets the device signal.
- An interrupt saves state and branches to the service routine.
- Multiple devices use priority, polling, vectored interrupts or daisy chaining.
- Nesting lets a higher-priority request interrupt a handler.
- DMA moves blocks between memory and a device without per-word CPU copying.
- Bus arbitration is centralised (one arbiter) or distributed.
- Cache mapping is direct, fully associative or set-associative.

### Definitions to reproduce

> An interrupt suspends the current program and transfers control to a service routine.

> DMA transfers data between memory and a device by a controller, without the CPU copying each word.

## Module 5 — Pipelining and control

### Must know

- Pipelining raises throughput, not single-instruction speed.
- Five stages: fetch, decode, fetch operands, execute, write.
- In steady state one instruction completes per clock.
- Cycles are `k + n − 1` for k stages, n instructions.
- Hazards are structural, data and control.
- Forwarding and stalling reduce data hazards.
- A branch flush loses fetched stages.
- `ADD (R3), R1` fetches, adds and writes to R1.

### Definitions to reproduce

> Pipelining overlaps instruction stages so that several instructions are in progress at once.

> A hazard is a condition that stops the next instruction from starting on the next clock.

### Worked pattern — pipeline timing

One row per stage, one column per clock. Start instruction i in stage one at clock i, shift it right each clock, and check against `k + n − 1`.

## Last 24 hours

1. Minimise one SOP and one POS function with don't cares.
2. Write the VHDL skeleton for a gate-level expression.
3. Draw a full adder and an 8:1 multiplexer.
4. Recite ten addressing modes with an example each.
5. Draw the interrupt and DMA transfer paths.
6. Compare the three cache mappings.
7. Draw the five-stage pipeline and the `ADD (R3), R1` sequence.

## Question bank

**Module 1**

1. Apply the K-map to find prime implicants and essential prime implicants, and implement using NAND gates: `f(a,b,c,d) = Σm(0,2,5,7,8,10,13,15) + Σd(1,4,11,14)`. [10]
2. Illustrate the structure of a VHDL program and develop code for `Y = C' + A'CD' + AB'CD'`. [10]

**Module 2**

3. Justify how ripple-carry delay is resolved in a carry look-ahead adder, and implement a full adder in VHDL. [10]
4. Describe an 8:1 multiplexer and implement `f(a,b,c,d) = Σm(0,1,2,5,7,9,12) + Σd(3,4,8)` using it. [10]
5. Illustrate an SR latch with its characteristic equation and implement it in VHDL. [10]

**Module 3**

6. Analyse the basic operational concepts of a computer with operating steps. [10]
7. How does the processor perform input and output? Write a program that reads a line and displays it. [10]
8. Define addressing modes and explain any four with examples. [10]

**Module 4**

9. Illustrate methods for handling multiple interrupt requests from multiple devices. [10]
10. Define DMA bus arbitration and explain the bus arbitration techniques. [10]
11. Analyse the mapping functions of cache memory. [10]

**Module 5**

12. Illustrate the five-stage instruction pipeline with a timing diagram. [10]
13. Analyse the control sequence for `ADD (R3), R1`. [10]
14. Illustrate the single-bus organisation of a computer. [10]

*Sources: `BCS302-DDCO-Model Qustion paper.pdf`; `DDCO Question Bank.pdf`; IA-1 and IA-2 banks. All parts carry 10 marks in the model paper; the banks print no marks.*
