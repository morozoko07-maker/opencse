---
title: Revision sheet
---

# Revision sheet — Principles of Programming using C

No SEE or IA paper is included, so the bank uses the twelve programming assignments printed in the syllabus and lab manual. No marks are printed.

## Exam pattern

The SEE is 100 marks in three hours, scaled to 50: ten questions, two per module, each of 20 marks with at most three sub-questions; answer five, one per module. CIE is 50.

## Module 1 — Introduction to C

### Must know

- A C program passes through preprocessing, compilation, assembly and linking.
- The preprocessor handles `#include` and `#define`; `stdio.h` supplies `printf` and `scanf`.
- Execution begins at `main`; every program has exactly one.
- A variable is a named memory location with a type; a constant cannot change.
- `printf` uses `%d`, `%f`, `%c` and `%s`; `scanf` needs the address of each variable.

### Definitions to reproduce

> A variable is a named location in memory whose value can change during execution.

## Module 2 — Operators and control flow

### Must know

- Arithmetic, relational, logical, bitwise and assignment operators have a fixed precedence; use parentheses when unsure.
- Integer division truncates towards zero; `%` works only on integers.
- Conversion is implicit (promotion) or explicit (casting).
- `if`, `if-else` and `switch` select alternatives; `switch` needs integer or character cases.
- `while` tests before the body, `do-while` after it, and `for` groups initialisation, condition and update.
- `break` leaves the nearest loop or switch, `continue` skips an iteration, and `goto` jumps to a label.

### Definitions to reproduce

> A loop repeats a block of statements while a condition remains true.

## Module 3 — Functions and arrays

### Must know

- A function has a declaration, a definition and calls; arguments are passed by value unless pointers are used.
- Local variables live inside their block; global variables are visible to the whole file.
- Storage classes: `auto` is temporary, `static` keeps its value between calls, `extern` refers to another file, `register` requests a CPU register.
- Recursion calls the same function on a smaller input and needs a base case.
- An array is a contiguous block of same-type elements, indexed from 0.
- A two-dimensional array is stored row by row, and its name decays to a pointer when passed.

### Definitions to reproduce

> A function is a named block of statements that performs a task and can be called elsewhere.

> Recursion is a technique in which a function calls itself with a smaller input until a base case is reached.

## Module 4 — Strings and pointers

### Must know

- A C string is a character array ending in `'\0'`.
- `string.h` provides `strlen`, `strcpy`, `strcat` and `strcmp`; string literals are read-only.
- A pointer holds an address; `*` dereferences it and `&` gives an address.
- Pointer arithmetic moves in units of the pointed-to type.
- Passing a pointer lets a function change the caller's variable.

### Definitions to reproduce

> A pointer is a variable that stores the memory address of another variable.

> A string is a sequence of characters terminated by the null character.

## Module 5 — Structures, unions and files

### Must know

- A structure groups members of different types; access uses `.` or `->`.
- A union shares one memory area among its members, so only one member is valid at a time.
- `fopen` modes: `"r"`, `"w"`, `"a"`, `"r+"`, `"w+"`, `"a+"`; `"w"` truncates an existing file.
- `fprintf` and `fscanf` do formatted I/O; `fgetc`, `fputc`, `fgets` and `fputs` handle characters and lines.
- `feof` detects end of file only after a read fails, so test the read result too; `fclose` flushes and releases the file.

### Definitions to reproduce

> A structure is a user-defined type that groups related variables of different types under one name.

> A file is a named collection of data on secondary storage, accessed through a stream.

## Last 24 hours

1. Write the compilation command and explain each stage.
2. Trace a `for` loop and a `while` loop by hand.
3. Write a structure program and a file copy program.

## Question bank

1. Simulate a simple calculator.
2. Compute the roots of a quadratic equation from its coefficients, and print appropriate messages.
3. An electricity board charges 80 paise per unit for the first 200 units, 90 paise for the next 100, and Rs 1 beyond 300. Every user pays Rs 100 meter charge, and a 15% surcharge applies above Rs 400. Read the name and units, and print the charges.
4. Display the pattern 1, 121, 12321 and so on up to the nth row.
5. Implement binary search on integers.
6. Implement matrix multiplication and validate the rules.
7. Compute sin(x)/cos(x) using Taylor series approximation and compare with the built-in library function.
8. Sort N numbers using bubble sort.
9. Write functions for string compare, concatenate and length, using parameter passing.
10. Use structures to read, write and average the marks of N students, listing those above and below the average.
11. Use pointers to compute the sum, mean and standard deviation of N real numbers.
12. Copy one text file to another, reading both names from the user.

*Sources: `22POP13-cpe.pdf` and `pop lab manual.pdf` (same twelve assignments). No marks printed.*
