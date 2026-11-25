# Module 1 — Part B
## Stacks, System Stack, Expressions, Multiple Stacks

> Source: `DSA Module-1 Part-B.pdf` (27 pages). Every section is covered below.

---

# 1. Stack — Basic Operations

## 1.1 What is a stack?

A **stack** is a special data structure in which:

- elements are **inserted at one end** called the **top**, and
- elements are **deleted from the same end**.

Because the **last element inserted is the first element deleted**, a stack is called **LIFO** — **Last In, First Out**.

**Real-life analogy:** a stack of plates. You add a plate on top and remove the top plate. You cannot pull a plate from the bottom without removing the ones above it.

Another analogy: browser history — the most recent page is the first one you go back to.

## 1.2 The two main operations

### Push

**Inserting** an element into a stack is called **push**.

- Before pushing, check whether the stack is full.
- If the stack is full and you try to push, **stack overflow** occurs.

### Pop

**Deleting** an element from a stack is called **pop**.

- Before popping, check whether the stack is empty.
- If the stack is empty and you try to pop, **stack underflow** occurs.

The PDF's schematic:

```
        push ↓
        ┌─────┐
        │  B  │ ← top
        ├─────┤
        │  A  │
        └─────┘
        pop ↑
```

`top` always points to the **most recently inserted** element.

## 1.3 Operations performed on a stack

The PDF lists:

1. **Insertion** (push)
2. **Deletion** (pop)
3. **Display**
4. **Check whether the stack is full** (`isFull`)
5. **Check whether the stack is empty** (`isEmpty`)

**Exam point:** a stack is a **linear** data structure with **restricted** insertion and deletion — both happen at the same end.

### Check yourself

1. Why is a stack called LIFO? **The last element pushed is the first popped.**
2. What is stack overflow? **Pushing into a full stack.**
3. What is stack underflow? **Popping from an empty stack.**
4. Where does insertion/deletion happen? **At the top.**

---

# 2. Implementation of Stack Using Arrays

## 2.1 The idea

Use an array `s[]` and an integer `top`.

- Initially, `top = -1` → stack is empty.
- **Push:** increment `top`, then store the item at `s[top]`.
- **Pop:** read `s[top]`, then decrement `top`.
- **Full condition:** `top == stacksize - 1`.
- **Empty condition:** `top == -1`.

The array size is fixed with `#define stacksize 5`.

## 2.2 Push function

```c
void push(int item, int *top, int s[]) {
    if (*top == stacksize - 1) {
        printf("Stack overflow\n");
        return;
    }
    *top = *top + 1;
    s[*top] = item;
}
```

**Why `int *top`?** Because `top` must be modified inside the function and the change must be visible in `main`. Passing the address allows that.

**Order matters:** increment `top` **before** storing. If you store first, you overwrite the current top element.

## 2.3 Pop function

```c
int pop(int *top, int s[]) {
    int item;
    if (*top == -1) {
        return -1;              // signals underflow
    }
    item = s[*top];
    *top = *top - 1;
    return item;
}
```

**Order matters:** read the item **before** decrementing `top`. Otherwise you lose the top element.

**Why return `-1`?** It is used as an error signal. In `main`, if `pop` returns `-1`, the program prints "Stack underflow". This assumes `-1` is not a valid data value; a more robust version would use a separate status variable.

## 2.4 Display function

```c
void display(int top, int s[]) {
    int i;
    if (top == -1) {
        printf("Stack is empty\n");
        return;
    }
    printf("Contents of the stack are\n");
    for (i = 0; i <= top; i++)
        printf("%d\n", s[i]);
}
```

This prints from **bottom to top** (`s[0]` first). If you want top-to-bottom, loop from `top` down to `0`.

## 2.5 `isFull` and `isEmpty`

```c
void isfull(int top) {
    if (top == stacksize - 1)
        printf("Stack is full\n");
    else
        printf("Stack is not full\n");
}

void isempty(int top) {
    if (top == -1)
        printf("Stack is empty\n");
    else
        printf("Stack is not empty\n");
}
```

## 2.6 Menu-driven `main`

```c
int top = -1, choice, item, s[stacksize], y;

for (;;) {
    printf("1.Push 2.Pop 3.Display 4.Exit\n");
    scanf("%d", &choice);

    switch (choice) {
        case 1:
            scanf("%d", &item);
            push(item, &top, s);
            break;
        case 2:
            y = pop(&top, s);
            if (y == -1)
                printf("Stack underflow\n");
            else
                printf("item deleted = %d\n", y);
            break;
        case 3:
            display(top, s);
            break;
        case 4:
            exit(0);
    }
}
```

