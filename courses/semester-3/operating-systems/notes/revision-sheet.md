---
title: Revision sheet
---

# Revision sheet — Operating Systems

A last-week sheet, not a textbook. Each module lists what to memorise, the definitions to reproduce, and the question shapes that recur in the BMS papers. Work through the bank closed-book.

## Exam pattern

CIE 50 + SEE 50. The SEE paper is **100 marks in 3 hours: five questions, one per module**, each with two 10-mark parts and an internal OR.

## Module 1 — OS structures, processes and IPC

### Must know

- User view: convenience. System view: resource allocator and control program.
- Multiprogramming holds several jobs, multitasking switches fast, multiprocessing uses several CPUs.
- A trap is software-generated; an interrupt is hardware-generated; both enter the kernel.
- Dual mode restricts privileged instructions to kernel mode.
- System calls: process control, files, devices, information, communication, protection.
- IPC is shared memory or message passing.
- States: new, ready, running, waiting, terminated.
- Threads share code and data but keep their own stack.

### Definitions to reproduce

> An operating system manages the hardware and provides an environment for executing programs conveniently and efficiently.

> A process is a program in execution, with its program counter, registers, stack and current state.

## Module 2 — CPU scheduling and threads

### Must know

- Long-term admits jobs, short-term picks the next burst, medium-term swaps out.
- The dispatcher switches context; dispatch latency is its cost.
- FCFS is non-pre-emptive and suffers the convoy effect.
- SJF minimises average waiting time; SRTF is pre-emptive SJF.
- Priority scheduling starves low-priority jobs; ageing fixes it.
- Round robin is pre-emptive; a huge quantum degenerates to FCFS.
- Turnaround = completion − arrival; waiting = turnaround − burst.
- Compare CPU use, throughput, turnaround, waiting, response.

### Definitions to reproduce

> A context switch saves the running process in its PCB and restores another.

> A time quantum is the interval a process runs in round robin before the CPU is taken away.

### Worked pattern — Gantt chart

Sort arrivals, choose at each point, mark every slice. For SRTF compare remaining times; for RR never pre-empt inside a quantum. Tabulate completion, turnaround and waiting.

## Module 3 — Synchronisation and deadlock

### Must know

- Critical section needs mutual exclusion, progress and bounded waiting.
- Peterson's solution uses `flag[]` and `turn` for two processes.
- `test_and_set()` and `swap()` make check-and-set atomic.
- A binary semaphore is a mutex; a counting semaphore controls N resources.
- Classic problems: producer–consumer, readers–writers, dining philosophers.
- A monitor allows one active process at a time.
- Deadlock needs mutual exclusion, hold and wait, no pre-emption, circular wait together.
- Handling: prevention, avoidance (Banker's), detection and recovery, ignore.

### Definitions to reproduce

> A semaphore is an integer accessed only through atomic wait and signal operations.

> A safe state has at least one sequence in which every process can finish without deadlock.

## Module 4 — Memory management

### Must know

- The CPU issues logical addresses; the MMU translates them to physical addresses.
- Fixed partitions fragment internally, variable partitions externally.
- First, best and worst fit differ only in the hole chosen.
- Paging removes external fragmentation but fragments the last page.
- A page table maps page number to frame number; the offset is unchanged.
- The TLB caches page-table entries; effective access time averages hits and misses.
- Demand paging loads on reference; a fault traps, the OS fetches and restarts.
- FIFO shows Belady's anomaly; LRU approximates optimal, a benchmark only.

### Definitions to reproduce

> A page fault is the trap raised when a program references a page not in physical memory.

> Thrashing is when the system spends more time paging than executing, so throughput collapses.

## Module 5 — File systems and disk scheduling

### Must know

- A file is a named collection of related information on disk.
- Attributes: name, type, location, size, protection, timestamps.
- Access methods: sequential, direct, indexed.
- Directory structures: single-level, two-level, tree, acyclic graph, general graph.
- Contiguous is fast but fragments; linked lacks random access; indexed adds index blocks.
- Free space: bit vector, linked list, grouping, counting.
- Disk scheduling: FCFS, SSTF, SCAN, C-SCAN, LOOK, C-LOOK.
- Head movement sums absolute differences between consecutive cylinders.

### Definitions to reproduce

> A file is a named collection of related information recorded on secondary storage.

> Disk scheduling decides the order in which pending disk requests are served, to reduce head movement.

## Last 24 hours

1. Redo the FCFS, SRTF and RR (q = 2) chart.
2. Redo Banker's algorithm; write the need matrix first.
3. Practise FIFO, LRU and optimal on the reference strings.
4. Rehearse page-fault handling with the diagram.
5. Do the disk queue with head at 50 for FCFS, SSTF, LOOK, CLOOK.
6. Recite the four deadlock and three critical-section conditions.
7. Label the allocation and directory diagrams.

## Question bank

**Module 1**

1. Illustrate with a diagram the I/O operation in a general-purpose computer with device controllers. [10]
2. Classify computing environments with an example for each. [10]

**Module 2**

3. Express the representation of process scheduling with a diagram and discuss the schedulers. [10]
4. Draw Gantt charts and find average waiting time for P1(0,9), P2(1,4), P3(2,9), P4(3,5) using FCFS, SRTF and RR (q = 2). [10]
5. Describe the actions a kernel takes to context switch between processes. [6]

**Module 3**

6. Illustrate Peterson's solution and prove mutual exclusion is preserved. [10]
7. Give the semaphore solution to the bounded-buffer problem. [10]
8. Define deadlock and write short notes on the four necessary conditions and handling methods. [10]

**Module 4**

9. With partitions 100K, 500K, 200K, 300K and 600K, place 212K, 417K, 112K and 426K by first, best and worst fit. Which is most efficient, and why are page sizes powers of two? [10]
10. Illustrate how demand paging affects performance and describe page-fault handling. [10]
11. For 7 0 1 2 0 3 0 4 2 3 0 3 2 1 2 0 1 7 0 1 with three frames, compare FIFO, LRU and optimal. [10]

**Module 5**

12. Explain directory implementation methods and file access methods. [10]
13. List directory structures and explain acyclic-graph and tree-structured directories. [7, July 2018]
14. For 95, 180, 34, 119, 11, 123, 62, 64 with the head at 50 and disk ending at 199, find head movement for FCFS, SSTF, LOOK and CLOOK. [12, Jan 2019]

*Sources: `BCS303_Model Question Paper.pdf`; `OS.pdf` all-module question bank; `IA-1.pdf`; `IA-2.pdf`. Marks are as printed in those files.*
