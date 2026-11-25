# Module 1 — Part A
## Foundations, Pointers, Memory Allocation, Arrays, Structures

> Source: `DSA Module-1 Part-A.pdf` (31 pages). Every section of the PDF is covered below.

---

# 1. Introduction to Data Structures

## 1.1 What is a data structure?

A **data structure** is a model for organising data so that accessing it becomes easy.

The PDF defines it as the study of:

- how data is organised in memory,
- how it can be manipulated,
- how efficiently it can be retrieved,
- how different data items are logically related.

**Plain English:** data is like luggage. A data structure is how you pack it — a cupboard with fixed shelves (array), a chain of boxes tied together (linked list), a family tree (tree), a road map (graph). The packing method decides how fast you can find, add or remove something.

**Exam definition:**
> A data structure is a way of organising and storing data in memory so that it can be accessed and modified efficiently. It also defines the logical relationship between the data elements.

## 1.2 Classification of data structures

```
Data Structures
├── Primitive
│     └── int, float, char, double ...
└── Non-Primitive
      ├── Linear
      │     ├── Array        (physically adjacent)
      │     ├── Linked List  (logically adjacent, linked by pointers)
      │     ├── Stack        (LIFO)
      │     └── Queue        (FIFO)
      └── Non-Linear
            ├── Tree
            └── Graph
```

### Primitive data structures

Data structures that **can be manipulated directly by machine instructions**.

Examples: `int`, `float`, `char`.

Think: the basic LEGO bricks the CPU already understands.

### Non-primitive data structures

Data structures that **cannot be manipulated directly by machine instructions**. They are built using primitive types and operations.

They are divided into:

**Linear data structures** — elements show either **physical adjacency** or **logical adjacency**.

- *Physical adjacency* means elements sit next to each other in memory.
  Example: **array** — `a[0]`, `a[1]`, `a[2]` are in consecutive memory locations.
- *Logical adjacency* means elements are connected by links even if they are scattered in memory.
  Example: **linked list** — each node stores a pointer to the next node.

The PDF's key sentence: data is arranged in a linear fashion, although the way it is stored in memory need not be sequential.

**Non-linear data structures** — no adjacency between elements, but they are logically related; data is not arranged sequentially.

Examples: **trees**, **graphs**.

**Exam points:**
- Array = physical adjacency.
- Linked list = logical adjacency.
- Tree/graph = non-linear.
- Stack and queue are linear even though their operations are restricted.

### Check yourself

1. Is a stack linear or non-linear? **Linear.**
2. What is the difference between physical and logical adjacency? **Physical = consecutive memory; logical = connected by pointers, memory may be scattered.**
3. Give one example each of primitive and non-primitive structures. **`int`; array/tree.**

---

## 1.3 Operations on data structures

The PDF lists eight operations:

| Operation | Meaning | Real-life example from the PDF |
|---|---|---|
| **Create** | Make a new data structure | Declaring `int a;` |
| **Insertion** | Add a new element/node | A new member joins the organisation |
| **Deletion** | Remove an existing element/node | A member resigns |
| **Update** | Change the contents of a node | A member changes address |
| **Traversal** | Visit every node exactly once | Reading every member's name/email to send a meeting invite |
| **Searching** | Find the location of a node for a given key | Find the address for a given name |
| **Sorting** | Arrange nodes in a particular order | List members by increasing age |
| **Merging** | Combine two lists into one | Combine member files of two departments |

**Create:** in most languages this is a declaration. `int a;` allocates memory for an integer at compile time.

**Traversal** is also called **visiting**. "Exactly once" is the important phrase.

**Merging** is not the same as sorting: merging combines; sorting orders. (Merge sort does both, but that is a later topic.)

### Check yourself

1. Which operation visits every element exactly once? **Traversal.**
2. Which operation would you use to correct a wrong phone number? **Update.**
3. Combining two sorted lists into one is called ______. **Merging.**

---

## 1.4 Representation of data structures

Any data structure can be represented in two ways.

### 1. Sequential representation

- Data is kept in **continuous memory locations**.
- **Retrieval is fast** because the address can be calculated directly.
- **Insertion and deletion are slow** because elements must be shifted.

Why shifting happens:

- To insert in the middle, free space must be created by shifting later elements **right**.
- To delete from the middle, the gap must be filled by shifting later elements **left**.

The CPU time spent shifting can be much larger than the actual insert/delete operation.

**Example:** an array.

### 2. Linked representation