**Exam point:** the array implementation is simple and fast, but the size is **fixed**. You cannot grow the stack beyond `stacksize`.

### Check yourself

1. What is the initial value of `top`? **-1.**
2. What is the full condition for an array stack of size `n`? **`top == n - 1`.**
3. In push, do you increment `top` before or after storing? **Before.**
4. In pop, do you decrement `top` before or after reading? **After.**

---

# 3. Applications of Stacks

The PDF lists:

1. **Recursive functions** — the system stack stores each function call.
2. **Conversion of expressions** — infix ↔ postfix/prefix.
3. **Evaluation of expressions** — postfix evaluation.
4. **Traversing trees and graphs** — DFS uses a stack.
5. **Reversal of a string.**
6. **Checking whether a string is a palindrome.**
7. **Checking parenthesis matching.**

**Exam question:** "List any four applications of stacks." Use the first four or any four from the list.

---

# 4. System Stack and Activation Record

## 4.1 What is the system stack?

The stack used by a program **at run time** is called the **system stack**. It is used when functions are invoked and executed.

When a function is called:

- a structure called an **activation record** (also called a **stack frame**) is created on top of the stack.

When the function terminates:

- its activation record is **deleted** from the top of the stack.

## 4.2 What is inside an activation record?

An activation record stores:

1. **Local variables** (if any)
2. **Parameters** (if any)
3. **Return address** — where to continue after the function finishes
4. **Pointer to the previous stack frame** (previous frame pointer)

Using the activation record, functions can communicate with each other.

## 4.3 Step-by-step execution

The PDF describes eight steps.

**Step 1:** The user asks the OS to execute the program. The OS transfers control to `main()` along with a **return address**, so that after `main` finishes, control returns to the OS.

**Step 2:** A stack frame is created for `main()` containing:

- return address of the OS,
- local variables of `main()`,
- previous frame pointer (`NULL`, because this is the first record).

This frame is pushed onto the system stack.

**Step 3:** `main()` executes.

**Step 4:** When the `return` statement in `main()` executes, its activation record is removed. The return address inside it is used to transfer control back to the OS.

**Step 5:** Suppose `main()` calls `a1()`. A new stack frame is created containing:

- return address of `main()`,
- local variables of `a1()`,
- current frame pointer (the top of the stack).

This new frame is pushed.

The **previous frame pointer** of `a1()`'s record points to `main()`'s record.

**Step 6:** Control transfers to `a1()`.

**Step 7:** When `a1()` returns, its activation record is removed. The return address inside it transfers control back to `main()`.

**Step 8:** When `main()` finishes, its record is removed and the OS return address transfers control back to the OS.

## 4.4 Diagram (described)

```
        ┌─────────────────────────┐
        │  return address (OS)    │
        │  local variables main   │
        │  previous frame = NULL  │  ← main() frame
        └─────────────────────────┘

After calling a1():

        ┌─────────────────────────┐
        │  return address (main)  │
        │  local variables a1     │
        │  previous frame ptr ────┼──→ main() frame
        └─────────────────────────┘  ← a1() frame (top)
```

**Exam points:**
- Activation record = stack frame.
- It contains locals, parameters, return address, previous frame pointer.
- Function calls are **pushed**; returns are **popped**.
- This is why infinite recursion causes **stack overflow**.

### Check yourself

1. What is another name for an activation record? **Stack frame.**
2. What four things does it contain? **Locals, parameters, return address, previous frame pointer.**
3. What happens to the activation record when a function returns? **It is popped/deleted.**
4. Why does recursion use the system stack? **Each recursive call creates a new activation record.**

---

# 5. Stack Abstract Data Type (ADT)

An **ADT** describes **what** operations a data structure supports, not **how** they are implemented.

The PDF defines a stack ADT as follows.

**Objects:** a finite ordered list with zero or more elements.

**Functions:** for all `s ∈ Stack`, `item ∈ element`, `stacksize ∈ positive integer`:

| Function | Meaning |
|---|---|
| `Stack Create(stacksize)` | Creates an empty stack whose maximum size is `stacksize` |
| `Boolean IsFull(s, stacksize)` | Returns TRUE if the number of elements in `s` is `stacksize`, else FALSE |
| `Stack Push(s, item)` | If `IsFull(s)`, stack is full; else insert `item` onto the stack and return |
| `Boolean IsEmpty(s)` | Returns TRUE if there are no elements, else FALSE |
| `Element Pop(s)` | If `IsEmpty(s)`, return; else remove and return the top element |

