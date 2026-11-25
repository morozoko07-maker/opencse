---
title: Revision sheet
---

# Revision sheet — Microcontrollers

The banks are module-wise, so this sheet follows their order. Draw the register and exception diagrams from memory.

## Exam pattern

The README gives CIE 50 + SEE 50. No paper with usable text is present; the files are IA banks, not a SEE paper.

## Module 1 — ARM architecture and embedded systems

### Must know

- An embedded system is a dedicated computer with a processor, memory, peripherals and software.
- RISC favours simple fixed-length instructions; CISC favours complex variable-length instructions.
- ARM design rules: few instruction classes, pipelines, a large register set, load–store architecture.
- Hardware parts: ARM core, controllers, peripherals and bus; AMBA defines AHB, ASB and APB.
- Software stack: initialisation code, operating system, device drivers, application.
- Registers: R0–R12 general, R13 stack pointer, R14 link register, R15 program counter.
- CPSR holds N, Z, C, V flags, I and F masks, the Thumb bit and the mode bits.
- The ARM7 pipeline has fetch, decode and execute stages.
- Seven modes: user, FIQ, IRQ, supervisor, abort, undefined and system.

### Definitions to reproduce

> RISC uses a small set of simple, fixed-length instructions, usually one per cycle.

> The CPSR is a 32-bit register holding condition flags, interrupt masks, state and mode.

## Module 2 — ARM instruction set

### Must know

- The barrel shifter shifts or rotates one operand before it reaches the ALU.
- Shifts: LSL, LSR, ASR, ROR and RRX.
- Data processing: MOV, MVN, ADD, SUB, AND, ORR, EOR, BIC, CMP, TST.
- Multiply: MUL, MLA, UMULL, UMLAL, SMULL and SMLAL.
- Branch: B, BL and BX; most instructions can be conditional.
- Load/store: LDR and STR with pre- or post-indexing and optional writeback.
- LDM and STM move multiple registers; stacks are full or empty, ascending or descending.
- SWI enters supervisor mode for an OS call; SWP performs an atomic swap.

### Definitions to reproduce

> The barrel shifter shifts or rotates a 32-bit operand within the instruction cycle.

> A load–store architecture acts on registers and moves data with separate load and store instructions.

## Module 3 — C programming for ARM

### Must know

- A C loop compiles to a compare, a conditional branch and a counter update.
- A decrementing loop that tests for zero saves an instruction per iteration.
- Loop unrolling repeats the body to cut branch overhead but increases code size.
- Use 32-bit int where possible; char and short may need extra masking instructions.
- ATPCS passes the first four arguments in R0–R3 and the rest on the stack.
- A 32-bit result returns in R0; a 64-bit result returns in R0–R1.
- The callee preserves R4–R11, SP and LR when it uses them.
- A checksum routine accumulates bytes or halfwords and returns a short.

### Definitions to reproduce

> ATPCS defines how arguments, return values and callee-saved registers pass between functions.

> Loop unrolling is the compiler transformation that replicates the loop body to reduce the number of branch instructions.

## Module 4 — Firmware and exception handling

### Must know

- A boot loader initialises hardware, runs diagnostics and loads the application image.
- Exceptions: reset, undefined instruction, SWI, prefetch abort, data abort, IRQ and FIQ.
- Reset starts in supervisor mode; IRQ and FIQ have their own banked registers.
- On an exception the CPSR is copied to SPSR, the mode changes and the return address goes to LR.
- The vector table holds branch instructions to the handlers.
- FIQ has higher priority than IRQ; the I and F bits mask the two interrupts.
- Interrupt latency is the time from the request to the first handler instruction.
- Nested interrupts need separate stacks and careful LR saving.

### Definitions to reproduce

> An exception changes normal execution and transfers control to a handler via the vector table.

> Interrupt latency is the delay between an interrupt request and the execution of the first instruction of its handler.

## Module 5 — Memory and cache

### Must know

- A cache is a small fast memory that holds recently used lines from main memory.
- Direct mapped: each address maps to one line. Set associative: each address maps to one set of n lines.
- Address bits: offset selects a word in the line, index selects the set, tag identifies the line.
- Write-through writes memory immediately; write-back writes only when the line is evicted.
- A write buffer hides memory latency; replacement policies are LRU, round-robin and random.
- Von Neumann uses one bus for instructions and data; Harvard uses separate buses.
- A virtual cache is indexed before translation; a physical cache is indexed after translation.
- Thrashing occurs when two hot lines keep evicting each other.
- Average memory access time = hit time + miss rate × miss penalty.

### Definitions to reproduce

> A cache is a small fast memory holding recently used main-memory lines.

> Thrashing is repeated conflict eviction of two blocks mapped to the same line.

## Last 24 hours

1. Draw the ARM register file and label R13, R14, R15 and CPSR.
2. Reproduce the RISC and CISC comparison table.
3. Trace an LDR with pre- and post-indexing and writeback.
4. Write the ATPCS argument and return conventions.
5. List the exception types with their modes and LR values.

## Question bank

**Module 1**

1. What do you mean by RISC architecture?
2. Differentiate CISC and RISC architecture.
3. Explain the current program status register with a neat diagram.

**Module 2**

4. What is a barrel shifter and which operations does it support?
5. Explain with an example how MLA, MUL, SMLAL and UMLAL work.
6. Explain load and store instructions with examples.

**Module 3**

7. Explain how decrementing loops can be implemented efficiently on ARM.
8. Explain loop unrolling in C with an example.
9. Describe how ATPCS passes function arguments and return values.

**Module 4**

10. Demonstrate the common firmware execution flow.
11. List the ARM exceptions and their modes, and explain what happens when an exception occurs.
12. Define interrupt latency and discuss how to reduce it.

**Module 5**

13. Design a 4 KB cache consisting of 256 lines of 4 words of 32 bits.
14. Explain how the memory address is interpreted in a direct-mapped cache.

*Source: `Module1_Question bank.pdf`, `Module2_Question bank.pdf`, `Module3-4-5_Question bank.pdf` and `2A question bank.pdf`. No marks are printed in these banks. The Module 2 file carries an old 15CS44 "Module-5" heading.*