- Elements are connected by **links (pointers)**.
- They **need not be in continuous memory**.
- Insertion and deletion only change links, so they are faster.
- Retrieval is slower because you must follow the links one by one.

**Example:** a linked list.

**Exam table:**

| | Sequential | Linked |
|---|---|---|
| Memory | Continuous | Scattered |
| Access | Fast, direct | Slow, sequential |
| Insert/delete | Slow, shifting | Fast, link changes |
| Example | Array | Linked list |

### Check yourself

1. Why is insertion in an array slow? **Elements after the position must be shifted right.**
2. Why is access in a linked list slow? **You must traverse links from the start; no direct address formula.**

---

## 1.5 Algorithm specification

**Definition:** an **algorithm** is a finite set of instructions that accomplishes a particular task.

### Five criteria every algorithm must satisfy

1. **Input** — zero or more quantities are supplied externally.
2. **Output** — at least one quantity is produced.
3. **Definiteness** — each instruction is clear and unambiguous.
4. **Finiteness** — the algorithm terminates after a finite number of steps and uses finite resources.
5. **Effectiveness** — every instruction is basic enough to be carried out.

**Memory trick:** **I-O-D-F-E** → Input, Output, Definiteness, Finiteness, Effectiveness.

Note: input can be **zero** (e.g. print "Hello"), but output must be **at least one**.

### Three ways to specify an algorithm

1. **Natural language** — a clear description, but ambiguous. Natural language is surprisingly difficult for algorithms because words can be interpreted in more than one way.
2. **Flowchart** — geometric shapes containing descriptions of steps. Works well only for small, simple algorithms.
3. **Pseudocode** — a mixture of natural language and programming-language constructs (like C). It is a semi-formal description of each step.

**Exam points:**
- Flowcharts are good for small algorithms only.
- Pseudocode is not tied to one programming language.
- Definiteness = no ambiguity; finiteness = must stop.

### Check yourself

1. Which criterion says an algorithm must stop? **Finiteness.**
2. Can an algorithm have zero inputs? **Yes.**
3. Which specification method mixes English and code? **Pseudocode.**

---

# 2. Pointers (Revision)

> The PDF marks this section "not in syllabus", but pointers are the foundation of linked lists, trees and dynamic memory. Learn it anyway.

## 2.1 Memory organisation

Memory is a sequence of **byte-sized locations** (1 byte = 8 bits).

- Each byte has a **unique address**.
- Addresses are **positive integers**, from 0 up to some maximum.
- Every object (data or code) loaded into memory occupies a **range of consecutive addresses**.
- Each variable and function starts at a particular location and spans as many bytes as its type needs.

For:

```c
int a = 10;
```

the compiler does three things:

1. Reserves space in memory for an integer.
2. Associates the name `a` with that location.
3. Stores the value `10` there.

Memory map from the PDF:

```
name:    a
value:   10
address: 1004
```

**Exam point:** the address of a variable is the address of its **first byte**.

## 2.2 The address operator `&`

When used as a prefix to a variable name, `&` gives the **address** of that variable.

```c
int a = 10;
printf("The address of a is %u\n", &a);
printf("The value of a is %d\n", a);
```

`%u` is used because addresses are **unsigned integers**.

For:

```c
char a;
int b;
```

assuming `char` = 1 byte and `int` = 4 bytes, the PDF shows:

```
a at 2000
b at 2001 ... 2004
&a = 2000
&b = 2001
```

So `&a` is the first byte occupied by `a`.

> Note: in real compilers `int` is usually aligned to a 4-byte boundary, so `b` would not normally start at 2001. The PDF uses this only to show "first byte" addressing. For exams, follow the PDF's assumption.

## 2.3 The indirection operator `*`

When used as a prefix to an **address**, `*` gives the **value stored at that address**.

```c
int a = 10;
printf("%u\n", &a);    // address
printf("%d\n", *(&a)); // value at that address = 10
```

The two operators are **complementary**:

```
*(&a) == a
```

**Plain English:** `&` asks "where do you live?", `*` says "go to that address and bring back what is inside".

## 2.4 Pointer variables

A **pointer** is a variable that contains the address of another variable.

```c
int a = 10;
int *p;
p = &a;
```

Memory picture:

```
p contains 1004  →  address 1004 contains 10
```

`p` is not an ordinary variable; its value is an address.

**Exam definition:**
> A pointer is a variable that stores the memory address of another variable.

## 2.5 Pointer declaration

Syntax:

```c
datatype *pointer_name;
```

The datatype can be primitive (`int`, `float`, `char`) or user-defined.