**Exam point:** ADT = **data + operations**, with implementation hidden. The same stack ADT can be implemented using an array or a linked list.

---

# 6. Stack Using Dynamic Arrays (Array Doubling)

## 6.1 The problem with a fixed array

A fixed-size array stack cannot grow. If it fills up, further pushes cause overflow even though the program might have more memory available.

## 6.2 The solution: array doubling

Start with some capacity (the PDF uses 5). When the stack is full:

1. Allocate a new array of **double** the capacity using `realloc`.
2. Copy the old elements ( `realloc` does this automatically).
3. Update `capacity`.
4. Continue pushing.

```c
int capacity = 5;
int *s;

void push(int item, int *top) {
    if (*top == capacity - 1) {
        // stack full → double the size
        s = (int *) realloc(s, 2 * capacity * sizeof(int));
        capacity = capacity * 2;
    }
    *top = *top + 1;
    s[*top] = item;
}
```

`pop` and `display` are the same as before, except they use the global `s` and `capacity`.

In `main`:

```c
s = (int *) malloc(capacity * sizeof(int));
...
case 4:
    free(s);
    exit(0);
```

## 6.3 Why doubling?

If you increase the capacity by only 1 each time, every push may require copying the whole array → very slow. Doubling means copies happen rarely, so the **average** cost per push is constant (amortised O(1)).

**Exam points:**
- Dynamic stack uses the **heap**.
- `realloc` preserves the old contents.
- Capacity doubles: 5 → 10 → 20 → 40 ...
- `free(s)` before exit to avoid a memory leak.

### Check yourself

1. What is array doubling? **When full, allocate twice the capacity and copy the elements.**
2. Which function is used to resize? **`realloc`.**
3. Does `realloc` preserve old data? **Yes.**
4. What is the new capacity if the old is 20? **40.**

---

# 7. Expressions

## 7.1 Three types of expressions

### Infix

An operator is **between** two operands.

Example:

```
(a + b) / (c - d)
```

This is the form humans normally write.

### Postfix (suffix, Reverse Polish)

An operator **follows** its two operands.

Example:

```
a b + c d - /
```

### Prefix (Polish)

An operator **precedes** its two operands.

Example:

```
/ + a b - c d
```

**Key idea:** in postfix and prefix, the operator and operands define the order of operations **without parentheses**. There is no ambiguity, so no repeated scanning is needed.

**Exam point:**
- Infix: operand operator operand → `a + b`
- Postfix: operand operand operator → `a b +`
- Prefix: operator operand operand → `+ a b`

## 7.2 Why postfix/prefix are useful

Evaluating infix requires repeated scanning left-to-right and right-to-left because of operator precedence and parentheses. Parentheses make it more complex.

In postfix/prefix:

- no parentheses,
- no precedence rules during evaluation,
- one left-to-right scan is enough,
- time is less.

This is why compilers convert infix to postfix/prefix before evaluation.

### Check yourself

1. Which expression type has the operator before the operands? **Prefix.**
2. Which has the operator after? **Postfix.**
3. Which form needs parentheses? **Infix.**
4. What is another name for postfix? **Reverse Polish notation.**

---

# 8. Converting Infix to Postfix and Prefix

## 8.1 The substitution method (used in the PDF)

The PDF solves conversions by repeatedly replacing a subexpression with a temporary name `T1`, `T2`, ...

For **postfix**, combine operands as `left right operator`.

For **prefix**, combine as `operator left right`.

### Problem 1: `((6 + (3 - 2) * 4) / 5 + 7)`

**Postfix:**

| Step | Expression | Temporary |
|---|---|---|
| 1 | `((6 + (3 - 2) * 4) / 5 + 7)` | `T1 = 3 2 -` |
| 2 | `((6 + T1 * 4) / 5 + 7)` | `T2 = T1 4 *` |
| 3 | `((6 + T2) / 5 + 7)` | `T3 = 6 T2 +` |
| 4 | `(T3 / 5 + 7)` | `T4 = T3 5 /` |
| 5 | `(T4 + 7)` | `T5 = T4 7 +` |

Expanding:

```
T1 = 3 2 -
T2 = 3 2 - 4 *
T3 = 6 3 2 - 4 * +
T4 = 6 3 2 - 4 * + 5 /
T5 = 6 3 2 - 4 * + 5 / 7 +
```

**Postfix answer:** `6 3 2 - 4 * + 5 / 7 +`

**Prefix:**

