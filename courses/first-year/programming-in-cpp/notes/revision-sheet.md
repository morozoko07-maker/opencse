---
title: Revision sheet
---

# Revision sheet — Introduction to C++ Programming

The paper is built from definitions plus short programs. For every concept, keep one sentence of definition and one compiling example ready. The same 8 + 8 + 4 pattern repeats in each module.

## Exam pattern

The model paper gives 100 marks in 3 hours: five full questions, one per module. Each is 20 marks (8 + 8 + 4) with an internal OR. The README gives CIE 50 + SEE 50.

## Module 1 — Object-oriented concepts, classes and objects

### Must know

- Object-based programming groups data and functions but lacks inheritance and polymorphism. Object-oriented programming adds both.
- A class is a user-defined type; an object is a variable of that class. Private members are reachable only inside the class, public members from outside, protected members in derived classes.
- Encapsulation binds data and the functions that operate on it, and hides the representation behind a public interface. Abstraction exposes only the essential interface.

### Definitions to reproduce

> A class is a blueprint that defines the data members and member functions common to a set of objects.

> An object is an instance of a class that occupies memory and has its own copy of the data members.

## Module 2 — Functions, overloading and parameter passing

### Must know

- Call by value copies the argument. Call by reference passes an alias, so changes affect the caller. Call by address passes a pointer.
- An inline function is expanded at the call site instead of being called. Use it for short, frequently called functions; it saves call overhead but increases code size.
- Function overloading uses the same name with different parameter lists. The return type alone cannot distinguish overloads.

### Definitions to reproduce

> Function overloading is the use of the same function name for several functions that differ in the number or type of parameters.

## Module 3 — Inheritance and polymorphism

### Must know

- Single inheritance has one base; multiple has several; multilevel forms a chain; hierarchical has several derived classes from one base; hybrid combines two or more forms.
- Public inheritance keeps public members public and protected members protected. Private inheritance makes both private. Protected inheritance makes both protected.
- Constructors run base first, then derived; destructors run derived first, then base. A derived constructor passes base arguments through its initialiser list.
- A virtual function is resolved at run time through a base-class pointer or reference.
- An abstract class has at least one pure virtual function and cannot be instantiated.

### Definitions to reproduce

> Inheritance is the mechanism by which a derived class acquires the properties and behaviour of a base class.

## Module 4 — I/O streams and file handling

### Must know

- A stream is a sequence of bytes moving between a program and a device. C++ uses istream for input, ostream for output and iostream for both.
- Hierarchy: ios is the base; istream and ostream derive from it; iostream derives from both; ifstream, ofstream and fstream derive from istream, ostream and iostream.
- Formatted I/O uses operators and manipulators such as setw, setprecision, fixed and endl. Unformatted I/O uses get, put, read and write.
- File modes: ios::in, ios::out, ios::app, ios::ate, ios::binary and ios::trunc, combined with |.

### Definitions to reproduce

> A stream is an abstraction for a sequence of bytes flowing between a program and an input or output device.

## Module 5 — Exception handling

### Must know

- An exception is a run-time anomaly. C++ uses try, throw and catch.
- Code that may fail goes in try. throw passes a value to a matching catch. catch(...) handles any type.
- Class types can be thrown and caught; the catch parameter must match or be a base class.
- Stack unwinding destroys local objects as the exception propagates.

### Definitions to reproduce

> An exception is a run-time event that disrupts the normal flow of a program and can be handled by a catch block.

## Last 24 hours

1. Write a class with a constructor, a member function defined outside, and an object.
2. Write one program each for call by value, reference and address.
3. Write a multilevel inheritance program and trace constructor and destructor order.
4. Write a text-file program that writes, reads and checks open failure.

## Question bank

**Module 1**

1. Compare object-based programming with object-oriented programming, with examples. [8]
2. Define class and objects and illustrate them with an example program. [8]
3. Illustrate abstraction and encapsulation with a neat diagram. [8]

**Module 2**

4. Differentiate pass by value and pass by reference, and explain pass by address in C++. [8]
5. What is an inline function? When would you make a function inline, and why? [8]

**Module 3**

6. When a base class is privately inherited, its public members become private in the derived class. Justify with a code snippet. [8]
7. Differentiate between single and multilevel inheritance with example code snippets. [8]

**Module 4**

8. Explain the C++ stream class hierarchy. [8]
9. Explain formatted and unformatted I/O. [8]

**Module 5**

10. Discuss exception-handling mechanisms in C++. [8]
11. Can class types be thrown as exceptions? Explain. [8]

*Source: `BPLCK205D- PLC++ 2nd Sem - Descriptive Model Question Paper (1).pdf`; all marks are from that paper.*