```c
int *p;    // p can hold the address of an int
float *p;  // p can hold the address of a float
char *p;   // p can hold the address of a char
```

**Rule:** the pointer's type must match the type of the variable it points to.

Valid:

```c
int *p;
int a = 10;
p = &a;
```

Invalid:

```c
int *p;
float a = 3.4;
p = &a;      // type mismatch
```

**Why the type matters:** the compiler uses it to know how many bytes to read/write and how far `p + 1` should move.

## 2.6 Accessing a variable through its pointer

```c
int a, b;
int *p;
a = 10;      // assume a is at 1000
p = &a;      // p = 1000
b = *p;      // b = 10
```

- `p` means the address `1000`.
- `*p` means the contents at address `1000`, which is `10`.

Program from the PDF prints `a`, `b` and `*p`; all three print `10`.

## 2.7 Initialisation of pointers

An uninitialised ordinary variable contains an unknown ("garbage") value.

An uninitialised pointer contains an **unknown address**. If you dereference it, the program may crash or corrupt memory. Such errors are very hard to debug.

Good practice:

```c
int a;
int *p = &a;    // valid address
int *q = NULL;  // points to nothing
```

**`NULL`** is a pointer value that indicates the pointer does **not point to any part of memory**.

**Exam point:** always initialise a pointer to a valid address or `NULL`.

## 2.8 Pointers and functions

### Swap without pointers (call by value)

```c
temp = a;
a = b;
b = temp;
```

This works inside `main` because the code directly uses `a` and `b`.

### Swap using pointers (call by reference)

```c
void swap(int *c, int *d) {
    int temp;
    temp = *c;
    *c = *d;
    *d = temp;
}

swap(&a, &b);
```

Here the function receives **addresses**, so changing `*c` and `*d` changes the original `a` and `b`.

**Key ideas from the PDF:**

- If `a` and `b` are passed **by value**, the swap is not seen in `main`; the originals keep their values.
- When **one** value must be sent back, use `return`.
- When **more than one** value must be sent back, use **call by reference** (pointers).

**Exam question:** "Why do we pass addresses to `swap`?" → Because C passes arguments by value; to modify the caller's variables, the function needs their addresses.

## 2.9 Functions returning pointers

A function can return a pointer.

```c
int* bigger(int *c, int *d) {
    if (*c > *d)
        return c;
    else
        return d;
}
```

`bigger` returns the **address** of the larger number. In `main`:

```c
int *big = bigger(&a, &b);
printf("%d", *big);
```

**Exam point:** the return type is `int *`, meaning "pointer to int".

## 2.10 Pointer to a function

A pointer can store the **address of a function**.

```c
int add(int c, int d) {
    return c + d;
}

int (*ptr)(int, int);   // pointer to a function taking 2 ints, returning int
ptr = add;              // store function address
res = (*ptr)(a, b);     // call through the pointer
```

**Why useful:** you can choose which function to call at runtime (e.g. a menu of operations).

**Syntax trap:** `int (*ptr)(int, int)` is a function pointer. `int *ptr(int, int)` would be a function returning an `int *`. The parentheses around `*ptr` are essential.

## 2.11 Pointer to a pointer

A pointer is itself a variable, so another pointer can store its address.

```c
int a = 10;
int *p = &a;
int **q = &p;
```

Memory:

```
q → p → a
3000 → 2000 → 10
```

- `p` is the address of `a` (2000).
- `*p` is the value at 2000 → 10.
- `q` is the address of `p` (3000).
- `*q` is the value at 3000 → 2000 (which is `p`).
- `**q` is the value at 2000 → 10.

Therefore:

```c
a == *p == **q
```

This is **2-level indirection**. There is no limit to the number of levels, but more levels are rarely needed.

### Check yourself (pointers)

1. What does `&a` give? **Address of `a`.**
2. What does `*(&a)` give? **Value of `a`.**
3. What is a dangling pointer? **A pointer that points to memory that has been freed or is no longer valid.**
4. What is the type of `int **q`? **Pointer to a pointer to int.**
5. Why is `p + 1` not always "one byte ahead"? **Pointer arithmetic moves by the size of the pointed-to type.**

---

# 3. Memory Allocation

## 3.1 Static memory allocation

Memory is allocated at **compile time**.

- The size is **fixed**.
- It cannot be increased or decreased during execution.
- If you allocate too much and use little, memory is **wasted**.
- If you try to store more than allocated, you get **overflow**.

Example:

```c
int a[10];
```

