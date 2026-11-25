# Module 2
## Recursion and Queues

> Source: `DSA MODULE-2.pdf` (24 pages). Every section is covered below.

---

# PART A — RECURSION

# 1. What is Recursion?

**Definition:** recursion is a process in which an object is defined in terms of a **simpler case of itself**.

In programming, a **recursive function** is a function that calls itself.

**Plain English:** you solve a big problem by solving a slightly smaller version of the same problem, again and again, until you reach a version so small that the answer is obvious.

**Analogy:** standing between two mirrors — each image contains a smaller copy of the same scene. In programming, the "smaller copy" must eventually stop, otherwise it goes on forever.

## 1.1 Direct recursion

A function that calls **itself** repeatedly is directly recursive.

```c
void a(...) {
    ...
    a(...);   // calls itself
    ...
}
```

## 1.2 Indirect recursion

A function need not call itself directly. It may call another function, which eventually calls the first one back.

```c
void a(...) {
    ...
    b(...);
    ...
}

void b(...) {
    ...
    a(...);
    ...
}
```

Here `a` calls `b`, `b` calls `a`, and so on. Both are recursive because they **indirectly** call themselves.

**Exam point:** in indirect recursion, you cannot tell that a function is recursive just by looking at its own body — you must follow the call chain.

## 1.3 Two requirements of every recursive function

The PDF states two constraints:

1. **Every call must move closer to the solution.** The problem must get smaller.
2. **There must be at least one terminating condition** (base case) that stops the recursion.

If either is missing:

- no base case → infinite recursion → **stack overflow**;
- no progress → the same call repeats forever → **stack overflow**.

## 1.4 How recursion uses the stack

Recursive calls are **pushed onto the system stack** until the terminating condition is met.

Once the base case is reached, the calls are **popped** and executed in reverse order.

Example for `fact(3)`:

```
fact(3) → fact(2) → fact(1) → fact(0)   [pushing]
fact(0) returns 1
fact(1) returns 1 * 1 = 1
fact(2) returns 2 * 1 = 2
fact(3) returns 3 * 2 = 6                [popping]
```

**Exam point:** recursion is elegant but uses stack space proportional to the depth of recursion.

### Check yourself

1. What is recursion? **A function defined in terms of a simpler version of itself.**
2. What is the base case? **The terminating condition that stops recursion.**
3. What happens without a base case? **Infinite recursion / stack overflow.**
4. What is indirect recursion? **A calls B, B calls A (or a longer cycle).**

---

# 2. Example 1 — Factorial

## 2.1 Definition

For a positive integer `n`, `n!` is the product of all integers from `n` down to 1.

```
5! = 5 × 4 × 3 × 2 × 1
3! = 3 × 2 × 1
0! = 1
```

## 2.2 Recursive definition

```
fact(n) = 1                 if n == 0
        = n * fact(n - 1)   otherwise
```

**Why `0! = 1`?** It is the base case. It also makes the formula consistent: `1! = 1 * 0! = 1`.

## 2.3 Trace for `4!`

```
4! = 4 × 3!
3! = 3 × 2!
2! = 2 × 1!
1! = 1 × 0!
0! = 1

1! = 1 × 1 = 1
2! = 2 × 1 = 2
3! = 3 × 2 = 6
4! = 4 × 6 = 24
```

The PDF's trace has a typo (`I'=1x1=1` should be `1! = 1 × 0! = 1`).

## 2.4 Recursive program

```c
int fact(int n) {
    if (n == 0)
        return 1;
    return (n * fact(n - 1));
}
```

**How to read it:**

- `if (n == 0) return 1;` — base case.
- `return n * fact(n - 1);` — recursive case: the answer depends on a smaller factorial.

**Exam point:** every recursive function needs a base case and a recursive call on a **smaller** input.

### Check yourself

1. What is `fact(5)`? **120.**
2. What is the base case of factorial? **`n == 0`, return 1.**
3. How many calls does `fact(4)` make? **5 calls: fact(4), fact(3), fact(2), fact(1), fact(0).**
4. What is the time complexity of this factorial? **O(n).**

---

# 3. Example 2 — Fibonacci Sequence

## 3.1 Definition

The Fibonacci sequence is:

```
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
```

The first two numbers are the initial values. Each later number is the sum of the two immediately preceding numbers.

**Note on the PDF:** it writes the sequence as `1, 1, 2, 3, 5, 8` in one place and says the first two are `0` and `1` in another. The recursive definition used in the code is:

```
Fib(1) = 0
Fib(2) = 1
Fib(n) = Fib(n-1) + Fib(n-2)   for n > 2
```

So with this convention:

```
Fib(1) = 0
Fib(2) = 1
Fib(3) = 1
Fib(4) = 2
Fib(5) = 3
Fib(6) = 5
```

Some textbooks use `F(0) = 0, F(1) = 1`, which shifts the index by one. Both conventions describe the same sequence; just state which one you are using.

## 3.2 Recursive definition

```
Fib(n) = 0                       if n == 1
       = 1                       if n == 2
       = Fib(n-1) + Fib(n-2)     otherwise