```
T1 = - 3 2
T2 = * - 3 2 4
T3 = + 6 * - 3 2 4
T4 = / + 6 * - 3 2 4 5
T5 = + / + 6 * - 3 2 4 5 7
```

**Prefix answer:** `+ / + 6 * - 3 2 4 5 7`

### Problem 2: `a + b * c ^ d`

**Postfix:**

```
T1 = c d ^
T2 = b T1 *
T3 = a T2 +
```

Answer: `a b c d ^ * +`

**Prefix:**

```
T1 = ^ c d
T2 = * b ^ c d
T3 = + a * b ^ c d
```

Answer: `+ a * b ^ c d`

## 8.2 Converting prefix/postfix back to infix

### Prefix → infix: scan **right to left**

**Problem 3: `+ - A B C`**

```
T1 = A - B
T2 = T1 + C
```

Answer: `(A - B) + C` or `A - B + C`.

**Problem 4: `+ A - B C`**

```
T1 = B - C
T2 = A + T1
```

Answer: `A + (B - C)`.

### Postfix → infix: scan **left to right**

**Problem 5: `A B + C -`**

```
T1 = A + B
T2 = T1 - C
```

Answer: `(A + B) - C`.

**Problem 6: `A B C + -`**

```
T1 = B + C
T2 = A - T1
```

Answer: `A - (B + C)`.

**Exam tip:** for prefix→infix, scanning right-to-left makes the **rightmost** operator the first one applied. For postfix→infix, scanning left-to-right does the same. Parentheses are added based on the subexpression, not on precedence.

### Check yourself

1. Convert `a b + c *` to infix. **`(a + b) * c`.**
2. Convert `* + a b c` to infix. **`(a + b) * c`.**
3. Convert `a + b * c` to postfix. **`a b c * +`.**
4. Convert `(a + b) * (c - d)` to postfix. **`a b + c d - *`.**

---

# 9. Infix to Postfix Using a Stack

## 9.1 The precedence table

The PDF uses two precedence functions:

- **Input precedence** — precedence of the symbol as it arrives from the infix expression.
- **Stack precedence** — precedence of the symbol while it is on the stack.

| Symbol | Input precedence | Stack precedence |
|---|---|---|
| `+`, `-` | 1 | 2 |
| `*`, `/`, `%` | 3 | 4 |
| `^`, `$` | 6 | 5 |
| Operands | 7 | 8 |
| `(` | 9 | 0 |
| `)` | 0 | — |
| `#` | — | -1 |

**Why two different values?**

- `+`, `-`, `*`, `/`, `%` are **left associative**. When a same-precedence operator arrives, the older one on the stack should be popped first. So **input < stack**.
- `^` (exponentiation) is **right associative**. The newer operator should bind first, so it should be pushed rather than popping the older one. So **input > stack**.
- `(` has the **highest input precedence** (9) so it is always pushed, but **stack precedence 0** so nothing is popped because of it.
- `)` has input precedence 0, so it pops everything until `(`.
- `#` is the bottom-of-stack marker with stack precedence -1.

**Note from the PDF:** `+`, `-`, `*`, `/`, `%` are left associative; `^` and `$` are right associative.

## 9.2 General procedure

**Step 1:** Get the next input symbol.

**Step 2:** While the precedence of the symbol on top of the stack is **greater than** the precedence of the current input symbol, pop the stack and place the popped symbol in the postfix expression.

**Step 3:** If the stack precedence and input precedence are **different**, push the current symbol. If they are **equal**, delete the top symbol (this handles `)` matching `(`).

**Step 4:** Repeat Steps 1–3 until the end of input.

**Step 5:** Pop all remaining symbols (except `#`) and place them in the postfix expression.

**Why Step 5 is needed:** for an unparenthesised expression, some operators remain on the stack at the end.

**Important:** operands are placed **directly** in the postfix output; they are not pushed onto the stack. The stack holds only operators and parentheses.

## 9.3 Worked trace: `(6 + (5 - 3) * 4)`

| Input | Stack (top at right) | Action | Postfix so far |
|---|---|---|---|
| `(` | `#(` | push `(` | |
| `6` | `#(` | operand → output | `6` |
| `+` | `#(+` | push `+` | `6` |
| `(` | `#(+(` | push `(` | `6` |
| `5` | `#(+(` | output | `6 5` |
| `-` | `#(+(-` | push `-` | `6 5` |
| `3` | `#(+(-` | output | `6 5 3` |
| `)` | `#(+` | pop `-`, then delete `(` | `6 5 3 -` |
| `*` | `#(+*` | push `*` | `6 5 3 -` |
| `4` | `#(+*` | output | `6 5 3 - 4` |
| `)` | `#` | pop `*`, pop `+`, delete `(` | `6 5 3 - 4 * +` |
| end | `#` | stop | **`6 5 3 - 4 * +`** |