The compiler reserves space for 10 integers. If you store only 3 values, 7 slots are wasted. If you need 11, you cannot fit them.

**Used when:** the data size is known before processing.

**Exam points:**
- Static allocation → compile time.
- Stored in stack or global/static memory.
- Faster, because memory is already reserved.
- Examples: normal arrays, global variables.

## 3.2 Dynamic memory allocation

Memory is allocated at **run time**.

- The size can be decided while the program is running.
- Memory can be increased or decreased.
- Used when the storage requirement is unpredictable.

The four standard library functions are `malloc`, `calloc`, `realloc` and `free`.

### `malloc`

**Description:** allocates and reserves a block of memory specified in **bytes** and returns a pointer to the **first byte** of the allocated space.

Syntax:

```c
ptr = (datatype *) malloc(size);
```

- `ptr` — pointer of type `datatype`.
- `datatype` — any basic or user-defined type.
- `size` — number of bytes required.

Example:

```c
ptr = (int *) malloc(sizeof(int));
```

This reserves enough memory for one `int` and stores the first byte's address in `ptr`.

**Return value:**
- On success: a `void *` pointer to the new block.
- On failure: `NULL`.

**Important:** `malloc` does **not** initialise the memory. It contains garbage.

### `calloc`

**Description:** allocates **multiple blocks of the same size**, initialises **all bytes to zero**, and returns a pointer to the first byte.

Syntax:

```c
ptr = (datatype *) calloc(n, size);
```

- `n` — number of blocks.
- `size` — size of each block in bytes.

Example:

```c
ptr = (int *) calloc(200, sizeof(int));
```

This reserves space for 200 integers (an array of 200 ints) and zeroes it.

**Return value:** same as `malloc` — `void *` on success, `NULL` on failure.

**Exam point:** `calloc` = **c**lear + allocate; it zero-fills.

### `realloc`

**Description:** changes the size of memory previously allocated by `malloc`, `calloc` or `realloc`.

Syntax:

```c
ptr = (datatype *) realloc(ptr, newsize);
```

- `ptr` — starting address of the old block.
- `newsize` — new size in bytes; may be larger or smaller.

Example:

```c
ptr = malloc(size);
ptr = realloc(ptr, newsize);
```

**Return value:**
- On success: pointer to the new block.
- On failure: `NULL`.

**Key guarantee:** the contents of the old block are copied to the new block, so earlier data is not lost.

**Exam point:** always assign the result to a temporary pointer first if you need to handle failure safely, otherwise you lose the old pointer:

```c
int *temp = realloc(ptr, newsize);
if (temp != NULL) ptr = temp;
```

### `free`

**Description:** de-allocates a block previously allocated by `malloc`, `calloc` or `realloc`.

Syntax:

```c
free(ptr);
```

**Return value:** none.

**Why it matters:** dynamically allocated memory has **no name**; it can only be accessed through a pointer. The programmer is responsible for freeing it when it is no longer needed.

## 3.3 Problems with dynamic memory allocation

### 1. Memory leakage

**Definition:** a part of memory is reserved but is **not accessible to any application**, so it cannot be freed or reused.

Example:

```c
int *a;
a = (int *) malloc(sizeof(int));
*a = 10;

a = (int *) malloc(sizeof(int));  // a now points to a new block
*a = 20;
```

The first block (holding 10) has lost its only pointer. It is still reserved but unreachable — a **memory leak**.

**Fix:** free the old block before overwriting the pointer, or use `realloc`.

### 2. Dangling pointer

**Definition:** a pointer that points to a **destroyed object** or does not contain a valid address.

Example:

```c
int *a;
a = (int *) malloc(sizeof(int));
*a = 20;
free(a);
// a still holds the old address, but that memory is no longer valid
```

After `free(a)`, the memory goes back to the free pool. `a` still contains the old address, so using `*a` is invalid. `a` is now a **dangling pointer**.

**Fix:** after `free(a);`, set `a = NULL;`.

**Exam distinction:**
- Memory leak = memory lost because no pointer points to it.
- Dangling pointer = pointer left pointing to memory that was freed.

## 3.4 `malloc` vs `calloc`

| S.No | `malloc()` | `calloc()` |
|---|---|---|
| 1 | Syntax: `ptr = (datatype*) malloc(size);` — one argument, the size of the block | Syntax: `ptr = (datatype*) calloc(n, size);` — two arguments: number of blocks and size of each |
| 2 | Allocates **one block** of the specified size | Allocates **multiple blocks**, each of the same size |
| 3 | Allocated space is **not initialised** | Each byte is **initialised to zero** |
| 4 | Faster, because no zero-filling | Computationally more expensive because of zero-filling, but often more convenient |
| 5 | Can allocate the required size even if memory is **not contiguous** but available at different locations | Allocates the required number of blocks **contiguously**; if it cannot, returns `NULL` |