```

## 3.3 Recursion tree for `Fib(5)`

```
                    Fib(5)
                   /      \
              Fib(4)      Fib(3)
             /     \      /     \
         Fib(3)  Fib(2) Fib(2) Fib(1)
         /    \     |       |      |
     Fib(2) Fib(1)  1       1      0
       |      |
       1      0
```

**Notice the repetition:** `Fib(3)` is computed twice, `Fib(2)` three times. This is why naive recursive Fibonacci is inefficient.

## 3.4 Recursive program

```c
int fib(int n) {
    if (n == 1)
        return 0;
    if (n == 2)
        return 1;
    return (fib(n - 1) + fib(n - 2));
}
```

## 3.5 Main function to print the `n`-th Fibonacci number

```c
int main() {
    int n, result;
    printf("enter the value of n\n");
    scanf("%d", &n);
    result = fib(n);
    printf("%d fibonacci number = %d\n", n, result);
    return 0;
}
```

## 3.6 Main function to generate `n` Fibonacci numbers

```c
for (i = 1; i <= n; i++)
    printf("%d ", fib(i));
```

**Exam point:** the recursive Fibonacci has **exponential** time complexity (about O(2^n)) because of repeated subproblems. Memoisation or iteration reduces it to O(n).

### Check yourself

1. What are the first six Fibonacci numbers with `Fib(1)=0`? **0, 1, 1, 2, 3, 5.**
2. Why is recursive Fibonacci slow? **It recomputes the same subproblems many times.**
3. What is the base case? **`n == 1` returns 0; `n == 2` returns 1.**
4. What is the recursion depth for `Fib(n)`? **O(n).**

---

# 4. Example 3 — GCD (Greatest Common Divisor)

## 4.1 Definition

The GCD of two numbers `m` and `n` is the **largest integer that divides both** with remainder zero.

Example: `GCD(10, 30)`.

- Divisors of 10: 1, 2, 5, 10.
- Divisors of 30: 1, 2, 3, 5, 6, 10, 15, 30.
- Common divisors: 1, 2, 5, 10.
- Greatest: **10**.

## 4.2 Recursive definition (subtraction method)

```
GCD(m, n) = m                 if m == n
          = GCD(m - n, n)     if m > n
          = GCD(m, n - m)     if m < n
```

**Idea:** if `m > n`, subtract `n` from `m`; the GCD does not change. Keep reducing the larger number until both are equal.

## 4.3 Trace `GCD(10, 30)`

```
GCD(10, 30)
= GCD(10, 20)     because 10 < 30, so GCD(10, 30-10)
= GCD(10, 10)     because 10 < 20
= 10              because m == n
```

## 4.4 Recursive program

```c
int GCD(int m, int n) {
    if (m == n)
        return m;
    if (m > n)
        return GCD(m - n, n);
    if (m < n)
        return GCD(m, n - m);
}
```

**Exam point:** this is Euclid's algorithm using repeated subtraction. The version using `%` is:

```c
int gcd(int m, int n) {
    if (n == 0) return m;
    return gcd(n, m % n);
}
```

Both compute the same result; the `%` version is faster.

### Check yourself

1. `GCD(12, 18)`? **6.**
2. What is the base case? **`m == n`.**
3. In `GCD(20, 8)`, what is the first recursive call? **`GCD(12, 8)` (since 20 > 8, subtract 8).**
4. Which is faster: subtraction or modulo? **Modulo.**

---

# 5. Example 4 — Towers of Hanoi

## 5.1 The problem

There are **three pegs**: Source `S`, Auxiliary `T`, Destination `D`.

There are `n` disks on peg `S`, of different diameters, placed so that a **larger disk is always below a smaller disk**.

**Goal:** move all `n` disks from `S` to `D`, using `T` as auxiliary.

**Rules:**

1. Only **one disk** can be moved at a time.
2. Only the **top disk** on any peg may be moved.
3. A **larger disk may never rest on a smaller one**.

## 5.2 Recursive solution

To move `n` disks from `S` to `D` using `T`:

**Step 1 (base case):** if `n == 1`, move the single disk from `S` to `D` and stop.

**Step 2:** recursively move the top `n-1` disks from `S` to `T`, using `D` as auxiliary.

**Step 3:** move the `n`-th (largest) disk from `S` to `D`.

**Step 4:** recursively move the `n-1` disks from `T` to `D`, using `S` as auxiliary.

**Plain English:** to move the biggest disk, first move everything above it out of the way; then move the biggest disk; then move the smaller pile onto it.

## 5.3 Trace for 3 disks

```
Move disk 1 from S to D
Move disk 2 from S to T
Move disk 1 from D to T
Move disk 3 from S to D
Move disk 1 from T to S
Move disk 2 from T to D
Move disk 1 from S to D
```

Total moves: **7 = 2^3 - 1**.

## 5.4 Program

```c
int count = 0;