**Check:** `(6 + (5 - 3) * 4)` = `6 + 2 * 4` = `6 + 8` = `14`.
Postfix evaluation: `5 3 -` = 2; `2 4 *` = 8; `6 8 +` = 14. ✓

## 9.4 Worked trace: `6 + 4 * 3`

| Input | Stack | Action | Postfix |
|---|---|---|---|
| `6` | `#` | output | `6` |
| `+` | `#+` | push | `6` |
| `4` | `#+` | output | `6 4` |
| `*` | `#+*` | push (`*` input 3 > `+` stack 2) | `6 4` |
| `3` | `#+*` | output | `6 4 3` |
| end | `#` | pop `*`, pop `+` | **`6 4 3 * +`** |

**Check:** `6 + 4 * 3 = 6 + 12 = 18`.
Postfix: `4 3 *` = 12; `6 12 +` = 18. ✓

## 9.5 Worked trace: `((6 + (3 - 2) * 4) / 5 + 7)`

| Input | Stack | Action | Postfix |
|---|---|---|---|
| `(` | `#(` | push | |
| `(` | `#((` | push | |
| `6` | `#((` | output | `6` |
| `+` | `#((+` | push | `6` |
| `(` | `#((+(` | push | `6` |
| `3` | `#((+(` | output | `6 3` |
| `-` | `#((+(-` | push | `6 3` |
| `2` | `#((+(-` | output | `6 3 2` |
| `)` | `#((+` | pop `-`, delete `(` | `6 3 2 -` |
| `*` | `#((+*` | push | `6 3 2 -` |
| `4` | `#((+*` | output | `6 3 2 - 4` |
| `)` | `#(` | pop `*`, pop `+`, delete `(` | `6 3 2 - 4 * +` |
| `/` | `#(/` | push | `6 3 2 - 4 * +` |
| `5` | `#(/` | output | `6 3 2 - 4 * + 5` |
| `+` | `#(+` | pop `/` (stack 4 > input 1), push `+` | `6 3 2 - 4 * + 5 /` |
| `7` | `#(+` | output | `6 3 2 - 4 * + 5 / 7` |
| `)` | `#` | pop `+`, delete `(` | `6 3 2 - 4 * + 5 / 7 +` |

**Postfix answer:** `6 3 2 - 4 * + 5 / 7 +`

## 9.6 Program to convert infix to postfix

The PDF gives a C program with:

- `input_precedence(char symbol)` — returns 1, 3, 6, 7, 9, 0 based on the table.
- `stack_precedence(char symbol)` — returns 2, 4, 5, 8, 0, -1.
- `push` and `pop` for a character stack.
- `infix_postfix(infix, postfix)` — scans the input, uses the stack, writes the output.
- `main` reads the infix string and prints the postfix string.

**Core loop (corrected logic):**

```c
push('#', &top, s);

for (i = 0; i < n; i++) {
    symbol = infix[i];

    if (isOperand(symbol)) {
        postfix[j++] = symbol;          // operands go straight to output
    } else {
        while (stack_precedence(s[top]) > input_precedence(symbol)) {
            postfix[j++] = pop(&top, s);
        }
        if (stack_precedence(s[top]) != input_precedence(symbol)) {
            push(symbol, &top, s);
        } else {
            pop(&top, s);               // equal precedence: remove '(' or ')'
        }
    }
}

while (s[top] != '#')
    postfix[j++] = pop(&top, s);

postfix[j] = '\0';
```

> **Note on the printed program:** the PDF's `infix_postfix` contains a likely typo — inside the `if` it calls `push(symbol)` and then immediately `pop()`, which would delete the symbol just pushed. The correct logic is the one shown above: push only when precedences differ; pop only when they are equal. Also, the PDF's code does not explicitly check for operands, so the `default` precedence values (7/8) are used to let operands pass through. In an exam, write the standard algorithm, not the typo.

**Exam points:**
- `#` is pushed first as a sentinel.
- Operands go directly to output.
- Higher stack precedence → pop.
- Equal precedence → pop (used for `)`).
- At the end, pop until `#`.

### Check yourself