**Memory trick:** `malloc` = **m**emory allocation (one block, garbage); `calloc` = **c**ontiguous allocation + clear (many blocks, zeroed).

## 3.5 Static vs dynamic memory allocation

| S.No | Static | Dynamic |
|---|---|---|
| 1 | Allocated at **compile time** | Allocated at **run time** |
| 2 | Size is **fixed**, cannot change during execution | Size is **not fixed**, can increase/decrease |
| 3 | Used when data size is **known** before processing | Used when storage requirement is **unpredictable** |
| 4 | **Faster** — memory already allocated, only data manipulation remains | **Slower** — memory must be allocated first, then data manipulated |
| 5 | Uses **stack** or **global/static** memory | Uses **heap** memory |
| 6 | Example: arrays | Example: dynamic arrays, linked lists |

### Check yourself (memory)

1. Which function zero-fills memory? **`calloc`.**
2. Which function changes the size of an existing block? **`realloc`.**
3. What happens if `malloc` fails? **It returns `NULL`.**
4. What is the difference between a memory leak and a dangling pointer? **Leak = unreachable allocated memory; dangling = pointer to freed memory.**
5. Where does dynamic memory come from? **The heap.**

---

# 4. Arrays

## 4.1 Definition and representation

An **array** is a collection of items of the **same data type**. All elements share a **common name**, and each element is identified by a **subscript/index**.

Example:

```c
int a[5] = {10, 20, 30, 40, 50};
```

Memory (assuming `int` = 4 bytes, base address 1000):

| Element | Value | Address |
|---|---|---|
| `a[0]` | 10 | 1000 |
| `a[1]` | 20 | 1004 |
| `a[2]` | 30 | 1008 |
| `a[3]` | 40 | 1012 |
| `a[4]` | 50 | 1016 |

Elements are stored in **consecutive memory locations**.

**Lower bound (LB):** smallest index (here 0).
**Upper bound (UB):** largest index (here 4).

**Length formula:**

```
Length = UB - LB + 1
```

Example: `4 - 0 + 1 = 5`.

**Exam point:** in C, array indices start at 0, so `LB = 0` and `UB = n - 1` for an array of `n` elements.

## 4.2 Address calculation and pointer arithmetic

Two ways to get an element's address:

1. Using `&`:
   ```c
   &a[0], &a[1], &a[2], ...
   ```
2. Using the array name as a pointer:
   ```c
   a, a + 1, a + 2, ...
   ```

The **base address** is the address of the first element, and it is stored in the array name:

```c
a == &a[0]
a + 1 == &a[1]
a + 2 == &a[2]
```

**Pointer arithmetic rule:**

```
a + n = a + n * sizeof(one element)
```

Example from the PDF: `a = 1000`, `sizeof(int) = 4`:

```
a + 3 = 1000 + 3 * 4 = 1012 = &a[3]
```

In general:

```
&a[i] == a + i
a[i]  == *(a + i)
```

**This is the single most examined line in the arrays section.**

### Program 1 — print elements and addresses

```c
for (i = 0; i < n; i++)
    scanf("%d", a + i);       // same as &a[i]

for (i = 0; i < n; i++) {
    printf("%u\t", a + i);    // address
    printf("%d\n", *(a + i)); // value
}
```

### Program 2 — sum of array elements

```c
sum = 0;
for (i = 0; i < n; i++)
    sum = sum + *(a + i);
```

**Exam point:** `a + i` is an address; `*(a + i)` is the value.

## 4.3 Two-dimensional arrays

The PDF explains a 2-D array as an **array of arrays**.

```c
int a[3][5];
```

This is a 1-D array of length 3; each element is itself a 1-D array of length 5.

```
a[0] → [0][1][2][3][4]
a[1] → [0][1][2][3][4]
a[2] → [0][1][2][3][4]
```

To reach `a[i][j]`:

1. `a[i]` gives a pointer to the first element of row `i`.
2. Add `j` to that pointer to reach the `j`-th element of row `i`.

Therefore:

```
*(a + i) + j   == &a[i][j]     // address
*(*(a + i) + j) == a[i][j]      // value
```