void tower(int n, char source, char destination, char temp) {
    if (n == 1) {
        printf("move %d disc from %c to %c\n", n, source, destination);
        count++;
        return;
    }
    tower(n - 1, source, temp, destination);
    printf("move %d disc from %c to %c\n", n, source, destination);
    count++;
    tower(n - 1, temp, destination, source);
}

int main() {
    int n;
    printf("enter the number of discs\n");
    scanf("%d", &n);
    tower(n, 'S', 'D', 'T');
    printf("the total number of disc moves=%d", count);
    return 0;
}
```

**Parameter order matters:** `tower(n, source, destination, temp)`. In the first recursive call, `temp` becomes the destination and `destination` becomes the auxiliary.

## 5.5 Number of moves

For `n` disks, the minimum number of moves is:

```
2^n - 1
```

Why: `T(n) = 2T(n-1) + 1`, `T(1) = 1` → `T(n) = 2^n - 1`.

| `n` | Moves |
|---|---|
| 1 | 1 |
| 2 | 3 |
| 3 | 7 |
| 4 | 15 |
| 10 | 1023 |
| 64 | 18,446,744,073,709,551,615 |

**Exam point:** Hanoi is a classic example of recursion where the problem is split into two smaller subproblems plus one move. Time complexity: **O(2^n)**.

### Check yourself

1. How many moves for 4 disks? **15.**
2. What is the base case? **`n == 1`: move the disk directly.**
3. Why can't the largest disk move first? **The smaller disks above it must be moved out of the way.**
4. What is the recurrence relation? **`T(n) = 2T(n-1) + 1`.**

---

# 6. Example 5 — Ackermann's Function

## 6.1 Definition

The Ackermann function, named after Wilhelm Ackermann, is one of the simplest and earliest-discovered examples of a **total computable function** that is not primitive recursive. It grows extremely quickly — both in its value and in the size of its call tree.

```
A(m, n) = n + 1                        if m == 0
        = A(m - 1, 1)                  if m > 0 and n == 0
        = A(m - 1, A(m, n - 1))        otherwise
```

## 6.2 Example expansion: `A(1, 2)`

```
A(1, 2) = A(0, A(1, 1))
        = A(0, A(0, A(1, 0)))
        = A(0, A(0, A(0, 1)))
        = A(0, A(0, 2))
        = A(0, 3)
        = 4
```

## 6.3 Growth: `A(4, 3)`

The PDF expands `A(4, 3)` to show how enormous the computation is. A few stages:

```
A(4, 3) = A(3, A(4, 2))
        = A(3, A(3, A(4, 1)))
        = ...
        = A(3, A(3, 65533))
        = ...
        = A(3, 2^65536 - 3)
        = ...
        = 2^(2^65536) - 3
