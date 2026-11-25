---
title: Revision sheet
---

# Revision sheet — Object Oriented Programming with C++

A last-week sheet for BCS306B. There is no past paper in the repository, so the shapes below come from the README marking pattern and the notes' question sections. Full explanations and nineteen compiled programs are in [Modules 1 & 2 notes](cpp-modules-1-2.html).

## Exam pattern

The README gives CIE 50 + SEE 50. No paper is stored locally, so no paper marks are quoted. The README marking guide is reliable:

| Question | What earns marks |
|---|---|
| 2 marks | Exact definition plus one example line |
| 5 marks | Definition, syntax, short program, two or three differences |
| 10 marks | Definition, features in points, labelled program, output, conclusion |

A program without output, or a definition without an example, loses marks.

## Module 1 — OOP foundations, classes and constructors

### Must know

- OOP designs around objects that hold data and the functions acting on it; POP designs around procedures.
- Eight ideas: class, object, encapsulation, abstraction, polymorphism, inheritance, dynamic binding, message passing.
- Encapsulation is how data is hidden; abstraction is what is exposed.
- `class` members are private by default; `struct` members are public by default.
- A constructor has the class name, no return type, and initialises the object.
- Constructor types: default, parameterised and copy.
- A destructor is `~Class()`, takes no arguments and runs when the object dies.
- Construction order: base, members, body; destruction is the reverse.
- A friend function is not a member but may touch private data; friendship is neither mutual, inherited nor transitive.
- `inline` asks the compiler to substitute the body; it is a request, not a command.
- Static data members need one definition outside the class.

### Definitions to reproduce

> A class is a user-defined data type that binds data members and member functions into one unit.

> An object is an instance of a class that occupies memory and has state and behaviour.

> A constructor initialises an object when it is created and has the same name as its class.

> Encapsulation is the binding of data and the functions that operate on it, with access controlled by specifiers.

### Worked pattern — 10-mark answer

Write the definition, then the features as numbered points, then a complete program with a class, object and output. Finish with one line on the advantage. For a constructor question, show all three types in one program and print something in each constructor and destructor so the order is visible.

## Module 2 — Objects, dynamic memory and class relationships

### Must know

- An array of objects calls the default constructor for every element.
- Passing an object by value copies it; by reference avoids the copy; by pointer needs `->`.
- A copy constructor is called on initialisation from another object, on pass by value and on return by value.
- `this` is an implicit pointer to the invoking object, of type `ClassName*`.
- `this` resolves a field/parameter name clash and supports chained calls.
- A static member function has no `this`.
- `new` allocates from the heap and returns a typed pointer; `delete` releases it.
- `new[]` must be matched with `delete[]`; mixing them is undefined.
- `new` throws `bad_alloc` on failure; `malloc` returns `NULL`.
- Unlike `malloc`, `new` calls the constructor; `delete` calls the destructor.
- A memory leak is heap memory allocated but never released.
- Stack memory is automatic and scoped; heap memory lasts until deleted.

### Definitions to reproduce

> The this pointer is an implicit pointer that holds the address of the object invoking a member function.

> A copy constructor creates a new object as a copy of an existing object of the same class.

### Worked pattern — program with output

Declare the class, write the constructor and destructor with a print, create one local and one heap object, use the object, then `delete` the heap object. Label the output lines so the construction and destruction order is obvious.

## Beyond module 2

The local notes stop at module 2. The standard BCS306B pattern continues with operator overloading, inheritance, virtual functions and polymorphism, streams and file I/O, templates, exception handling and the STL. No notes or papers for those topics exist here, so this sheet does not invent questions on them. Treat the topic list as a checklist for what to revise elsewhere.

## Last 24 hours

1. Recite the eight OOP features with one example each.
2. Write the `Account` class with deposit, withdraw and display from memory.
3. Write a program showing default, parameterised and copy constructors and the destruction order.
4. Write a friend function that compares private data of two classes.
5. Write a program using `new` for a variable, an array and an object, then delete all three.
6. Recite `new` versus `malloc` and stack versus heap.
7. Repeat the 2-mark answers on `this`, static members and `delete[]`.

## Question bank

Questions are taken from the existing notes' own question sections. They are practice items, not past-paper questions.

**Module 1**

1. Differentiate procedure-oriented and object-oriented programming. [5]
2. Explain the features of OOP with one example each. [5]
3. Give the general form of a class, explain the access specifiers and write an `Account` class. [5]
4. Friend function: characteristics, plus a program comparing private data of two classes. [5]
5. Inline functions: advantages, limitations and comparison with macros. [5]
6. Constructors: default, parameterised and copy, with a program for each. [5]
7. Destructor, including the order of construction and destruction. [5]
8. Static data member and static member function, with an object counter. [5]
9. Explain the basic concepts of OOP with examples. [10]
10. Explain classes and objects with access specifiers and a program. [10]
11. Explain constructors and destructors in detail, including execution order. [10]
12. Explain friend functions, friend classes and inline functions. [10]

**Module 2**

13. What is `this`? Show its use in a name clash and in chained calls. [5]
14. Compare `new`/`delete` with `malloc`/`free`, with a program. [5]
15. Compare stack and heap, and name the memory segments. [5]
16. Explain argument passing by value, reference and address, with a swap program. [10]
17. Explain static members, the `this` pointer and arrays of objects. [10]
18. Explain dynamic memory allocation with programs for a variable, an array and an object. [10]

*Source: `cpp-modules-1-2.md`, sections A to D. No BCS306B paper exists in the repository, so no marks are claimed beyond the notes' own 2/5/10-mark grouping.*