1. Why does `(` have input precedence 9 but stack precedence 0? **So it is always pushed and never causes a pop while on the stack.**
2. Why does `)` have input precedence 0? **So it pops all operators until `(`.**
3. Convert `A + B * C` to postfix. **`A B C * +`.**
4. Convert `A * (B + C)` to postfix. **`A B C + *`.**

---

# 10. Evaluation of Postfix Expression

## 10.1 Why postfix is easier to evaluate

Infix requires repeated scanning because of precedence and parentheses. Postfix has no parentheses and the order is already decided, so **one left-to-right scan** is enough.

## 10.2 Algorithm

**Step 1:** Scan from left to right until an operator is found.

**Step 2:** Take the **immediate two left operands**.

**Step 3:** Perform the operation.

**Step 4:** Replace the operands and operator with the result.

**Step 5:** Repeat until the end of input.

**Stack version:**

```
for each symbol:
    if operand:
        push(symbol)
    else:
        op2 = pop()
        op1 = pop()
        result = op1 <operator> op2
        push(result)
return pop()
```

**Critical order:** the **first** popped value is `op2`, the **second** is `op1`. For non-commutative operators like `-` and `/`, this matters:

```
op1 - op2, not op2 - op1
op1 / op2, not op2 / op1
```

## 10.3 Worked trace: `6 3 2 - 5 * +`

This is the postfix form of `(6 + (3 - 2) * 5)`.

| Symbol | op2 | op1 | Result | Stack after |
|---|---|---|---|---|
| `6` | | | | `6` |
| `3` | | | | `6 3` |
| `2` | | | | `6 3 2` |
| `-` | 2 | 3 | `3 - 2 = 1` | `6 1` |
| `5` | | | | `6 1 5` |
| `*` | 5 | 1 | `1 * 5 = 5` | `6 5` |
| `+` | 5 | 6 | `6 + 5 = 11` | `11` |
| end | | | return `11` | |

**Answer: 11.**

## 10.4 Program for postfix evaluation

The PDF's `evaluate(char postfix[])`:

- Uses an integer stack.
- For each symbol:
  - `+`, `-`, `*`, `/`, `%`, `^`/`$` → pop two, compute, push result.
  - default (digit) → push `symbol - '0'`.
- Returns the final popped value.

**Character-to-integer conversion:**

```c
symbol - '0'
```

Example: `'6' - '0' = 54 - 48 = 6` (ASCII values).

For exponentiation:

```c
res = (int) pow((double)op1, (double)op2);
```

**Limitation:** this program handles **single-digit** operands only. For multi-digit numbers, you need to read consecutive digits and form the number.

**Exam points:**
- Postfix evaluation uses one stack.
- Pop order: `op2` first, then `op1`.
- Operands are pushed; operators pop two and push one.
- The final stack contains exactly one value — the answer.

### Check yourself

1. Evaluate `5 3 + 2 *`. **16.**
2. Evaluate `8 2 / 3 -`. **1.**
3. Evaluate `2 3 4 * +`. **14.**
4. In `8 2 /`, which is `op1` and which is `op2`? **`op1 = 8`, `op2 = 2`; result `8 / 2 = 4`.**

---

# 11. Multiple Stacks in a Single Array

## 11.1 Two stacks in one array

Use one array `s[0 ... stacksize-1]`:

- **Stack 1** starts at the **left end** (`s[0]`) and grows **right**.
- **Stack 2** starts at the **right end** (`s[stacksize-1]`) and grows **left**.

Initial values:

```c
top1 = -1;            // stack 1 is empty
top2 = stacksize;     // stack 2 is empty
```

- Stack 1 push: `top1++`, then `s[top1] = item`.
- Stack 2 push: `top2--`, then `s[top2] = item`.
- **Overflow condition:** `top1 == top2 - 1` → the two tops have met; the array is full.

```
top1 → [ ][ ][ ][ ][ ][ ][ ][ ]
                 ↑
                top2
```

Stack 1 grows toward the right; stack 2 grows toward the left. This uses space efficiently because both share the same free region.

**Exam point:** the two stacks meet in the middle; overflow happens only when **all** array slots are used, not when one stack reaches the middle.

## 11.2 Program for two stacks

```c
void push1(int item, int *top1, int *top2, int s[]) {
    if (*top1 == *top2 - 1) {
        printf("Stack overflow\n");
        return;
    }
    *top1 = *top1 + 1;
    s[*top1] = item;
}

void push2(int item, int *top1, int *top2, int s[]) {
    if (*top1 == *top2 - 1) {
        printf("Stack overflow\n");
        return;
    }
    *top2 = *top2 - 1;
    s[*top2] = item;
}

int pop1(int *top1, int s[]) {
    if (*top1 == -1)
        return -1;
    int item = s[*top1];
    *top1 = *top1 - 1;
    return item;
}

int pop2(int *top2, int s[]) {
    if (*top2 == stacksize)
        return -1;
    int item = s[*top2];
    *top2 = *top2 + 1;
    return item;
}
```