```

This number has far more digits than there are atoms in the observable universe. The point is not to compute it by hand; it is to show how fast a recursive function can grow.

## 6.4 Program

```c
int ackerman(int m, int n) {
    if (m == 0)
        return n + 1;
    if (n == 0)
        return ackerman(m - 1, 1);
    return ackerman(m - 1, ackerman(m, n - 1));
}
```

**Exam points:**
- Three cases: `m == 0`, `n == 0`, otherwise.
- The third case contains a **nested recursive call** — the inner `A(m, n-1)` is computed first and passed as the second argument to the outer call.
- It is **not primitive recursive**, but it is computable.
- It grows faster than any primitive recursive function.

### Check yourself

1. What is `A(0, n)`? **`n + 1`.**
2. What is `A(m, 0)`? **`A(m-1, 1)`.**
3. What is `A(1, 1)`? **`A(0, A(1, 0)) = A(0, A(0, 1)) = A(0, 2) = 3`.**
4. Why is Ackermann's function famous? **It is computable but grows extremely fast and is not primitive recursive.**

---

# PART B — QUEUES

# 7. Queue — Basic Operations

## 7.1 What is a queue?

A **queue** is a waiting line. Example: customers in front of a bank counter or ticket counter.

- Customers join at the **end of the line** (rear/tail).
- The customer at the **front** gets service and leaves (front/head).

This is **FCFS** — First Come First Serve — or **FIFO** — First In First Out.

**As a data structure:**
> A queue is an ordered list of elements from which an element may be removed at one end called the **front**, and into which an element may be inserted at the other end called the **rear**.

These restrictions ensure data is processed in the order it is received.

**Exam point:** stack = LIFO, one end; queue = FIFO, two ends.

## 7.2 Pictorial representation

```
        delete (front)                    insert (rear)
             ↑                                 ↑
        ┌────┬────┬────┬────┬────┬────┐
        │ 10 │ 20 │ 30 │    │    │    │
        └────┴────┴────┴────┴────┴────┘
          ↑              ↑
          f              r
```

- `f` points to the **front** element (the next one to be deleted).
- `r` points to the **rear** element (the most recently inserted).

## 7.3 Types of queues

The PDF lists:

1. **Ordinary queue** (linear queue)
2. **Double-ended queue** (deque)
3. **Circular queue**
4. **Priority queue**

## 7.4 Queue ADT

**Objects:** a finite ordered list with zero or more elements.

**Functions:** for all `q ∈ Queue`, `item ∈ element`, `queuesize ∈ positive integer`:

| Function | Meaning |
|---|---|
| `Queue Create(queuesize)` | Creates an empty queue whose maximum size is `queuesize` |
| `Boolean IsFull(q, queuesize)` | TRUE if the number of elements in `q` is `queuesize`, else FALSE |
| `Queue InsertQ(q, item)` | If `IsFull(q)`, queue is full; else insert `item` at the rear and return |
| `Boolean IsEmpty(q)` | TRUE if there are no elements, else FALSE |
| `Element DeleteQ(q)` | If `IsEmpty(q)`, return; else remove and return the front element |

**Exam point:** the ADT names the operations abstractly; `InsertQ` = enqueue, `DeleteQ` = dequeue.

### Check yourself

1. Why is a queue called FIFO? **The first element inserted is the first removed.**
2. Where is insertion done? **Rear.**
3. Where is deletion done? **Front.**
4. Name four types of queues. **Ordinary, circular, deque, priority.**

---

# 8. Ordinary (Linear) Queue

## 8.1 Operations

1. **Insert Rear** — insert at the rear.
2. **Delete Front** — delete from the front.
3. **Display** — show the contents.

## 8.2 Initial conditions and observations

- Initially, when there are no elements: **`f = 0` and `r = -1`**.
- Whenever **`f > r`**, there are no elements → queue is empty.
- **`f == r`** means there is exactly **one** element.

## 8.3 Array implementation

```c
#define queuesize 5

void insert_rear(int item, int *r, int q[]) {
    if (*r == queuesize - 1) {
        printf("queue overflow\n");
        return;
    }
    *r = *r + 1;
    q[*r] = item;
}

void delete_front(int *f, int *r, int q[]) {
    int item;
    if (*f > *r) {
        printf("queue is empty\n");
        return;
    }
    item = q[*f];
    printf("the item deleted is %d", item);
    *f = *f + 1;

    if (*f > *r) {   // queue became empty
        *f = 0;
        *r = -1;
    }
}
```

**Why reset `f` and `r` when the queue becomes empty?** So the queue can be reused from the beginning. Without the reset, `f` would keep increasing and the queue would appear permanently full.

**Display:**

```c
for (i = f; i <= r; i++)
    printf("%d\n", q[i]);
```

## 8.4 The disadvantage of an ordinary queue

Once `rear` reaches `queuesize - 1`, you **cannot insert** any more elements, **even if the queue is not full**.

Example: `queuesize = 5`.

```
index:  0    1    2    3    4
        ┌────┬────┬────┬────┬────┐
        │    │    │ 30 │ 40 │ 50 │
        └────┴────┴────┴────┴────┘
                       ↑
                       r = 4