**Memory trick:** read from the inside out:
- `a + i` → row pointer
- `*(a + i)` → row (which decays to a pointer to its first element)
- `*(a + i) + j` → address of column `j`
- `*(*(a + i) + j)` → value

### Program — read and print an `m × n` matrix

```c
scanf("%d", *(a + i) + j);        // same as &a[i][j]
printf("%d\t", *(*(a + i) + j));  // same as a[i][j]
```

## 4.4 Dynamic arrays

**Problem with normal arrays:** the size must be known at **compile time**, and it cannot change while the program runs.

A **dynamic array** is an array whose size is determined at **run time**, and whose size can also be changed at run time.

Creating one:

```c
int *a;
a = (int *) malloc(n * sizeof(int));
```

- `n` is read from the user at run time.
- `a` behaves like an array: `a[i]` or `*(a+i)`.
- Free it when done: `free(a);`.

### Program — read and print `n` elements

```c
a = (int *) malloc(n * sizeof(int));
for (i = 0; i < n; i++)
    scanf("%d", a + i);

for (i = 0; i < n; i++)
    printf("%d\n", *(a + i));

free(a);
```

### Program — maximum of `n` elements

```c
max = *(a + 0);
for (i = 1; i < n; i++)
    if (*(a + i) > max)
        max = *(a + i);
```

### Program — sum of positive and negative numbers

```c
psum = 0; nsum = 0;
for (i = 0; i < n; i++) {
    if (*(a + i) > 0)
        psum += *(a + i);
    else
        nsum += *(a + i);
}
```

### 2-D dynamic array

For an `m × n` matrix, allocate an array of row pointers, then allocate each row:

```c
int **a;
a = (int **) malloc(rows * sizeof(int *));

for (i = 0; i < rows; i++)
    a[i] = (int *) malloc(columns * sizeof(int));
```

Access:

```c
scanf("%d", *(a + i) + j);        // &a[i][j]
printf("%d\t", *(*(a + i) + j));  // a[i][j]
```

**Exam point:** a 2-D dynamic array is a **pointer to a pointer** (`int **`), and each row is allocated separately.

> The PDF's final `free(a)` only frees the row-pointer array; strictly, you should also `free(a[i])` for each row before `free(a)`. Mention this if asked about correct deallocation.

### Check yourself (arrays)

1. `a[5]` has what valid indices? **0 to 4.**
2. If `a = 2000` and `sizeof(int) = 4`, what is `a + 5`? **2020.**
3. What is `*(a + i)` in words? **The value at index `i`.**
4. What is `*(*(a + i) + j)`? **`a[i][j]`.**
5. Why use `malloc` for an array? **To decide the size at run time.**

---

# 5. Structures

## 5.1 Why structures?

Arrays store many items of the **same** data type. But real records mix types:

- name → string
- age → int
- salary → float

A structure lets you group **related information of possibly different data types under one name**.

**Exam definition:**
> A structure is a collection of related information of possibly different data types grouped under one name.

## 5.2 Definition and syntax

```c
struct tagname {
    datatype member1;
    datatype member2;
};
```

- `struct` — keyword.
- `tagname` — user-defined name for the structure.
- `datatype` — basic or user-defined type.
- `member1`, `member2` — fields/attributes of the structure.

Example:

```c
struct student {
    char name[20];
    int marks1;
    int marks2;
    int marks3;
    char regno[10];
};
```

**Important:** defining a structure does **not** allocate memory. It only describes a **template/format**. Memory is allocated only when a **variable** of that structure type is declared.

```
name   → array of 20 characters
marks1 → integer
marks2 → integer
marks3 → integer
regno  → array of 10 characters
```

## 5.3 `typedef`

`typedef` creates a **new name** for an existing data type.

Syntax:

```c
typedef datatype user_provided_name;
```

Example:

```c
typedef int MARKS;
MARKS m1, m2, m3;
```

This is the same as `int m1, m2, m3;`, but the name `MARKS` documents the purpose.

**Advantages:**
- Self-documenting: descriptive names for standard types.
- Shortens complex/lengthy declarations.
- Improves readability.

With structures:

```c
typedef struct student STD;
STD a, b;
```

`STD` is now a new type name for `struct student`.

## 5.4 Forms of structure variable declaration

**Format 1 — declare tag, then variables separately:**

```c
struct student {
    char name[20];
    int marks1, marks2, marks3;
    char regno[10];
};

struct student a, b, c;
```

**Format 2 — declare variables with the definition:**

```c
struct student {
    char name[20];
    int marks1, marks2, marks3;
    char regno[10];
} a, b, c;
```