**Display:**

- Stack 1: `for (i = 0; i <= top1; i++)`
- Stack 2: `for (i = top2; i < stacksize; i++)`

## 11.3 More than two stacks in one array

For `n` stacks, there is no obvious "middle" to grow toward. Two possible solutions from the PDF:

1. **Divide the array into `n` segments based on expected sizes** of the stacks.
2. **Divide the array into `n` equal segments.**

For equal segments:

```c
#define stack_size 100
#define max_stacks 10

int s[stack_size];
int n;                  // number of stacks
int top[max_stacks];
int boundary[max_stacks];

for (j = 0; j <= n; j++)
    top[j] = boundary[j] = stack_size / n * j - 1;
```

- `boundary[i]` marks the position just before stack `i` starts.
- `top[i]` is the current top of stack `i`.
- Stack `i` occupies positions `boundary[i] + 1` through `boundary[i+1]`.

**Push for stack `i`:**

```c
if (top[i] == boundary[i+1])
    printf("Stack overflow\n");
else {
    top[i] = top[i] + 1;
    s[top[i]] = item;
}
```

**Pop for stack `i`:**

```c
if (top[i] == boundary[i])
    return -1;
else {
    item = s[top[i]];
    top[i] = top[i] - 1;
    return item;
}
```

**Display for stack `i`:**

```c
for (j = boundary[i] + 1; j <= top[i]; j++)
    printf("%d\n", s[j]);
```

## 11.4 The "stack full" problem for `n` stacks

The condition `top[i] == boundary[i+1]` only means **stack `i` ran out of its segment**, not that the whole array is full. There may be free space in other segments.

Two methods to handle this:

### Right check

Find the **least** `j` such that `i < j < n` and there is free space between stacks `j` and `j+1`. If such a `j` exists, move stacks `i+1, i+2, ..., j` **one position right**. This creates space between stacks `i` and `i+1`.

### Left check

If no such `j` exists, find the **largest** `j` such that `0 < j < i` and there is free space between stacks `j` and `j+1`. If such a `j` exists, move stacks `j+1, j+2, ..., i` **one position left**. This also creates space between stacks `i` and `i+1`.

### If neither works

All memory is used; the stack is genuinely full and no element can be added.

**Exam point:** for multiple stacks, overflow of one segment does not necessarily mean the array is full; shifting may free space.

### Check yourself

1. For two stacks in one array, what are the initial `top1` and `top2`? **-1 and `stacksize`.**
2. When is the array full? **When `top1 == top2 - 1`.**
3. Which direction does stack 1 grow? **Right (increasing indices).**
4. Which direction does stack 2 grow? **Left (decreasing indices).**
5. In the `n`-stack equal division, what does `boundary[i]` represent? **The position just before stack `i` begins.**

---

# 12. Stack Applications with Code

## 12.1 Reverse a string using a stack

**Idea:** push every character of the string onto a stack. Because a stack is LIFO, popping gives the characters in reverse order.

```c
void reverse_string(char str[], char revstr[]) {
    int top = -1, n, i;
    char s[stacksize], symbol;

    n = strlen(str);

    for (i = 0; i < n; i++) {
        symbol = str[i];
        push(symbol, &top, s);
    }

    for (i = 0; i < n; i++)
        revstr[i] = pop(&top, s);

    revstr[i] = '\0';
}
```

**Example:** `"HELLO"` → push H,E,L,L,O → pop O,L,L,E,H → `"OLLEH"`.

**Exam point:** reversal works because the **last pushed** character is the **first popped**.

## 12.2 Check whether a string is a palindrome

**Idea:**

1. Push all characters onto the stack.
2. Pop them one by one and compare with the original string from the beginning.
3. If any character differs → not a palindrome.
4. If all match → palindrome.

```c
int check_palindrome(char str[]) {
    int top = -1, n, i;
    char s[stacksize], symbol, s1, s2;

    n = strlen(str);

    for (i = 0; i < n; i++) {
        symbol = str[i];
        push(symbol, &top, s);
    }

    for (i = 0; i < n; i++) {
        s1 = str[i];
        s2 = pop(&top, s);
        if (s1 != s2)
            return 0;    // not a palindrome
    }
    return 1;            // palindrome
}
```