```

Here two locations (0 and 1) are free, but `r == 4`, so insertion fails. This is called **false overflow**.

**Solutions:**

1. **Shift the data** to the beginning so elements start at index 0. This is costly if the data is large.
2. **Use a circular queue** — the preferred solution.

**Exam point:** ordinary queue suffers from **false overflow** (space wasted at the front).

### Check yourself

1. Initial values of `f` and `r`? **`f = 0`, `r = -1`.**
2. When is the queue empty? **`f > r`.**
3. When does it have one element? **`f == r`.**
4. What is false overflow? **Rear reaches the end while free space exists at the front.**
5. What are two solutions? **Shift elements, or use a circular queue.**

---

# 9. Circular Queue

## 9.1 The idea

A circular queue is not straight; the **last element of the array is logically followed by the first element**. The array is used as if it were a circle.

```
        q[0] ── q[1]
       /            \
    q[3]            q[2]
       \            /
        q[4] ── ...
```

When `rear` reaches the end, the next position wraps around to index 0.

## 9.2 Modulo arithmetic

To move to the next position:

```c
r = (r + 1) % queuesize;
```

Example: `queuesize = 4`, `r = 3`:

```
(3 + 1) % 4 = 4 % 4 = 0
```

So the next position is index 0.

Similarly, for the front:

```c
f = (f + 1) % queuesize;
```

## 9.3 The `count` variable

In a circular queue, `f == r` can mean **empty** or **full**, so pointers alone are ambiguous. Use a variable **`count`** that stores the number of elements currently in the queue.

- `count == 0` → queue is empty.
- `count == queuesize` → queue is full.

## 9.4 Insert and delete

**Insert:**

```c
r = (r + 1) % queuesize;
q[r] = item;
count = count + 1;
```

**Delete:**

```c
item = q[f];
f = (f + 1) % queuesize;
count = count - 1;
```

**Check empty/full:**

```c
if (count == 0)        // empty
if (count == queuesize) // full
```

## 9.5 Implementation

```c
#define queuesize 5

void insert_rear(int item, int *r, int *count, int q[]) {
    if (*count == queuesize) {
        printf("queue overflow\n");
        return;
    }
    *r = (*r + 1) % queuesize;
    q[*r] = item;
    *count = *count + 1;
}

void delete_front(int *f, int *count, int q[]) {
    int item;
    if (*count == 0) {
        printf("queue is empty\n");
        return;
    }
    item = q[*f];
    printf("the item deleted is %d", item);
    *f = (*f + 1) % queuesize;
    *count = *count - 1;
}
```

**Display:**

```c
for (i = 1; i <= count; i++) {
    printf("%d\n", q[f]);
    f = (f + 1) % queuesize;
}
```

Note: display uses a **copy** of `f` (passed by value), so the original front pointer is not changed.

## 9.6 Worked example

`queuesize = 4`, initially `f = 0`, `r = -1`, `count = 0`.

Insert 10, 20, 30, 40:

```
r = 0 → q[0] = 10, count = 1
r = 1 → q[1] = 20, count = 2
r = 2 → q[2] = 30, count = 3
r = 3 → q[3] = 40, count = 4  → full
```

Delete 10, 20:

```
f = 1, count = 3
f = 2, count = 2
```

Insert 50, 60:

```
r = (3+1)%4 = 0 → q[0] = 50, count = 3
r = (0+1)%4 = 1 → q[1] = 60, count = 4 → full
```

The queue now holds `30, 40, 50, 60` in circular order starting at `f = 2`.

**Exam point:** the modulo operation is what makes the queue circular; `count` removes the empty/full ambiguity.

### Check yourself

1. What does `(r + 1) % size` do? **Wraps the rear pointer to the start after the last index.**
2. Why is `count` needed? **To distinguish empty from full when `f == r`.**
3. What is the next position after index 4 in a queue of size 5? **0.**
4. Is a circular queue full when `r == f`? **Not necessarily; check `count`.**

---

# 10. Circular Queue Using Dynamic Arrays (Array Doubling)

## 10.1 Why simple doubling is not enough

Consider a circular queue of size 5:

```
index:  0    1    2    3    4
        ┌────┬────┬────┬────┬────┐
        │ 10 │ 20 │ 30 │ 40 │ 50 │
        └────┴────┴────┴────┴────┘
          ↑                        ↑
          f                        r
```

Full. Delete 3 elements:

```
        ┌────┬────┬────┬────┬────┐
        │    │    │    │ 40 │ 50 │
        └────┴────┴────┴────┴────┘
                            ↑    ↑
                            f    r
