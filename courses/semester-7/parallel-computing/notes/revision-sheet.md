---
title: Revision sheet
---
# Revision sheet — Parallel Computing

Parallel Computing (BCS702) is a CSE course. Its outcomes cover data and temporal parallelism, parallel architectures, performance evaluation and CUDA. The folder has no readable map for every unit, so this sheet groups the material by topic.

## Exam pattern

Internal-assessment papers are 40 marks. Questions are usually 10 marks with an OR alternative, at L3 or L4: apply a concept to a scenario, then analyse the consequences.

## Topic 1 — Parallelism, architecture and performance

### Must know

- Sequential processing is limited by instruction fetch, memory access and processor speed; parallelism uses multiple processors on one problem.
- Flynn's taxonomy: SISD, SIMD, MISD and MIMD. SIMD suits vector and array processors; MIMD covers multicore and distributed systems.
- Shared memory has one address space; distributed memory has private memories and explicit message passing. DSM lies between them.
- Speedup S(n) = T(1) / T(n); efficiency E(n) = S(n) / n. Amdahl bounds speedup by the serial fraction; Gustafson considers scaled problem size.

### Definitions to reproduce

**Parallel computing** is simultaneous execution of subtasks on multiple processors. **Temporal parallelism** overlaps stages in time, as in a pipeline. **SIMD** runs one instruction stream over multiple data streams; **MIMD** runs multiple streams over multiple data streams. **DSM** gives a shared address space over distributed memories. **Speedup** is sequential time divided by parallel time; **efficiency** is speedup divided by processor count.

### Worked pattern

For shared versus distributed memory, tabulate address space, communication, scalability, programming difficulty and fault tolerance. Shared memory is easy to program but suffers contention and coherence costs; distributed memory scales well but needs send and receive. If T(1) = 100 s and T(32) = 8 s, S = 12.5 and E = 39 per cent; explain the gap by communication and idle time.

## Topic 2 — Processes, threads and the parallel operating system

### Must know

- Resource management: processor allocation, memory allocation, scheduling and load balancing.
- Static scheduling assigns work before execution; dynamic scheduling moves tasks at run time.
- Processes have separate address spaces; threads share one. User-level threads are invisible to the kernel; kernel-level threads are scheduled individually.
- Mutual exclusion, critical sections, race conditions, atomic test-and-set, spinlocks and blocking locks.
- IPC by shared memory or message passing; semaphores and monitors for synchronisation.

### Definitions to reproduce

A **process** is a program in execution with its own address space. A **thread** is a schedulable unit sharing its process's memory. A **race condition** makes the result depend on uncontrolled interleaving. **Test-and-set** atomically reads a location and writes 1, forming a lock primitive. A **spinlock** busy-waits; a **blocking lock** sleeps.

### Worked pattern

For test-and-set, show `while (test_and_set(lock) == 1);` for lock and `lock = 0` for unlock. Under low contention and short critical sections, spinning gives low latency; under high contention or long sections, blocking avoids wasted CPU.

## Topic 3 — GPU architecture and CUDA

### Must know

- CPUs have few complex cores; GPUs have thousands of simple cores, high bandwidth and SIMT execution.
- CUDA grid, block and thread hierarchy; a warp is a scheduling group of threads.
- Memory hierarchy: registers, shared memory, cache and global memory. Shared memory is on-chip and low latency.
- Host code allocates device memory, copies data, launches the kernel and copies results back.
- Occupancy, coalescing, shared-memory tiling and warp divergence determine performance.

### Definitions to reproduce

A **kernel** is a function run in parallel by many GPU threads. A **warp** is a scheduling group, usually 32 threads. **Shared memory** is low-latency, block-visible memory. **Occupancy** is active warps divided by the maximum supported. **Coalescing** combines adjacent accesses into fewer transactions. **Warp divergence** occurs when threads in a warp take different paths.

### Worked pattern

For vector addition, write `__global__ void add(float *a, float *b, float *c, int n)` with `idx = blockIdx.x * blockDim.x + threadIdx.x`. Host code does `cudaMalloc`, `cudaMemcpy`, launch `add<<<blocks, threads>>>`, copy back and free. Copy overhead can dominate for small vectors.

## Topic 4 — Diagnosing and improving performance

### Must know

- A profiler shows kernel time, call sequence, thread states, elapsed time and memory use.
- A trace analyser shows the timeline: communication, idle time, synchronisation and load imbalance.
- Uneven execution across cores may be load imbalance or communication overhead; traces distinguish them.
- Benchmarking and memory profiling show whether latency, bandwidth or compute dominates.
- Optimisations: better decomposition, fewer synchronisations, locality and sequential I/O.

### Definitions to reproduce

**Profiling** measures where a running program spends time and memory. **Tracing** records timed events across processors. **Communication overhead** is time spent sending, receiving and waiting. **Load imbalance** exists when some processors finish later than others.

### Worked pattern

For a slow simulation, compare per-core busy time with waiting time. If all cores are busy but wall time is high, look for communication or serial sections. If some idle while others work, look for load imbalance.

## Last 24 hours

Revise speedup and efficiency, Flynn's taxonomy, shared versus distributed memory, user versus kernel threads, test-and-set and spinlocks, the CUDA execution model and vector addition.

## Question bank

1. In multiprocessor systems, test-and-set coordinates access to shared memory. Analyse how it enables atomic updates, use pseudocode to implement lock and unlock, and discuss its performance under contention. (10 marks)
2. Analyse how the shift from serial to parallel processing has influenced computational efficiency, and compare CPU limitations with GPU advantages. (5 marks)
3. A data analytics team wants to accelerate vector addition using CUDA. Write the structure of a CUDA C program that launches a kernel, and explain the host and device roles. (10 marks)
4. A genomics company accelerates vector summation for DNA analysis. Explain how CPU and GPU memory hierarchies affect efficiency, and why CUDA may not give linear speedup. (10 marks)
5. A lab runs a simulation on 2, 8 and 32 processors and sees sublinear speedup and low sustained performance. Analyse the causes and distinguish them from peak figures. (10 marks)
6. A multithreaded server blocks on I/O while other threads idle. Analyse user-level versus kernel-level threads and the effect of context switching and locks on throughput. (10 marks)
7. A banking application updates shared balances concurrently and shows lost updates. Analyse mutual exclusion, spinlocks and blocking locks. (10 marks)

*Source: `Improvement Test Scheme.pdf` and `schemePC IA2.pdf`. The module PDFs `PC SCHEME IA1.pdf`, `PC MODULE 1 N19.pdf`, `PC module -3.pdf`, `INS Module-4 N19.pdf`, `PC Module-5.pdf` and `PC question Bank answer N-19.pdf` are scans with no usable text.*