**Format 3 — using `typedef`:**

```c
typedef struct {
    char name[20];
    int marks1, marks2, marks3;
    char regno[20];
} STD;

STD a, b;
```

or:

```c
struct student { ... };
typedef struct student STD;
```

**Exam point:** all three forms create variables; the difference is only where the variable names appear and whether a type alias is used.

## 5.5 Accessing members

Use the **dot operator** `.` (member selection operator).

```c
STD a;
a.name
a.marks1
a.marks2
a.marks3
a.regno
```

**Rule:** before the dot there must be a **structure variable**; after the dot there must be a **member**.

## 5.6 Assigning values to members

Direct assignment:

```c
strcpy(a.name, "Mahesh");
a.marks1 = 97;
a.marks2 = 98;
a.marks3 = 99;
strcpy(a.regno, "1AY10IS0017");
```

Using `scanf`:

```c
scanf("%s", a.name);
scanf("%d%d%d", &a.marks1, &a.marks2, &a.marks3);
scanf("%s", a.regno);
```

**Why no `&` for `name` and `regno`?** Because they are character arrays; the array name already gives the base address.

## 5.7 Structure initialisation

Like arrays, structures can be initialised where they are declared.

```c
struct book {
    char name[10];
    float price;
    int pages;
};

struct book b1 = {"c++", 150.00, 550};
struct book b2 = {"physics", 150.80, 800};
```

Or with the definition:

```c
struct book {
    char name[10];
    float price;
    int pages;
} b1 = {"c++", 150.00, 550},
  b2 = {"physics", 150.80, 800};
```

**Important:** C does **not** allow initialising individual members inside the template:

```c
struct person {
    int weight = 60;      // NOT allowed
    float height = 170.6; // NOT allowed
} p1;
```

Initialisation must happen when the **actual variable** is declared.

## 5.8 Array of structures

To store data about 100 books, you could declare `b1 ... b100`, but that is inconvenient. Use an **array of structures**:

```c
struct book {
    char name[10];
    float price;
    int pages;
};

struct book b[100];
```

Access:

```c
b[i].name
b[i].price
b[i].pages
```

The dot operator still accesses fields; the subscript selects the array element.

## 5.9 Assigning/copying structure variables

A structure variable can be assigned to another structure variable of the **same type** using `=`.

```c
struct employee e1 = {"Harish", 30, 25000.00};
struct employee e2, e3;

// piece-meal copying
strcpy(e2.name, e1.name);
e2.age = e1.age;
e2.salary = e1.salary;

// one-shot copying
e3 = e2;
```

All three print the same data.

**Why one-shot copying works:** structure members are stored in **contiguous memory locations**, so the compiler can copy the whole block.

**Invalid:** assigning between **different** structure types.

```c
struct { char name[10]; int age; float salary; } a, b;
struct { char name[10]; int age; float salary; } c, d;

a = b;   // valid (same type)
a = c;   // invalid (different type)
```

## 5.10 Comparing structure variables

Comparison of two structure variables is **not allowed**, even of the same type:

```c
a == b   // invalid
a != b   // invalid
```

But individual members **can** be compared:

```c
a.member1 == b.member1
a.member1 != b.member1
```

**Rule:** arithmetic, relational, logical and other operations can be performed on **individual members**, not on whole structure variables.

## 5.11 Pointer to a structure

A variable that contains the address of a structure variable is a **pointer to a structure**.

```c
struct employee e1 = {"Harish", 30, 25000.00};
struct employee *ptr;
ptr = &e1;
```

Two ways to access members:

1. Dereference then dot:
   ```c
   (*ptr).name
   (*ptr).age
   (*ptr).salary
   ```
2. Arrow operator:
   ```c
   ptr->name
   ptr->age
   ptr->salary
   ```

**Why parentheses in `(*ptr).name`?** Because `.` has higher precedence than `*`. `*ptr.name` would be wrong.

**To read with `scanf`:**

```c
scanf("%d", &ptr->age);
// or
scanf("%d", &(*ptr).age);
```

## 5.12 Structures vs arrays

| Arrays | Structures |
|---|---|
| Collection of related data elements of the **same** data type | Collection of variables of **similar or dissimilar** data types |
| Elements accessed by **subscript/index**, or by dereferencing/indirection for pointers | Members accessed using `.` or `->` for pointers |

## 5.13 Self-referential structures

A structure that contains a **reference (pointer) to itself** is a **self-referential structure**.

General form:

```c
struct tagname {
    datatype member1;
    datatype member2;
    struct tagname *pointer_name;
};
```