```

Insert 3 elements:

```
        ┌────┬────┬────┬────┬────┐
        │ 60 │ 70 │ 80 │ 40 │ 50 │
        └────┴────┴────┴────┴────┘
          ↑    ↑
          r    f
```

Full again. If you simply double the array to size 10, the elements are **out of order** in memory: `60, 70, 80, 40, 50`. You must copy them into the new array **in queue order**, starting from `front`.

Correct new array:

```
index:  0    1    2    3    4    5    6    7    8    9
        ┌────┬────┬────┬────┬────┬────┬────┬────┬────┬────┐
        │ 40 │ 50 │ 60 │ 70 │ 80 │    │    │    │    │    │
        └────┴────┴────┴────┴────┴────┴────┴────┴────┴────┘
          ↑                        ↑
          f                        r
```

Then reset:

```c
f = 0;
r = count - 1;
capacity = 2 * capacity;
```

## 10.2 Insert function with doubling

```c
void insert_rear(int item, int *r, int *count, int *f) {
    int i;
    int *newq;

    if (*count == capacity) {
        // allocate double capacity
        newq = (int *) malloc(2 * capacity * sizeof(int));

        // copy elements in queue order
        for (i = 0; i < *count; i++) {
            newq[i] = q[*f];
            *f = (*f + 1) % capacity;
        }

        // reinitialize pointers
        *f = 0;
        *r = *count - 1;
        capacity = 2 * capacity;

        free(q);
        q = newq;
    }

    *r = (*r + 1) % capacity;
    q[*r] = item;
    *count = *count + 1;
}
```

**Important details:**

- The copy loop uses `*f` and advances it modulo the **old** capacity.
- `newq[i]` places the elements contiguously from index 0.
- After copying, `f = 0` and `r = count - 1`.
- `free(q)` releases the old array; `q = newq` points to the new one.

**Delete and display** are the same as the ordinary circular queue, using `capacity` instead of `queuesize`.

**Exam point:** for a circular queue, doubling requires **reordering** the elements, not just copying the raw array.

### Check yourself

1. Why can't you just `realloc` a circular queue? **Because the logical order wraps around; elements must be copied in queue order.**
2. After doubling, what are `f` and `r`? **`f = 0`, `r = count - 1`.**
3. What is the new capacity if the old is 5? **10.**
4. Which loop condition copies the elements? **`for (i = 0; i < count; i++)`, advancing `f` modulo the old capacity.**

---

# 11. Deque (Double-Ended Queue)

## 11.1 Definition

A **deque** is a data structure in which insertions and deletions can be done at **either the front or the rear**.

So there are four basic operations:

1. **Insert Front**
2. **Insert Rear**
3. **Delete Front**
4. **Delete Rear**
5. **Display**

## 11.2 Two variations

### Input-restricted deque

Insertion is allowed at **only one end**, but deletion is allowed at **both ends**.

Example: insertion only at the rear.

```
        delete ← [10][20][30] → delete
                    ↑
                  insert (rear only)
```

### Output-restricted deque

Deletion is allowed at **only one end**, but insertion is allowed at **both ends**.

Example: deletion only at the front.

```
        insert → [10][20][30] ← insert
                    ↑
                  delete (front only)
```

**Exam point:**
- Input-restricted = **insert** restricted.
- Output-restricted = **delete** restricted.

## 11.3 `insert_front` cases

`insert_rear`, `delete_front` and `display` are the same as an ordinary queue.

### Case 1: `f == 0` and `r != -1`

```
        ┌────┬────┬────┬────┬────┬────┐
        │ 10 │ 20 │ 30 │    │    │    │
        └────┴────┴────┴────┴────┴────┘
          ↑              ↑
          f              r
```

There is no space before index 0, so **insert front is not possible**.

### Case 2: `f == 0` and `r == -1` (queue empty)

```
        ┌────┬────┬────┬────┬────┬────┐
        │    │    │    │    │    │    │
        └────┴────┴────┴────┴────┴────┘
          ↑
          f, r = -1
```

Insert at the rear position:

```c
r = r + 1;
q[r] = item;
```

### Case 3: `f > 0`

```
        ┌────┬────┬────┬────┬────┬────┐
        │    │    │ 30 │ 40 │    │    │
        └────┴────┴────┴────┴────┴────┘
                       ↑    ↑
                       f    r
