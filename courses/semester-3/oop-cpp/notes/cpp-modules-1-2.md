# C++ Modules 1 & 2 — Complete Exam Notes (with programs)

**Subject:** Object Oriented Programming using C++ (BCS306B pattern)

**Coverage:** Module 1 (all three PDFs' basics + classes) and Module 2 (classes, objects, dynamic memory)

**Source material:** `Module 1.pdf`, `Module 1- c++.pdf`, `Module 2.pdf` + the Exercise / Interview question sets inside them.

> All 19 programs below were compiled with `g++ -std=c++17 -Wall -Wextra` and run. Real outputs are shown.
> Copies are in `cpp_prep/` so you can run them yourself.

---

## How to score in this paper

| Question type | What the examiner wants |
|---|---|
| 2 marks | Exact definition + 1 example line. No stories. |
| 5 marks | Definition → syntax → small program/snippet → 2–3 point difference/advantage. |
| 10 marks | Definition → features/rules in points → labelled program → output → conclusion/advantage. |

**Golden rule:** in this subject, a program without its **output** and a definition without an **example** loses marks. Every long answer below follows that pattern.

**Terminology the slides sometimes get wrong (write the correct version):**
- `cout << x` → `<<` is the **insertion (output) operator**; `cin >> x` → `>>` is the **extraction (input) operator**.
- A constructor **initializes** an object. Memory is allocated by the object definition / `new`, not by the constructor.
- Correct headers are `<iostream>`, not `<iostream.h>`. `main` returns `int`, not `void`.
- `float Circle::_pi = 3.14f;` — no space between `3.14` and `f`.

---

# PART A — MODULE 1

## 1. What is Object-Oriented Programming?

**Definition:** OOP is a programming methodology that designs software around **objects** — entities that bundle **data (state)** and **functions (behaviour)** — instead of around functions and logic.

**Object = Data + Functions that operate on that data.**

Bank-account analogy:
- Data: account number, holder name, balance
- Functions: deposit(), withdraw(), checkBalance()

So a bank account object carries both *what it knows* and *what it can do*. That is the whole idea of OOP.

### 1.1 POP vs OOP (almost guaranteed question)

| Procedure-Oriented (POP) | Object-Oriented (OOP) |
|---|---|
| Focus on functions/procedures | Focus on objects and classes |
| Data and functions are separate | Data and functions are bundled |
| Top-down approach | Bottom-up approach |
| No access specifiers; data is often global | public / private / protected control access |
| Data less secure | Data more secure (hidden inside objects) |
| No inheritance/polymorphism | Supports inheritance, polymorphism, etc. |
| Suited to small, simple programs | Suited to large, complex programs |
| Examples: C, Pascal, COBOL | Examples: C++, Java, Python, C# |

*Bottom-up* means: build classes/objects first → combine them → complete program.

### 1.2 The eight building blocks / features of OOP

1. **Class** — user-defined data type; a blueprint holding data members + member functions.
2. **Object** — an instance of a class; the real entity with memory.
3. **Encapsulation** — wrapping data and the functions that manipulate it into one unit (the class).
4. **Abstraction** — show only the essential interface; hide the implementation details.
5. **Polymorphism** — "many forms": one name behaving differently (function overloading, operator overloading, virtual functions).
6. **Inheritance** — a derived class acquires the properties of a base class; gives reusability.
7. **Dynamic binding** — the function to call is decided at **run time** (virtual functions); the opposite, static binding, is fixed at compile time.
8. **Message passing** — objects communicate by calling each other's member functions.

**Exam line:** Encapsulation is *how* data hiding is achieved; abstraction is *what* is exposed.

### 1.3 C vs C++

| C | C++ |
|---|---|
| Procedure-oriented | Object-oriented |
| Top-down | Bottom-up |
| `scanf` / `printf` | `cin` / `cout` |
| `<stdio.h>` | `<iostream>` |
| No class, object, inheritance, polymorphism | Supports all of them |
| Format specifiers (`%d`, `%f`) required | Not required; type-safe I/O |
| Data hiding not possible | Achieved with `private` |
| Limited reusability | Reusable via inheritance/templates |

**Where C++ is used:** operating systems, games, GUI apps (Photoshop), browsers (Chrome/Firefox), embedded systems, banking software (Finacle), compilers, MySQL.

---

## 2. Writing a simple C++ program

```cpp
int main()          // function definition
{
    return 0;       // 0 = success
}
```

A function definition has **four elements**:
1. return type → `int`
2. function name → `main`
3. parameter list in parentheses → `()` (may be empty, cannot be omitted)
4. function body in braces → `{ ... }`

The OS starts a C++ program by calling `main`. The value returned to the OS is a **status indicator**: `0` = success, non-zero = some error (system-defined).

### 2.1 General form of a C++ program

```cpp
#include <iostream>              // headers
using namespace std;             // optional

class Base { ... };              // base-class declarations
class Derived : public Base { ... };

int helper(int);                 // non-member function prototypes

int main()                       // main
{
    // ...
    return 0;
}

int helper(int x) { ... }        // non-member function definitions
```

In large projects class declarations go into header files (`.h`) and are `#include`d, but this organisation stays the same.

### 2.2 Compiling and executing

- Source file suffix: `.cpp` (e.g. `binary_search.cpp`).
- GNU compiler: `g++ prog1.cpp` → produces executable `prog1` (`./prog1` to run).
- Other compilers: Clang, MSVC.

**Full flow (draw this diagram if asked):**

```
source.cpp → Preprocessor → Compiler → Assembler → object code (.o)
           → Linker (+ libraries) → executable (.exe / a.out) → Loader → RAM → run
```

- **Linker:** combines object code with required library code to make the executable.
- **Loader:** loads the executable into main memory (RAM) for execution.

---

## 3. A first look at input/output

C++ does **not** define I/O statements; the standard library `<iostream>` provides them.

- **Stream** = a sequence of characters flowing between the program and an I/O device.
- `istream` → input type; object **`cin`** (standard input, keyboard).
- `ostream` → output type; objects **`cout`** (standard output), **`cerr`** (standard error, unbuffered), **`clog`** (buffered general log).
- `endl` → inserts a newline **and flushes** the stream.
- All standard-library names live in the namespace **`std`**, hence `std::cout` or `using namespace std;`.
- **Namespace** = named container used to organise names and avoid collisions.

```cpp
#include <iostream>
int main()
{
    std::cout << "Enter two numbers:" << std::endl;
    int v1 = 0, v2 = 0;
    std::cin >> v1 >> v2;
    std::cout << "The sum of " << v1 << " and " << v2
              << " is " << v1 + v2 << std::endl;
    return 0;
}
```

**Output**
```
Enter two numbers:
5 6
The sum of 5 and 6 is 11
```

`<<` and `>>` return their left operand (the stream), which is why they can be **chained**.

---

## 4. Variables and compound types

**Variable:** a named memory location whose value can change during execution. Every variable has a **type**, which decides:
- size and layout of its memory,
- range of values it can hold,
- operations that can be applied to it.

**Definition** allocates storage; **declaration** only announces the name.

```cpp
int i;                       // declared + defined, uninitialized (garbage)
int j = 10;                  // defined and initialized
double price = 109.99, discount = price * 0.16;   // definition may use earlier names
```

A **compound type** is defined in terms of another type. The two important ones here are **references** and **pointers**.

| Reference `int &r = n;` | Pointer `int *p = &n;` |
|---|---|
| Another **name** (alias) for an existing object | Holds the **address** of an object |
| Must be initialized when declared | Can be declared uninitialized / set to `nullptr` |
| Cannot be null | Can be null |
| Cannot be re-bound to another object | Can point to different objects |
| Accessed directly (`r`) | Dereferenced with `*p` |
| No separate memory needed (conceptually) | Occupies memory to store the address |

### Program: references and pointers

```cpp
#include <iostream>
using namespace std;

int main()
{
    int n = 10;

    int &r = n;          // r is another name for n
    r = 42;              // changes n itself
    cout << "n = " << n << ", r = " << r << endl;

    int *p = &n;         // p stores the address of n
    cout << "address of n = " << p << endl;
    cout << "value via *p = " << *p << endl;
    *p = 99;             // changes n through the pointer
    cout << "n after *p=99: " << n << endl;

    const int &cr = n;   // read-only reference (no copy)
    cout << "const ref reads: " << cr << endl;

    int *q = nullptr;    // safe empty pointer
    cout << "q is " << (q == nullptr ? "null" : "not null") << endl;
    return 0;
}
```

**Output**
```
n = 42, r = 42
address of n = 0x7ffcb7200194
value via *p = 42
n after *p=99: 99
const ref reads: 99
q is null
```

> The exact address changes on every run; that is expected.

**Remember:** a reference must be initialized, cannot be null, and cannot be made to refer to another variable afterwards.

---

## 5. Statements

**Statement:** a complete instruction commanding the computer to do something. Most end with `;`.

**Expression:** a combination of operands and operators that yields a value (e.g. `ival + 5`). Adding a semicolon turns it into an **expression statement** (`ival + 5;` — legal but useless; `cout << ival;` — useful).

| Kind | Meaning | Example |
|---|---|---|
| Expression statement | expression + `;` | `cout << ival;` |
| Null statement | just `;`, intentionally empty | `;` (comment it!) |
| Compound / block | statements + declarations in `{ }` | function body, loop body |
| Control statement | if, switch, loops, jumps | `if (x > 0) ...` |

A block is **not** terminated by a semicolon. Names declared in a block are visible only there and in nested blocks.

**Statement scope:** a variable declared in the control structure of `if`/`switch`/`while`/`for` is visible only inside that statement.

```cpp
while (int i = get_num())     // i created and initialized each iteration
    cout << i << endl;
i = 0;                         // ERROR: i not visible here
```

### 5.1 Conditional statements

**`if` / `if-else`:**

```cpp
if (condition)
    statement;
else
    statement2;
```

**Dangling else:** an `else` binds to the **nearest unmatched `if`**, regardless of indentation.

```cpp
if (grade % 10 >= 3)
    if (grade % 10 > 7)
        lettergrade += '+';
    else
        lettergrade += '-';   // actually belongs to the INNER if -> logic bug
```

Fix: use braces so the `else` clearly belongs to the outer `if`.

**`switch`:** selects among fixed integral alternatives.

```cpp
switch (expression) {      // integral or char, not float/string
    case value1:
        // ...
        break;
    case value2:
        // ...
        break;
    default:
        // executes when no case matches
}
```

- Omitting `break` causes **fall-through** into the next case.
- `default` is optional and can appear anywhere, usually last.

### 5.2 Iterative statements

| Loop | Test | Minimum runs | Best used when |
|---|---|---|---|
| `while` | before body (entry-controlled) | 0 | count unknown, condition-driven |
| `do-while` | after body (exit-controlled) | 1 | body must run at least once (menus) |
| `for` | before body | 0 | number of repetitions known |

```cpp
while (condition) statement;
do { statement; } while (condition);
for (init; condition; update) statement;
```

### 5.3 Jump statements

- **`break`** — leave the nearest loop/switch immediately.
- **`continue`** — skip the rest of this iteration, go to the next.
- **`goto`** — unconditional jump (avoid; unstructured).
- **`return`** — leave the function, optionally with a value.

### Program: all loops + break/continue

```cpp
#include <iostream>
using namespace std;

int main()
{
    int sum = 0, val = 1;
    while (val <= 10) { sum += val; ++val; }
    cout << "while sum 1..10 = " << sum << endl;

    sum = 0;
    for (int i = 1; i <= 10; ++i) sum += i;
    cout << "for   sum 1..10 = " << sum << endl;

    int n = 10;
    do { cout << n << " "; --n; } while (n >= 0);
    cout << endl;

    for (int i = 1; i <= 10; ++i) {
        if (i == 8) break;
        if (i % 2 == 0) continue;
        cout << i << " ";
    }
    cout << endl;
    return 0;
}
```

**Output**
```
while sum 1..10 = 55
for   sum 1..10 = 55
10 9 8 7 6 5 4 3 2 1 0
1 3 5 7
```

### Program: if-else, dangling else, switch

```cpp
#include <iostream>
using namespace std;

int main()
{
    int marks;
    cout << "Enter marks: ";
    cin >> marks;

    if (marks >= 90)      cout << "Grade A\n";
    else if (marks >= 75) cout << "Grade B\n";
    else if (marks >= 60) cout << "Grade C\n";
    else                  cout << "Fail\n";

    char op;
    cout << "Enter operator (+ or -): ";
    cin >> op;
    switch (op) {
        case '+': cout << "You chose addition\n"; break;
        case '-': cout << "You chose subtraction\n"; break;
        default:  cout << "Unknown operator\n";
    }

    int grade = 68;
    if (grade >= 60) {
        if (grade >= 90) cout << "A\n";
    } else {
        cout << "Fail\n";     // braces: else clearly belongs to outer if
    }
    return 0;
}
```

**Output (input `88`, `+`)**
```
Enter marks: Grade B
Enter operator (+ or -): You chose addition
```

---

## 6. Functions in C++

**Function:** a named block of code that performs a task; executed by **calling** it.

```cpp
return_type function_name(parameter list)
{
    // body
}

int result = add(10, 20);     // call; 10,20 are arguments
```

- **Parameters** are the names in the definition; **arguments** are the values supplied at the call.
- The call operator is the pair `()`.
- Functions can be **overloaded**: same name, different parameter lists.
- Parameter list: may be empty but the parentheses **cannot be omitted**; no two parameters may share a name; the type must be repeated (`int f(int a, int b)`, not `int f(int a, b)`); every parameter needs an argument at the call.
- Return type can be `void` (nothing) but **cannot be an array or a function type**; it *can* be a pointer to an array or function.

**Scope vs lifetime (favourite 2-mark question):**
- **Scope** = the part of the program text where a name is visible.
- **Lifetime** = the time during execution when the object exists.

```cpp
int main() {
    int x = 10;          // x created
    {
        int y = 20;      // y created
        cout << x << y;  // both visible
    }                    // y destroyed
    cout << x;           // x still visible
    // cout << y;        // ERROR: out of scope
}
```

**Four categories of functions:** no args/no return; args/no return; no args/with return; args/with return.

### Program: functions and overloading

```cpp
#include <iostream>
using namespace std;

int add(int a, int b) { return a + b; }        // parameters a, b
void greet() { cout << "Hello from greet()\n"; }
void show(int x) { cout << "Value = " << x << endl; }
double add(double a, double b) { return a + b; }  // overloaded

int main()
{
    greet();
    int result = add(10, 20);                  // arguments 10, 20
    cout << "int add    = " << result << endl;
    cout << "double add = " << add(2.5, 3.5) << endl;
    show(result);
    return 0;
}
```

**Output**
```
Hello from greet()
int add    = 30
double add = 6
Value = 30
```

---

## 7. Argument passing (very important)

### 7.1 Pass by value
The argument's value is **copied** into the parameter. The parameter and argument are independent objects; changes inside the function do not affect the caller.

### 7.2 Pass by reference
The parameter is a **reference**; it is bound directly to the caller's object, so changes are visible outside. No copy is made.

> Reference parameters that the function does not modify should be `const` references — avoids copying large objects while guaranteeing safety.

### 7.3 Pass by address
The **address** is passed with `&`; the function receives a pointer and modifies the original through `*`.

### Program: all three with swap

```cpp
#include <iostream>
using namespace std;

void swapValue(int x, int y)      // copies swapped; originals untouched
{
    int t = x; x = y; y = t;
    cout << "  inside swapValue   : " << x << " " << y << endl;
}

void swapRef(int &x, int &y)      // aliases of caller's variables
{
    int t = x; x = y; y = t;
}

void swapPtr(int *x, int *y)      // addresses; *x is the original
{
    int t = *x; *x = *y; *y = t;
}

int main()
{
    int a = 5, b = 10;
    cout << "before             : " << a << " " << b << endl;

    swapValue(a, b);
    cout << "after swapValue    : " << a << " " << b << endl;

    swapRef(a, b);
    cout << "after swapRef      : " << a << " " << b << endl;

    a = 5; b = 10;
    swapPtr(&a, &b);
    cout << "after swapPtr      : " << a << " " << b << endl;
    return 0;
}
```

**Output**
```
before             : 5 10
  inside swapValue   : 10 5
after swapValue    : 5 10
after swapRef      : 10 5
after swapPtr      : 10 5
```

| Method | Copy made? | Can modify original? | Typical use |
|---|---|---|---|
| By value | Yes | No | small data, must protect caller |
| By reference | No | Yes | swap, output parameters, large objects |
| By address | Address copied | Yes (via `*`) | C-style APIs, optional/null arguments |

**Exam trap:** "Call by value does not change the original" is the expected conclusion — show it using the swap output above.

---

## 8. Classes and objects

- **Class:** user-defined type that links data and functions; the basic unit of encapsulation; a **blueprint**.
- **Object:** an **instance** of a class; has physical existence and memory.
- No memory is allocated when a class is **defined**; memory is allocated when an object is **created**.

### 8.1 General form

```cpp
class ClassName
{
        private:                  // default for class
                data and functions
        public:
                data and functions
        protected:
                data and functions
} object-list;                    // optional; can declare objects here
```

### 8.2 Access specifiers

| Specifier | Access |
|---|---|
| `private` | Only members of the same class (and friends). Default for `class`. |
| `public` | Accessible from anywhere in the program. |
| `protected` | Same as private, but also accessible in derived classes (needed with inheritance). |

- An access specifier stays in effect until the next specifier or the end of the class.
- A class may have multiple sections of each kind.
- A non-static data member cannot be declared `auto`, `extern`, or `register`.
- **Good practice:** data members private; member functions public.

### 8.3 Defining and using

```cpp
class Rectangle {
    private:
        int length, breadth;
    public:
        Rectangle(int l, int b) { length = l; breadth = b; }
        int area() { return length * breadth; }  // defined inside -> implicitly inline
        int perimeter();                          // declared inside
};

int Rectangle::perimeter() { return 2 * (length + breadth); }  // defined outside

int main() {
    Rectangle r(8, 3);
    cout << r.area();            // dot operator with object
    Rectangle *p = &r;
    cout << p->area();           // arrow operator with pointer
}
```

**Output of the full program**
```
Area      = 24
Perimeter = 22
Area via -> = 24
```

**Members defined inside the class are implicitly inline; those defined outside use `ClassName::`.**

> Dot (`.`) is used with an object; arrow (`->`) with a pointer to an object.

---

## 9. Friend functions and friend classes

Data hiding restricts private members. `friend` grants a **non-member** access to private/protected members.

### 9.1 Friend function

- Declared inside the class with the `friend` keyword, defined like a normal function outside.
- **Not a member** — no `this`, not called with `object.func()`.
- Can access **all private and protected** members of the class.
- Friendship is **granted, not taken**: not mutual, not inherited, not transitive.
- A friend declaration may be placed in any access section; access specifiers do not affect it.
- If it needs private data of two classes, declare it as a friend in **both** (use a forward declaration for the second class).

```cpp
#include <iostream>
using namespace std;

class B;                               // forward declaration

class A {
    int x;
    public:
        A(int v) { x = v; }
        friend int maxOf(A, B);
};

class B {
    int y;
    public:
        B(int v) { y = v; }
        friend int maxOf(A, B);
};

int maxOf(A a, B b) { return a.x > b.y ? a.x : b.y; }

int main() {
    A a(30); B b(45);
    cout << "Max = " << maxOf(a, b) << endl;   // called like a normal function
    return 0;
}
```

**Output**
```
Max = 45
```

**Advantages:** controlled access when two classes/functions must cooperate; useful in operator overloading and I/O (`operator<<`); avoids adding public getters for everything.
**Disadvantages:** weakens encapsulation; increases coupling; not inherited, so maintenance is harder; overuse is bad design.

### 9.2 Friend class

If `class B` is declared `friend class` inside `A`, then **every member function of B** can access A's private/protected members.

```cpp
#include <iostream>
using namespace std;

class TwoValues {
    int a, b;
    public:
        TwoValues(int i, int j) { a = i; b = j; }
        friend class Min;              // Min can read a and b
};

class Min {
    public:
        int min(TwoValues t) { return t.a < t.b ? t.a : t.b; }
};

int main() {
    TwoValues ob(10, 20);
    Min m;
    cout << "Minimum = " << m.min(ob) << endl;
    return 0;
}
```

**Output**
```
Minimum = 10
```

Properties (write these as bullet points):
- Not mutual — if A befriends B, B does not automatically befriend A.
- Not inherited — derived classes do not inherit friendship.
- Not transitive — friend of a friend is not a friend.
- Reduces data hiding, so friend classes are "seldom used".

---

## 10. Inline functions

**Definition:** a function declared with `inline` whose code is **copied (expanded) at the call site** by the compiler, removing function-call overhead.

```cpp
inline int square(int n) { return n * n; }
```

- It is a **request**, not a command; the compiler may ignore it.
- Functions defined **inside** a class body are implicitly inline.
- Typically ignored for: large bodies, loops/recursion/`switch` inside, virtual functions, when the address of the function is taken.

**Advantages:** no call overhead (no stack push/pop), faster for small frequently used functions, type-safe (unlike macros).
**Disadvantages:** code size increases (code bloat), may reduce cache performance; debugging is harder; not guaranteed.

**Inline vs macro:** a macro is textual substitution (no type checking, side effects like `SQR(x++)`), inline is a real function with type checking.

```cpp
#include <iostream>
using namespace std;

inline int square(int n) { return n * n; }
inline void displayNum(int num) { cout << num << endl; }

int main() {
    cout << square(5) << " " << square(6) << endl;
    displayNum(666);
    return 0;
}
```

**Output**
```
25 36
666
```

---

## 11. Constructors and destructors

### 11.1 Constructor

A **special member function** called automatically when an object is created.

Rules:
- Same name as the class.
- **No return type** (not even `void`).
- Usually `public`.
- Can be **overloaded** (default, parameterized, copy).
- Cannot be `static`, and cannot be `virtual`.
- If you write no constructor, the compiler supplies a **default constructor** with an empty body.

**Types:**

| Type | Form | Purpose |
|---|---|---|
| Default | `A()` | no arguments; initializes to default values |
| Parameterized | `A(int x, int y)` | initializes with supplied values |
| Copy | `A(const A &other)` | creates a new object as a copy of an existing object |

**Parameterized constructor** is the preferred way to initialize members. **Initializer list** form:

```cpp
Account(int no, double bal) : accNo(no), balance(bal) {}
```

**Copy constructor is called when:** an object is initialized from another object (`A b = a;`), passed **by value**, or returned **by value**.

**Shallow vs deep copy (interview favourite):** the default copy constructor copies members one by one. If a member is a raw pointer, both objects point to the **same** memory (shallow copy) → changing one affects the other and the memory may be deleted twice. A user-defined copy constructor that allocates new memory and copies the contents is a **deep copy**.

### 11.2 Destructor

- Name is the class name preceded by `~`.
- No parameters, no return type, **cannot be overloaded**; one per class.
- Called automatically when the object's lifetime ends:
  - local object → end of its block,
  - dynamically created object → when `delete` is used,
  - global/static object → when the program terminates.
- Used to release resources (memory, files, locks).

| Constructor | Destructor |
|---|---|
| Initializes the object | Cleans up the object |
| Called when object is created | Called when object is destroyed |
| Can take arguments | Takes no arguments |
| Can be overloaded | Cannot be overloaded |
| Called in order of creation | Called in **reverse** order |

### Program: all constructor types + destruction order

```cpp
#include <iostream>
using namespace std;

class Demo
{
    static int counter;
    int id;
    public:
        Demo() { id = ++counter; cout << "Default ctor  -> object " << id << endl; }
        Demo(int k) { id = ++counter; cout << "Param ctor    -> object " << id << " value " << k << endl; }
        Demo(const Demo &d) { id = ++counter; cout << "Copy ctor     -> object " << id << " copied from " << d.id << endl; }
        ~Demo() { cout << "Destructor    -> object " << id << endl; }
};

int Demo::counter = 0;
Demo globalObj;                     // before main

int main()
{
    cout << "--- main starts ---\n";
    Demo a;
    Demo b(50);
    Demo c = b;                     // copy constructor
    Demo *p = new Demo(99);
    delete p;                       // destroyed here
    Demo arr[2];                    // default ctor twice
    cout << "--- main ends ---\n";
    return 0;
}
```

**Output**
```
Default ctor  -> object 1
--- main starts ---
Default ctor  -> object 2
Param ctor    -> object 3 value 50
Copy ctor     -> object 4 copied from 3
Param ctor    -> object 5 value 99
Destructor    -> object 5
Default ctor  -> object 6
Default ctor  -> object 7
--- main ends ---
Destructor    -> object 7
Destructor    -> object 6
Destructor    -> object 4
Destructor    -> object 3
Destructor    -> object 2
Destructor    -> object 1
```

**Order to remember:**
1. Global objects are constructed **before** `main`.
2. Local objects are destroyed in **reverse order** of construction at the end of their block.
3. A heap object is destroyed at `delete`, not at the end of `main`.
4. Array elements are destroyed in reverse index order.
5. Globals are destroyed **last** (after `main`).

---

## 12. Static class members

### 12.1 Static data member

- Declared with `static` inside the class; **only one copy** exists for the whole class, shared by all objects.
- Initialized to **zero** before any object is created.
- Lifetime = entire program; visible only through the class.
- Must be **defined outside** the class (no `static` keyword there):

```cpp
class Employee { static int count; };
int Employee::count = 0;          // definition + initialization
```

Why outside? The declaration inside the class does not allocate storage; the out-of-class definition allocates the single copy.

**Uses:** count objects, share a resource/flag among all objects, constants common to the class.

### 12.2 Static member function

- Belongs to the class, not to an object; callable as `ClassName::func()` without an object.
- Can access **only static** members directly (no object → no non-static data).
- Has **no `this` pointer**.
- Cannot be `virtual`, `const`, or `volatile`; a static and a non-static version with the same signature cannot coexist.

```cpp
#include <iostream>
using namespace std;

class Student
{
    int roll;
    static int count;
    public:
        Student(int r = 0) { roll = r; ++count; }
        ~Student() { --count; }
        static int getCount() { return count; }   // only static data allowed
};

int Student::count = 0;

int main()
{
    cout << "Objects alive = " << Student::getCount() << endl;
    Student s1(1), s2(2);
    {
        Student s3(3);
        cout << "Inside block  = " << Student::getCount() << endl;
    }
    cout << "After block   = " << Student::getCount() << endl;

    Student *p = new Student(4);
    cout << "With heap obj = " << p->getCount() << endl;
    delete p;
    cout << "Final         = " << Student::getCount() << endl;
    return 0;
}
```

**Output**
```
Objects alive = 0
Inside block  = 3
After block   = 2
With heap obj = 3
Final         = 2
```

---

## 13. Scope resolution operator `::`

Three standard uses (learn all three):

1. **Define a member function outside its class** — `int Rectangle::area() { ... }`
2. **Access a global name hidden by a local name** — `::value`
3. **Access a static member / class member without an object** — `Student::count`

(It is also used to qualify a base class in inheritance, e.g. `Base::show()`.)

```cpp
#include <iostream>
using namespace std;

int value = 100;

class Test {
    public:
        static int count;
        void show();
};

int Test::count = 7;              // (1) static member defined outside

void Test::show() {               // (2) member function defined outside
    cout << "static count = " << Test::count << endl;
}

int main()
{
    int value = 20;                        // hides global
    cout << "local  value = " << value << endl;
    cout << "global value = " << ::value << endl;   // (3) global access
    Test t; t.show();
    return 0;
}
```

**Output**
```
local  value = 20
global value = 100
static count = 7
```

---

## 14. Passing objects, returning objects, object assignment

- Objects can be passed to functions **by value** (copy), **by reference** (no copy, can modify), or by address/pointer.
- A function can **return an object** by value; the returned object is copied into the caller's variable (copy elision may optimise this).
- **Object assignment** (`b = a;`) copies all data members from `a` into `b`; the two remain separate objects. Default assignment performs a **member-wise (shallow)** copy.
- Prefer `const ClassName&` when passing objects that should not be modified.

```cpp
#include <iostream>
using namespace std;

class Student
{
    public:
        double marks1, marks2;
        Student() { marks1 = marks2 = 0; }
        Student(double m1, double m2) { marks1 = m1; marks2 = m2; }
        void show() const { cout << marks1 << " " << marks2 << endl; }
};

void byValue(Student s) { s.marks1 = 0; cout << "Inside byValue: "; s.show(); }
void byRef(Student &s)  { s.marks1 += 5; }

Student createStudent() { Student temp(96.5, 75.0); return temp; }

int main()
{
    Student a(80, 70), b;
    byValue(a);
    cout << "After byValue: "; a.show();
    byRef(a);
    cout << "After byRef  : "; a.show();
    b = a;
    cout << "b (assigned) : "; b.show();
    Student c = createStudent();
    cout << "Returned obj : "; c.show();
    return 0;
}
```

**Output**
```
Inside byValue: 0 70
After byValue: 80 70
After byRef  : 85 70
b (assigned) : 85 70
Returned obj : 96.5 75
```

> An object of one class can also be passed to a member function of another class, provided the member is accessible (often via a friend).

---

# PART B — MODULE 2

Most Module 2 topics are the same class concepts in more depth. Below are the **new** points; revise sections 8–14 above for the shared ones.

## 15. Classes, structures and classes are related

A C++ `struct` is a class in every way **except default access**:

| | `struct` | `class` |
|---|---|---|
| Default member access | **public** | **private** |
| Default inheritance access | public | private |
| Can have member functions? | Yes | Yes |
| Can have constructors/destructors? | Yes | Yes |
| Can use access specifiers? | Yes | Yes |

```cpp
struct StudentS { string name; int marks; };   // public by default

class StudentC {
    string name; int marks;                    // private by default
    public:
        void set(string n, int m) { name = n; marks = m; }
        void show() { cout << name << " : " << marks << endl; }
};

int main() {
    StudentS s1;
    s1.name = "Anu"; s1.marks = 88;            // OK
    StudentC s2;
    // s2.name = "Ravi";                       // ERROR: private
    s2.set("Ravi", 91); s2.show();
}
```

**Output**
```
Anu : 88
Ravi : 91
```

In C, a struct could not have functions; C++ expanded it into an alternative class declaration. In practice use `struct` for passive data bundles, `class` when you need encapsulation/invariants.

---

## 16. Array of objects

An array whose every element is an object of the same class.

```cpp
ClassName objArray[size];
```

- Each element is a separate object with its own data members.
- Access with `objArray[i].member`.
- If the class has a **default constructor**, `Employee e[3];` constructs all 3 automatically.
- If only a **parameterized constructor** exists, initialize each element explicitly:

```cpp
cl ob[3] = { cl(1, 2), cl(3, 4), cl(5, 6) };
```

Without an initializer in that case, compilation fails (no default constructor).

### Program: array of objects, highest salary

```cpp
#include <iostream>
#include <string>
using namespace std;

class Employee
{
    string name;
    double salary;
    public:
        Employee() { name = "-"; salary = 0; }
        Employee(string n, double s) { name = n; salary = s; }
        double getSalary() const { return salary; }
        void show() const { cout << name << " : " << salary << endl; }
};

int main()
{
    Employee e[3] = { Employee("Anu", 45000),
                      Employee("Ravi", 62000),
                      Employee("Meera", 58000) };

    int best = 0;
    for (int i = 1; i < 3; ++i)
        if (e[i].getSalary() > e[best].getSalary())
            best = i;

    cout << "Employee with highest salary: ";
    e[best].show();
    return 0;
}
```

**Output**
```
Employee with highest salary: Ravi : 62000
```

---

## 17. The `this` pointer

When a member function is called, the compiler passes an **implicit argument**: a pointer to the object that invoked it. That pointer is **`this`**.

- Type: `ClassName*` (pointer to the class); in a `const` member function, `const ClassName*`.
- Stores the **address of the invoking object**.
- Used to:
  1. resolve a **name conflict** between a parameter and a data member: `this->marks = marks;`
  2. **return the current object** (`return *this;`) to allow **method chaining**.
  3. compare objects (`if (this == &other)`), or pass the current object to another function.
- **Not available in static member functions** because they are not called on an object.

```cpp
#include <iostream>
using namespace std;

class Counter
{
    int value;
    public:
        Counter() { value = 0; }
        void setValue(int value) { this->value = value; }  // member = parameter
        Counter& increment() { ++value; return *this; }    // returns current object
        void show() const { cout << "value = " << value << endl; }
};

int main()
{
    Counter c;
    c.setValue(10);
    c.show();
    c.increment().increment().increment();   // chaining
    c.show();
    return 0;
}
```

**Output**
```
value = 10
value = 13
```

---

## 18. Dynamic allocation: `new` and `delete`

C++ allocates/frees heap memory at run time with two **operators**:

```cpp
pointer = new type;                 // allocate one item
pointer = new type(initializer);    // allocate and initialize
pointer = new type[size];           // allocate an array
delete pointer;                     // free one item
delete[] pointer;                   // free an array
```

- `new` allocates memory on the **heap** and returns a **typed pointer** to the start.
- `delete` frees memory previously allocated with `new`.
- If memory is insufficient, `new` throws **`bad_alloc`** (defined in `<new>`).
- `delete[]` is mandatory for arrays; using plain `delete` on an array is undefined behaviour.
- The heap is finite; forgetting `delete` causes a **memory leak**, and using memory after `delete` gives a **dangling pointer**.

### Program: all forms + failure handling

```cpp
#include <iostream>
#include <new>
using namespace std;

class Balance
{
    double amount;
    public:
        Balance() { amount = 0; cout << "Balance object constructed\n"; }
        Balance(double a) { amount = a; cout << "Balance object constructed\n"; }
        ~Balance() { cout << "Balance object destroyed\n"; }
        void show() const { cout << "Balance = " << amount << endl; }
};

int main()
{
    int *p = new int;                 // single variable
    *p = 100;
    cout << "p points to " << *p << endl;
    delete p;

    int *q = new int(87);             // initialized allocation
    cout << "q points to " << *q << endl;
    delete q;

    int *arr = new int[5];            // array
    for (int i = 0; i < 5; ++i) arr[i] = i * 10;
    for (int i = 0; i < 5; ++i) cout << arr[i] << " ";
    cout << endl;
    delete[] arr;                     // array form

    Balance *b = new Balance(2500.75);  // object: ctor runs
    b->show();                          // arrow operator
    delete b;                           // dtor runs

    try {
        int *big = new int[1000000000000];
        delete[] big;
    }
    catch (bad_alloc &e) {
        cout << "Allocation failure caught: " << e.what() << endl;
    }
    return 0;
}
```

**Output**
```
p points to 100
q points to 87
0 10 20 30 40
Balance object constructed
Balance = 2500.75
Balance object destroyed
Allocation failure caught: std::bad_alloc
```

### 18.1 `new`/`delete` vs `malloc`/`free`

| `new` / `delete` | `malloc` / `free` |
|---|---|
| Operators (can be overloaded) | Library functions |
| Calls **constructor** / **destructor** | Does not |
| Returns a **typed pointer** | Returns `void*` (needs cast) |
| Size calculated automatically | Must pass `sizeof` |
| Throws `bad_alloc` on failure | Returns `NULL` |
| `delete[]` for arrays | `free` for any allocation |
| Type-safe | Not type-safe |

### 18.2 `nothrow` form

```cpp
int *p = new (nothrow) int[1000];
if (p == nullptr) { /* handle failure */ }
```

`new (nothrow)` returns `nullptr` instead of throwing.

---

## 19. Stack vs heap, and memory segments

| Stack | Heap |
|---|---|
| Automatically managed | Manually managed (`new`/`delete`) |
| Local variables, function-call info | Dynamically allocated objects/data |
| Allocation/deallocation automatic and fast | Programmer requests/releases; slower |
| Size/lifetime constrained by scope | Flexible, can be large/long-lived |
| Example: `int x;` | Example: `int *p = new int;` |

| Segment | Stores | Lifetime | Example |
|---|---|---|---|
| Code | Program instructions | Whole execution | `main()` instructions |
| Global/Data | Global and static variables | Usually whole program | `int count = 10;` |
| Stack | Local variables, call info | Until block/function ends | `int x = 10;` |
| Heap | Dynamically allocated data | Until `delete` / program end | `new int` |

**Memory leak:** allocated memory is never freed.
**Dangling pointer:** a pointer that still holds the address of memory that has already been freed.

---

# PART C — QUESTION BANK

The PDFs do not contain a separate "question bank" file, so this section is built from (a) the exercise questions printed in Module 1 and Module 2, and (b) the "Frequently Asked Interview Questions" page of Module 2. Answers are compressed to what fits the marks.

## A. 2-mark rapid fire (with answers)

1. **What is a class?** A user-defined data type that binds data members and member functions; a blueprint for objects.
2. **What is an object?** An instance of a class that occupies memory and has state and behaviour.
3. **Encapsulation?** Wrapping data and the functions that operate on it into a single unit (class).
4. **Abstraction?** Exposing only the essential interface and hiding implementation details.
5. **Polymorphism?** The ability of one name/interface to take many forms (function/operator overloading, virtual functions).
6. **Inheritance?** A derived class acquiring the properties of a base class; provides reusability.
7. **Data hiding?** Restricting direct access to data, achieved with `private`.
8. **Message passing?** Objects communicating by invoking each other's member functions.
9. **Dynamic binding?** Deciding at run time which function body to execute (via `virtual`).
10. **Default access of class vs struct?** `class` → private; `struct` → public.
11. **Why is a static data member defined outside the class?** The in-class declaration allocates no storage; the external definition creates the single shared copy.
12. **Can a constructor be virtual?** No — the vtable is not set up until the object exists. A destructor can and should be virtual in a base class.
13. **Can a destructor be overloaded?** No — it takes no parameters and there is only one per class.
14. **Is friendship inherited?** No; it is also not mutual and not transitive.
15. **What is `this`?** An implicit pointer to the object that invoked the member function; type `ClassName*`.
16. **Why can't a static member function use `this`?** It is not called on any object, so there is no invoking object.
17. **`delete` vs `delete[]`?** `delete` frees one object; `delete[]` frees an array allocated by `new[]`.
18. **`endl` vs `"\n"`?** `endl` writes a newline and flushes the stream; `"\n"` only writes a newline.
19. **Null statement?** A lone `;` that does nothing, used where syntax requires a statement.
20. **Dangling else?** An ambiguity where an `else` binds to the nearest unmatched `if`.
21. **Scope vs lifetime?** Scope is where a name is visible in the text; lifetime is how long the object exists during execution.
22. **Why is `sizeof` an empty class 1?** The standard requires distinct objects to have distinct addresses, so the compiler gives it 1 byte.
23. **Reference vs pointer?** Reference is an alias, must be initialized, cannot be null or reseated; pointer stores an address, can be null and reassigned.
24. **What does `new` return?** A typed pointer to heap memory; throws `bad_alloc` on failure.
25. **What is a memory leak?** Heap memory that is allocated but never released with `delete`.

## B. 5-mark questions (answer skeleton + program reference)

1. **Differentiate POP and OOP.** → Section 1.1 table; add bottom-up vs top-down and data security.
2. **Explain the features of OOP.** → Section 1.2, one line each + class/object example.
3. **General form of a class; explain access specifiers; write `Account`.** → Section 8 + program `p08_account.cpp`.
4. **Member functions inside vs outside a class; dot and arrow operators.** → Section 8.3 + `p07_rectangle.cpp`.
5. **Compare struct and class; show a struct with member functions/constructor.** → Section 15 + `p09_struct_class.cpp`.
6. **Friend function: characteristics + compare private data of two classes.** → Section 9.1 + `p10_friend_func.cpp` (mention forward declaration).
7. **Friend class + program.** → Section 9.2 + `p11_friend_class.cpp`; list non-mutual/non-inherited/non-transitive.
8. **Inline functions: advantages, limitations, inline vs macro.** → Section 10 + `p12_inline.cpp`.
9. **Constructors: default, parameterized, copy with a program each.** → Section 11 + `p13_constructors.cpp`.
10. **Destructor + order of construction/destruction (global, local, heap).** → Section 11.2 output of `p13_constructors.cpp`.
11. **Static data member + static member function; count objects.** → Section 12 + `p14_static.cpp`.
12. **Uses of `::` with examples.** → Section 13 + `p19_scope.cpp` (3 uses).
13. **Array of objects; n employees, highest salary.** → Section 16 + `p15_array_objects.cpp`.
14. **`this` pointer; name conflict and chaining.** → Section 17 + `p16_this.cpp`; note no `this` in static functions.
15. **`new`/`delete` vs `malloc`/`free`; program for variable, array, object.** → Section 18 + `p17_new_delete.cpp`.
16. **Stack vs heap and memory segments.** → Section 19 tables.

## C. 10-mark questions (full-answer plan)

1. **Explain the basic concepts of OOP with examples.**
   Definition → 8 features (class, object, encapsulation, abstraction, polymorphism, inheritance, dynamic binding, message passing) → one real-world example each → POP vs OOP table → conclusion (modularity, security, reuse).
2. **Explain classes and objects in C++ with access specifiers and a program.**
   Class syntax → object creation → private/public/protected → member functions inside/outside → dot/arrow → `Account` or `Rectangle` program with output → "class is logical, object is physical".
3. **Explain constructors and destructors in detail, including execution order.**
   Definition + rules → 3 types → initializer list → destructor rules → comparison table → `p13_constructors.cpp` with output → order points (global, local reverse, heap at delete).
4. **Explain friend functions, friend classes and inline functions.**
   Need for friendship → syntax → program comparing two classes → friend class properties → inline mechanism/advantages/limitations → program → one line on encapsulation trade-off.
5. **Explain static members, `this` pointer and arrays of objects.**
   Static data (one copy, defined outside) → static function rules → `this` (implicit, name conflict, chaining) → array declaration/initialisation → program(s) → outputs.
6. **Explain argument passing and dynamic memory allocation with programs.**
   Value/reference/address semantics → swap program output → `new`/`delete` forms → array/object allocation → `bad_alloc` → `new` vs `malloc` table → stack vs heap.
7. **General form of a C++ program, compilation process and I/O library.**
   Program skeleton → source file naming → `g++` → preprocessor/compiler/assembler/linker/loader diagram → `cin`, `cout`, `cerr`, `clog`, `endl`, namespace `std` → sum program.

## D. Program-writing drills (do these on paper once)

| # | Write a program to... | Model |
|---|---|---|
| 1 | Add two numbers using `cin`/`cout` | `p01_io.cpp` |
| 2 | Sum 1–10 using while and for; print 10–0 using do-while | `p02_loops.cpp` |
| 3 | Print grade using if-else and a menu using switch | `p03_conditions.cpp` |
| 4 | Swap two numbers using value, reference, address | `p05_swap.cpp` |
| 5 | Find area/perimeter of a rectangle using a class | `p07_rectangle.cpp` |
| 6 | Implement an `Account` class with deposit/withdraw/display | `p08_account.cpp` |
| 7 | Compare private data of two classes using a friend function | `p10_friend_func.cpp` |
| 8 | Show that class B is a friend of class A | `p11_friend_class.cpp` |
| 9 | Count objects created/destroyed using a static member | `p14_static.cpp` |
| 10 | Store n employees in an array of objects and print highest salary | `p15_array_objects.cpp` |
| 11 | Use `this` to resolve a name conflict and chain calls | `p16_this.cpp` |
| 12 | Dynamically allocate one variable, an array and an object | `p17_new_delete.cpp` |
| 13 | Return an object from a function and assign it to another | `p18_object_ops.cpp` |

## E. Module 1 textbook exercises (quick solutions)

1. **Sum 50–100 with `while`.**
   ```cpp
   int sum = 0, i = 50;
   while (i <= 100) { sum += i; ++i; }
   // sum = 3825
   ```
2. **Count down 10 to 0 with `--`.**
   ```cpp
   int n = 10;
   while (n >= 0) { cout << n << " "; --n; }
   ```
3. **Print every number between two inputs.**
   ```cpp
   int a, b; cin >> a >> b;
   if (a > b) { int t = a; a = b; b = t; }
   for (int i = a; i <= b; ++i) cout << i << " ";
   ```
4. **`for (int i = -100; i <= 100; ++i) sum += i;`** → final `sum = 0` (each positive cancels its negative; runs 201 times).
5. **Sum until `-1`.**
   ```cpp
   int x, sum = 0;
   while (cin >> x && x != -1) sum += x;
   ```
6. **Accept integers; stop on a negative.**
   ```cpp
   int x;
   while (cin >> x) {
       if (x < 0) break;
       cout << x << " ";
   }
   ```
7. **Sum 1–10 using `for`** → 55 (same as while).

## F. Viva / interview questions (from Module 2, with answers)

1. **struct vs class?** Only default access/inheritance differs (public vs private); both support member functions, constructors, destructors.
2. **Why is `sizeof` an empty class 1?** To guarantee unique addresses for distinct objects.
3. **Shallow vs deep copy? When do you need a copy constructor?** Shallow copies pointer values (shared memory); deep allocates and copies the pointed-to data. Need a user-defined copy constructor when the class owns a raw pointer/resource.
4. **Can a constructor be virtual? Can a destructor?** Constructor no (vtable not ready); destructor yes — a virtual destructor is required when deleting a derived object through a base pointer.
5. **Why can't a static member function use `this`?** It belongs to the class, not to an object; no object means no `this`.
6. **new/delete vs malloc/free? Memory leak? Dangling pointer?** See table in 18.1; leak = never freed; dangling = pointer to freed memory.
7. **Inline: advantages/disadvantages; is it binding?** No, `inline` is only a request; the compiler decides. Code bloat is the main drawback.
8. **Does friendship violate encapsulation? When justified?** It exposes private members, so it weakens encapsulation; justified for tightly coupled classes, operator overloading and stream I/O.

---

# PART D — LAST-MINUTE REVISION SHEET

## 20 one-liners to read in the exam hall

1. Object = data + functions.
2. POP = top-down, functions; OOP = bottom-up, objects.
3. Class = blueprint, no memory; object = instance, memory allocated.
4. Default access: class → private, struct → public.
5. `public` anywhere, `private` same class, `protected` same class + derived.
6. `::` = scope resolution; used for outside definitions, globals, static members.
7. Friend = non-member with private access; granted, not taken.
8. Friendship: not mutual, not inherited, not transitive.
9. Inline = code expanded at call site; request only; no call overhead; code bloat.
10. Function defined inside a class is implicitly inline.
11. Constructor: same name, no return type, can overload, called automatically.
12. Destructor: `~Name`, no args, no return, cannot overload.
13. Destruction order = reverse of construction; heap at `delete`; globals last.
14. Static data: one copy, zero-initialized, defined outside the class.
15. Static function: no `this`, only static members, call with `Class::func()`.
16. `this` = pointer to invoking object; resolves shadowing; `return *this` enables chaining.
17. Array of objects: each element constructed; needs default ctor or explicit initializers.
18. `new` → typed pointer, calls ctor, throws `bad_alloc`; `delete` calls dtor.
19. Arrays: `new[]` with `delete[]`; mismatch is undefined behaviour.
20. Stack = automatic/local; heap = manual/dynamic; leak and dangling pointer definitions.

## Common mistakes that cost marks

| Mistake | Correct |
|---|---|
| `cin << x;` / `cout >> x;` | `cin >> x;` / `cout << x;` |
| Constructor written with `void` | No return type at all |
| `delete p;` for `new int[5]` | `delete[] p;` |
| Forgetting `;` after class body | `};` is required |
| Defining static member as `static int X::count = 0;` outside | `int X::count = 0;` |
| Saying constructor allocates memory | Object creation/`new` allocates; constructor initializes |
| Saying friend function is a member | It is a non-member; called normally |
| `int f(int a, b)` | `int f(int a, int b)` |
| Using `this` in a static function | Not allowed |
| Writing `if (x = 5)` | `if (x == 5)` |

## Answer templates

**"Explain X" (5 marks):**
> Definition (1) → syntax (1) → 2–3 properties/rules (1) → program snippet (1) → output/advantage (1).

**"Write a program" (5–8 marks):**
> Include headers → class with private data + public functions → `main` creating objects → **write the expected output** → 1 line explaining what it demonstrates.

**"Differentiate" (5 marks):**
> Table with 4–6 comparison points, not paragraphs.

---

*End of notes. Programs are in `cpp_prep/` — compile with `g++ file.cpp -o file && ./file`.*