**Example:** `"MADAM"` → reverse is also `"MADAM"` → palindrome.
`"HELLO"` → reverse `"OLLEH"` → not a palindrome.

## 12.3 Check whether a number is a palindrome

Same idea, but the input is a number read as a string.

- Push each digit (converted to an integer using `symbol - '0'`).
- Pop and compare with the digits from the left.
- If all match → palindrome.

```c
push(symbol - '0', &top, s);

s1 = str[i] - '0';
s2 = pop(&top, s);
if (s1 != s2)
    return 0;
```

**Example:** `12321` → palindrome. `12345` → not.

**Exam point:** the stack reverses the order; a palindrome reads the same forwards and backwards, so comparing the original with the reversed order is the test.

### Check yourself

1. Why does a stack reverse a string? **LIFO order.**
2. What is the time complexity of the stack palindrome check? **O(n).**
3. What extra space does it use? **O(n) for the stack.**
4. Can you check a palindrome without a stack? **Yes — two pointers from both ends, O(1) space. The stack version is for practice.**

---

# Module 1 Part B — Question Bank

## 1–2 mark questions

1. Define a stack.
2. Why is a stack called LIFO?
3. Define push and pop.
4. What is stack overflow?
5. What is stack underflow?
6. What is the initial value of `top`?
7. Write the full and empty conditions for an array stack.
8. What is an activation record?
9. Name the four fields of an activation record.
10. What is a system stack?
11. Define stack ADT.
12. What is array doubling?
13. Define infix, postfix and prefix expressions.
14. Give the postfix form of `a + b * c`.
15. Give the prefix form of `a + b * c`.
16. What is the input precedence of `(` and `)`?
17. What is the stack precedence of `#`?
18. Why is `^` right associative?
19. What is the postfix form of `(a + b) * c`?
20. In postfix evaluation, which operand is popped first?
21. Why is postfix evaluation easier than infix?
22. How many stacks are used in postfix evaluation?
23. How are two stacks represented in one array?
24. What is the overflow condition for two stacks in one array?
25. What is the purpose of `boundary[]` in multiple stacks?
26. How is a string reversed using a stack?
27. How is a palindrome checked using a stack?

## 5-mark questions

1. Explain the basic operations of a stack with a diagram.
2. Explain the array implementation of a stack with push, pop and display functions.
3. Explain the system stack and activation record with a diagram.
4. Explain the stack ADT.
5. Explain the dynamic array implementation of a stack (array doubling).
6. Explain infix, postfix and prefix expressions with examples.
7. Explain the conversion of infix to postfix using a stack, with a trace.
8. Explain the precedence table used in infix-to-postfix conversion.
9. Explain the evaluation of a postfix expression with a trace.
10. Explain how to represent two stacks in a single array.
11. Explain the `n`-stack representation in a single array.
12. Explain the right-check and left-check methods for multiple stacks.
13. Explain string reversal using a stack.
14. Explain palindrome checking using a stack.
15. List and explain any five applications of stacks.

## 10-mark questions

1. Explain stack operations, array implementation and dynamic array implementation in detail.
2. Explain the system stack, activation record and function-call mechanism in detail.
3. Explain infix-to-postfix conversion: precedence table, algorithm, trace and program.
4. Explain postfix evaluation: algorithm, trace and program.
5. Explain multiple stacks in a single array, including two-stack and `n`-stack representations.
6. Explain any five stack applications with code/logic.

---

# Common exam mistakes in Part B

1. **Incrementing `top` after storing in push.** Increment first.
2. **Decrementing `top` before reading in pop.** Read first.
3. **Saying "stack overflow" when popping.** That is underflow.
4. **Forgetting that operands are not pushed in infix→postfix.** They go straight to output.
5. **Using the wrong pop order in postfix evaluation.** First pop = `op2`, second = `op1`.
6. **Treating `^` as left associative.** It is right associative, so input precedence > stack precedence.
7. **Forgetting the `#` sentinel.** It marks the bottom of the operator stack.
8. **Saying two stacks in one array overflow when one reaches the middle.** They overflow only when the tops meet.
9. **Forgetting to free dynamically allocated memory.** Call `free(s)` before exit.
10. **Confusing prefix and postfix.** Prefix: operator first. Postfix: operator last.
11. **Forgetting that a stack is linear.** It is not a non-linear structure.
12. **Thinking recursion uses a separate "recursion stack."** It uses the same system stack.