```

There is space before `f`, so decrement `f` and insert:

```c
f = f - 1;
q[f] = item;
```

## 11.4 `insert_front` function

```c
void insert_front(int item, int *f, int *r, int q[]) {
    if (*f == 0 && *r != -1) {
        printf("Insert front not possible\n");
        return;
    }
    if (*f == 0) {          // empty queue
        *r = *r + 1;
        q[*r] = item;
        return;
    }
    *f = *f - 1;
    q[*f] = item;
}
```

## 11.5 `delete_rear` function

```c
void delete_rear(int *f, int *r, int q[]) {
    int item;
    if (*f > *r) {
        printf("queue is empty\n");
        return;
    }
    item = q[*r];
    printf("the item deleted is %d", item);
    *r = *r - 1;

    if (*f > *r) {   // queue became empty
        *f = 0;
        *r = -1;
    }
}
```

**Exam point:** a deque generalises both stack and queue:
- insert/delete at the **same** end → stack behaviour;
- insert at rear, delete at front → queue behaviour.

### Check yourself

1. What is a deque? **A double-ended queue; insert/delete at both ends.**
2. Input-restricted deque restricts what? **Insertion to one end.**
3. Output-restricted deque restricts what? **Deletion to one end.**
4. When is `insert_front` not possible? **When `f == 0` and the queue is not empty.**

---

# 12. Priority Queue

## 12.1 Why priority queues?

Linear and circular queues process elements in **FIFO** order. But sometimes items must be processed by **importance**, not arrival time.

Example: in an operating system, a high-priority process should run before a low-priority one, even if it arrived later.

## 12.2 Definition and rules

A **priority queue** is a queue in which each element has a **priority**, and elements are processed according to:

1. An element of **higher priority** is processed before any element of **lower priority**.
2. If two elements have the **same priority**, the one inserted **first** is processed first (FIFO within the same priority).

## 12.3 Types

### Ascending priority queue

Elements can be inserted in **any order**, but on deletion the **smallest** element is removed.

(Assumption in the PDF: a smaller value = higher priority.)

### Descending priority queue

Elements can be inserted in **any order**, but on deletion the **largest** element is removed.

**Exam point:** "ascending" refers to the order of deletion (smallest first), not the insertion order.

## 12.4 Method 1 — Insert anywhere, delete the smallest

**Aim:**

- Insert elements in any order.
- Delete only the smallest (highest-priority) element.

**Deletion steps:**

1. Starting from the front, traverse the array to find the **smallest element** and its position.
2. Delete that element.
3. If the deleted element is not the rightmost, **shift all trailing elements one position left** to fill the gap.
4. Update the rear pointer.

**Code:**

```c
void delete_small(int *f, int *r, int q[]) {
    int item, i, min, pos;

    if (*f > *r) {
        printf("queue is empty\n");
        return;
    }

    if (*f == *r) {          // only one element
        item = q[*r];
        printf("the item deleted is %d", item);
        *f = 0;
        *r = -1;
    } else {
        min = q[0];
        pos = 0;

        for (i = 1; i <= *r; i++) {
            if (q[i] < min) {
                min = q[i];
                pos = i;
            }
        }

        item = q[pos];
        printf("the item deleted is %d", item);

        for (i = pos; i < *r; i++)
            q[i] = q[i + 1];

        *r = *r - 1;
    }
}
```

**Disadvantage:** inefficient — it searches the whole queue for the smallest element and shifts elements after deletion. Both are O(n).

## 12.5 Method 2 — Keep the queue sorted, delete from the front

**Aim:**

- Insert elements so the queue is always in **increasing order** (highest priority at the front).
- Delete simply from the front.

**Insertion steps:**

1. Find the appropriate vacant position based on priority.
2. Insert the item there.
3. Update the rear pointer.

**Code:**

```c
void insert_order(int item, int *f, int *r, int q[]) {
    int j;

    if (*r == queuesize - 1) {
        printf("queue is full\n");
        return;
    }

    j = *r;
    while (j >= *f && item < q[j]) {
        q[j + 1] = q[j];   // shift right
        j--;
    }
    q[j + 1] = item;
    *r = *r + 1;
}
```

**Disadvantage:** insertion requires finding the correct position and shifting elements; it also needs compaction when the array has free space at the front but the rear has reached the end.

**Exam point:** arrays are **not efficient** for priority queues. A **heap** is the standard efficient implementation (covered later).

## 12.6 Comparison of the two methods

| | Method 1 | Method 2 |
|---|---|---|
| Insertion | O(1) — insert anywhere at rear | O(n) — find position and shift |
| Deletion | O(n) — search + shift | O(1) — delete front |
| Queue order | Unsorted | Always sorted ascending |
| Best when | Few deletions, many insertions | Many deletions, few insertions |

### Check yourself

1. What are the two rules of a priority queue? **Higher priority first; same priority → FIFO.**
2. In an ascending priority queue, which element is deleted? **The smallest.**
3. In a descending priority queue, which element is deleted? **The largest.**
4. Which method is better for many deletions? **Method 2 (sorted insertion, O(1) deletion).**
5. What data structure is best for priority queues? **A heap.**

---

# Module 2 — Question Bank

## 1–2 mark questions

1. Define recursion.
2. Differentiate direct and indirect recursion.
3. What are the two requirements of a recursive function?
4. What is a base case?
5. What happens if a recursive function has no base case?
6. Write the recursive definition of factorial.
7. What is `0!`?
8. Write the recursive definition of Fibonacci.
9. Write the recursive definition of GCD.
10. State the rules of the Towers of Hanoi.
11. How many moves are needed for `n` Hanoi disks?
12. Write the Ackermann function definition.
13. Why is Ackermann's function special?
14. Define a queue.
15. Why is a queue called FIFO?
16. What is the front? What is the rear?
17. Name four types of queues.
18. Define queue ADT.
19. What are the initial values of `f` and `r` in an ordinary queue?
20. When is an ordinary queue empty?
21. What is false overflow?
22. What is a circular queue?
23. What is the purpose of `count` in a circular queue?
24. Write the formula to advance the rear in a circular queue.
25. What is a deque?
26. Differentiate input-restricted and output-restricted deques.
27. Define a priority queue.
28. What is an ascending priority queue?
29. What is a descending priority queue?
30. Why are arrays inefficient for priority queues?

## 5-mark questions

1. Explain direct and indirect recursion with examples.
2. Explain the recursion requirements and how recursion uses the stack.
3. Explain the factorial function with a recursive program and trace.
4. Explain the Fibonacci function with a recursion tree.
5. Explain the GCD function with a trace.
6. Explain the Towers of Hanoi with rules, recursive solution and trace.
7. Explain Ackermann's function with an example.
8. Explain the basic operations of a queue with a diagram.
9. Explain the array implementation of an ordinary queue.
10. Explain the disadvantage of an ordinary queue and its solutions.
11. Explain a circular queue with insert/delete operations.
12. Explain the dynamic array implementation of a circular queue.
13. Explain a deque and its two variations.
14. Explain `insert_front` and `delete_rear` with cases.
15. Explain a priority queue and its two types.
16. Explain Method 1 of priority queue implementation.
17. Explain Method 2 of priority queue implementation.
18. Compare the two priority queue implementation methods.

## 10-mark questions

1. Explain recursion in detail with factorial, Fibonacci, GCD, Hanoi and Ackermann examples.
2. Explain the Towers of Hanoi problem with rules, recursion, trace and program.
3. Explain queues in detail: ADT, ordinary queue, circular queue, deque and priority queue.
4. Explain circular queues, including the `count` variable and dynamic array doubling.
5. Explain deques and priority queues with implementation methods.

---

# Common exam mistakes in Module 2

1. **No base case or no progress** → infinite recursion.
2. **Writing `fact(n) = n * fact(n)`** → no progress; must be `fact(n-1)`.
3. **Mixing Fibonacci conventions.** State whether `Fib(1)=0` or `Fib(0)=0`.
4. **Hanoi parameter order.** `tower(n, source, destination, temp)`; the recursive calls swap roles.
5. **Saying Hanoi takes `2^n` moves.** It is `2^n - 1`.
6. **Ackermann's third case.** It is `A(m-1, A(m, n-1))`, with a nested call.
7. **Queue initial values.** `f = 0`, `r = -1`, not both 0.
8. **Empty condition.** `f > r`, not `f == r` (which means one element).
9. **Circular queue overflow.** Check `count == queuesize`, not `r == f`.
10. **Forgetting modulo.** `r = (r + 1) % size`, not `r = r + 1`.
11. **Dynamic circular queue.** Copy elements in queue order, not raw array order.
12. **Deque confusion.** Input-restricted = insertion restricted; output-restricted = deletion restricted.
13. **Priority queue direction.** Ascending = smallest deleted first; descending = largest deleted first.
14. **Same-priority rule.** FIFO among equal priorities.
15. **Saying arrays are ideal for priority queues.** They are not; heaps are.