Example:

```c
struct node {
    int info;
    struct node *link;
};
```

**Why it matters:** this is the building block of **linked lists, trees and graphs**. Each node stores data plus a pointer to another node of the same type.

**Exam point:** a self-referential structure cannot contain a member of its own type directly (that would require infinite memory); it contains a **pointer** to its own type.

### Check yourself (structures)

1. Does defining a structure allocate memory? **No — only declaring a variable does.**
2. Which operator accesses a member through a structure variable? **Dot (`.`).**
3. Which operator accesses a member through a pointer? **Arrow (`->`).**
4. Can you compare two structure variables with `==`? **No; compare members individually.**
5. What is a self-referential structure used for? **Linked lists, trees, graphs.**

---

# Module 1 Part A — Question Bank

## 1–2 mark questions

1. Define a data structure.
2. Differentiate primitive and non-primitive data structures.
3. Differentiate linear and non-linear data structures with examples.
4. List any five operations performed on data structures.
5. Define algorithm and list its five characteristics.
6. What is the difference between flowchart and pseudocode?
7. Define pointer. Give the syntax for pointer declaration.
8. What is the difference between `&` and `*` operators?
9. What is a NULL pointer?
10. Why are pointers initialised?
11. What is call by reference? Why is it needed?
12. Define memory leak.
13. Define dangling pointer.
14. Differentiate `malloc` and `calloc`.
15. Differentiate static and dynamic memory allocation.
16. Define an array. State the length formula.
17. If `a` is an integer array with base address 1000, find the address of `a[6]` (`sizeof(int)=4`).
18. What is a dynamic array?
19. Define a structure.
20. What is `typedef`? Give an example.
21. What is an array of structures?
22. Why can't two structure variables be compared with `==`?
23. What is a self-referential structure?

## 5-mark questions

1. Explain the classification of data structures with a diagram.
2. Explain the operations performed on data structures with examples.
3. Compare sequential and linked representation.
4. Explain the five characteristics of an algorithm.
5. Explain memory organisation with a diagram.
6. Explain pointers and functions with a swap example.
7. Explain functions returning pointers and pointers to functions.
8. Explain pointer to a pointer with a diagram.
9. Explain static and dynamic memory allocation with advantages and disadvantages.
10. Explain `malloc`, `calloc`, `realloc` and `free` with syntax and examples.
11. Explain memory leakage and dangling pointers with code.
12. Explain the representation of a 1-D array in memory.
13. Explain pointer arithmetic with an example.
14. Explain the memory representation of a 2-D array using the array-of-arrays concept.
15. Explain dynamic arrays with an example.
16. Explain the different forms of structure variable declaration.
17. Explain array of structures with an example.
18. Explain copying and comparison of structure variables.
19. Explain pointers to structures with an example.
20. Differentiate structures and arrays.
21. Explain self-referential structures with an example.

## 10-mark questions

1. Explain the classification, operations and representation of data structures in detail.
2. Explain pointers in detail: declaration, initialisation, access, functions, function pointers, pointer to pointer.
3. Explain dynamic memory allocation functions in detail, including memory leak and dangling pointer.
4. Explain arrays in detail: representation, address calculation, pointer arithmetic, 2-D arrays and dynamic arrays.
5. Explain structures in detail: definition, declaration forms, initialisation, arrays of structures, copying, comparison, pointers and self-referential structures.

---

# Common exam mistakes in Part A

1. **Saying "array is a pointer."** An array name *decays* to a pointer to its first element, but the array itself is a block of memory; `sizeof(a)` differs.
2. **Forgetting `+1` in the length formula.** `UB - LB + 1`, not `UB - LB`.
3. **Pointer arithmetic in bytes.** `a + 1` moves by `sizeof(*a)`, not 1 byte.
4. **Using `*ptr.member`.** Use `(*ptr).member` or `ptr->member`.
5. **Saying `calloc` is always better.** It zero-fills, which costs time; `malloc` is faster when initialisation is not needed.
6. **Confusing memory leak and dangling pointer.** Leak = no pointer to allocated memory; dangling = pointer to freed memory.
7. **Saying structure definition allocates memory.** It does not; only a variable declaration does.
8. **Comparing whole structures.** Only members can be compared.
9. **Forgetting that `malloc` returns `void *`.** It must be cast to the required pointer type in C++ (and is often cast in C for clarity).
10. **Mixing up `realloc` failure handling.** If you assign directly and it returns `NULL`, you lose the old block's address.
