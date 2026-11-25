---
title: Revision sheet
---

# Revision sheet — Object Oriented Programming with Java

A last-week sheet built from the model question paper and the IA-2 bank. Each module lists the marks-carrying definitions, then the questions those papers ask. Answers need short programs with output, not essays.

## Exam pattern

CIE 50 + SEE 50. The model paper is **100 marks in 3 hours: five questions, one per module**, with an internal OR. Module 1 splits into 6 + 6 + 8; the rest into 10 + 10. The IA banks add packages, exceptions and threads.

## Module 1 — Java basics and OOP principles

### Must know

- Procedure-oriented uses functions on shared data; object-oriented uses objects.
- Encapsulation, inheritance, polymorphism and abstraction are the four principles.
- Java compiles to bytecode and runs on the JVM, so it is portable.
- Primitive types: `byte`, `short`, `int`, `long`, `float`, `double`, `char`, `boolean`.
- Operators: arithmetic, relational, logical, bitwise, assignment, ternary.
- `if` tests a boolean; `switch` selects integral or `String` values and falls through without `break`.
- Arrays are fixed-size objects with a `length` field; `args[]` holds command-line strings.
- `Integer.parseInt` converts a command-line string to `int`.

### Definitions to reproduce

> Object-oriented programming organises a program around objects that combine data and the methods acting on that data.

> Encapsulation binds data and methods into one unit, with access controlled by `private`, `public` and `protected`.

## Module 2 — Classes, objects and methods

### Must know

- A class is a blueprint; an object is an instance in memory.
- Fields hold state, methods hold behaviour; `new` allocates the object.
- A constructor has the class name, no return type, and initialises the object.
- Default, parameterised and copy constructors; overloading is allowed.
- `this` refers to the current object and resolves name clashes.
- Java passes by value: primitives and object references are copied.
- Overloading means the same name with different parameters, resolved at compile time.
- `static` members belong to the class, not to an instance.

### Definitions to reproduce

> A constructor initialises an object when it is created and has the same name as its class.

> Method overloading defines several methods with one name but different parameter lists.

## Module 3 — Inheritance, abstract classes and interfaces

### Must know

- `extends` subclasses a class; Java allows one superclass but many interfaces.
- `super` calls the parent constructor first, or a hidden parent method.
- In multilevel inheritance, `super` reaches only the immediate parent.
- `final` blocks overriding or extension.
- An abstract class cannot be instantiated and may mix abstract and concrete methods.
- An interface holds abstract methods; `implements` supplies the bodies.
- Interface variables are `public static final` by default.
- Dynamic dispatch picks the overridden method of the actual object at run time.

### Definitions to reproduce

> Inheritance is the mechanism by which one class acquires the fields and methods of another.

> Dynamic method dispatch is the run-time choice of an overridden method based on the object actually referred to.

## Module 4 — Packages and exception handling

### Must know

- A package groups related classes and avoids name clashes.
- `import` brings a class or package into scope; `java.lang` is implicit.
- Access: private (class), default (package), protected (package and subclasses), public (any).
- Resolution order: current package, explicit imports, `java.lang`.
- An exception is an abnormal event; `Throwable` splits into `Error` and `Exception`.
- Checked exceptions must be handled or declared; unchecked ones derive from `RuntimeException`.
- `try` guards, `catch` handles, `finally` always runs.
- A custom exception extends `Exception` or `RuntimeException` and is raised with `throw`.

### Definitions to reproduce

> An exception is an object representing an abnormal condition raised during execution.

> A package is a named collection of related classes and interfaces that gives access protection and a namespace.

## Module 5 — Threads

### Must know

- A thread is a lightweight unit of execution sharing process memory.
- The JVM creates the main thread, which runs `main`.
- Create a thread by extending `Thread` and overriding `run`, or by implementing `Runnable`.
- `start()` creates a new call stack; calling `run` directly does not.
- Lifecycle: new, runnable, running, blocked or waiting, terminated.
- `sleep`, `join`, `yield`, `interrupt` control scheduling; priority is a hint.
- `synchronized` gives exclusion; `wait`, `notify`, `notifyAll` coordinate through a monitor.
- `wait` releases the lock, `sleep` does not; both throw `InterruptedException`.

### Definitions to reproduce

> A thread is the smallest unit of execution that can be scheduled independently within a process.

> Synchronisation coordinates threads so that shared data is accessed by one thread at a time.

## Last 24 hours

1. Write matrix addition with `args[]` parsing.
2. Rewrite the `Shape`, `Circle` and `Triangle` abstract-class program.
3. Write the `Resizable` interface and `Rectangle` implementation.
4. Memorise the `try-catch-finally` order and custom-exception skeleton.
5. Recite the thread lifecycle and the `wait`/`notify` contract.
6. Write a producer–consumer program with `wait` and `notify`.

## Question bank

**Module 1**

1. Explain the two paradigms of object-oriented programming and give an example of each. [6]
2. Discuss the three main OOP principles and their significance in Java. [6]
3. Develop a Java program to add two matrices of order N, reading N from command-line arguments. [8]
4. Develop a stack class holding ten integers, with a main method illustrating its operations. [8]

**Module 2**

5. What is a constructor? Explain its role and how it differs from other methods. [10]
6. Explain argument passing in Java methods. [10]
7. Define method overloading, discuss its significance and give an example. [10]

**Module 3**

8. Compare the use of `super` in constructor calls under single and multilevel inheritance. [10]
9. Create an abstract `Shape` class with `calculateArea()` and `calculatePerimeter()`, and subclasses `Circle` and `Triangle`. [10]
10. Explain the relationship between dynamic method dispatch and method overriding. [10]

**Module 4**

11. Discuss how the compiler resolves package and class references when importing. [10]
12. Analyse the structure and purpose of `try-catch-finally`. [10]
13. Explain how to create custom exception subclasses in Java. [10]
14. Define an interface and explain how to declare and implement one with an example. [IA-2]

**Module 5**

15. Analyse the role and significance of the main thread. [10]
16. Examine the process of creating threads in Java. [10]
17. Discuss the thread lifecycle and its state transitions. [10]
18. Explain how threads coordinate using `wait()`, `notify()` and `notifyAll()`. [10]

*Sources: `Model QP_BCS306A.pdf`; `question Bank2.pdf`. Marks are as printed; IA-2 items carry none in that bank.*
