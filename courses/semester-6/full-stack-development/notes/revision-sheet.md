---
title: Revision sheet
---

# Revision sheet — Full Stack Development

This sheet follows the 2023-24 syllabus (BCS604C) and the module notes in `material/Full Stack/ISE final`. The folder has no text-based IA paper, so the question bank is short and comes from the worked Q&A document.

## Exam pattern

The syllabus gives CIE 50 + SEE 50, 40 contact hours and a three-hour SEE. No marks are printed on the available questions.

## Module 1 — Basics of full-stack development and JavaScript

### Must know

- A web request travels from the user through the browser to a web server and backend services; the response travels back the same path.
- A stack is the chosen set of front-end, back-end and database tools. MEAN is MongoDB, Express, Angular and Node; MERN replaces Angular with React.
- Node runs JavaScript outside the browser. Express is a Node web framework; Angular and React are front-end frameworks or libraries; MongoDB is the document database.
- Declare variables with `var`, `let` or `const`. `let` and `const` are block-scoped; `const` prevents reassignment.
- JavaScript types: number, string, boolean, null, undefined, object and symbol.
- Operators: arithmetic, assignment, comparison (`==` and `===`), logical, ternary and type operators. Prefer `===`.

### Definitions to reproduce

> Full-stack development covers both the client-side interface and the server-side application, including the database.

> JavaScript is a dynamically typed, interpreted language standardised as ECMAScript.

## Module 2 — JavaScript control flow, functions and data

### Must know

- Loops: `for`, `while`, `do...while`, `for...in` for keys and `for...of` for iterable values.
- A function declaration is hoisted; a function expression is not. Arrow functions keep the enclosing `this`.
- Scope is global, function or block. `var` ignores block scope; `let` and `const` respect it. Closures keep an outer function's variables alive after it returns.
- Objects hold key-value pairs. Read with dot or bracket notation and add, update or delete properties.
- Strings are immutable. Useful methods: `length`, `indexOf`, `slice`, `split`, `trim` and `replace`.
- Arrays are mutable. Useful methods: `push`, `pop`, `slice`, `splice`, `map`, `filter` and `reduce`.
- Error handling uses `try`, `catch`, `finally` and `throw`; `finally` runs whether or not an error occurs.

### Definitions to reproduce

> A closure is a function together with the lexical environment in which it was created.

> Hoisting moves declarations to the top of their scope before execution.

### Worked pattern

For a scope question, trace each variable to the nearest enclosing block, then check whether it was declared with `var`, `let` or `const`. For a closure question, show the inner function reading a variable that is no longer on the call stack.

## Module 3 — Node.js

### Must know

- Node.js is a runtime built on Chrome's V8 engine. It uses a single-threaded event loop and non-blocking I/O.
- Installation gives `node` and `npm`. `npm init` creates `package.json`; `npm install <module>` adds a dependency to `node_modules`.
- `package.json` records the name, version, entry point, scripts and dependencies.
- A module exports through `module.exports` or `exports`; another file loads it with `require`.
- The event loop takes callbacks from a queue. Blocking work goes to the thread pool, and its callback returns to the queue.
- `EventEmitter` provides `on` for listeners and `emit` for events. Timers use `setTimeout`, `setInterval`, `clearTimeout` and `clearInterval`.
- The traditional server model uses one thread per request; Node uses one main thread plus a thread pool.

### Definitions to reproduce

> Node.js is an open-source, cross-platform JavaScript runtime built on the V8 engine.

> The event loop repeatedly takes ready callbacks from the queue and runs them on the main thread.

### Worked pattern

For an event-emitter answer, define an object, inherit from `EventEmitter`, attach two or three listeners with `on`, emit the event after a state change, and show the output order. Explain that listeners run synchronously when `emit` is called.

## Module 4 — Handling data I/O in Node.js

### Must know

- A callback is passed to another function and called when the work finishes. Node uses error-first callbacks: `callback(err, result)`.
- Callbacks can receive extra parameters, close over outer variables, or be chained. Deep nesting creates callback hell; promises and `async`/`await` flatten it.
- JSON is a text format for objects. `JSON.stringify` converts an object to a string; `JSON.parse` converts a string back.
- A Buffer is a fixed-length byte sequence. Create it with `Buffer.from` or `Buffer.alloc`; convert with `toString`.
- A stream moves data in chunks. Readable, writable, duplex and transform are the four types.
- Zlib compresses and decompresses with `gzip`, `gunzip`, `deflate` and `inflate`, usually through `zlib.createGzip()` and `pipe`.

### Definitions to reproduce

> A callback is a function passed as an argument and invoked when an asynchronous operation completes.

> A stream is an abstract interface for working with data piece by piece rather than all at once.

## Module 5 — MongoDB

### Must know

- MongoDB is a NoSQL document database. A database holds collections; a collection holds documents; a document is a BSON object with fields.
- NoSQL trades the relational table model for flexible schemas and horizontal scaling. MongoDB supports replica sets and sharding.
- `mongod` is the server process; `mongo` or `mongosh` is the shell.
- Use `use <db>`, `show dbs` and `show collections`.
- Collection operations: `createCollection`, `drop`, `insert`, `find`, `update` and `deleteMany`.
- Create users in `admin` and grant read, readWrite or dbAdmin roles.
- The Node.js driver connects with a URI, then calls `find()`, `insertOne()`, `updateOne()` or `deleteOne()`.

### Definitions to reproduce

> NoSQL is a family of database systems that do not use the relational table model as their primary structure.

> A document in MongoDB is a BSON record containing field-value pairs.

## Last 24 hours

1. Draw the browser-server-backend request path and label MEAN components.
2. Write one closure example and one `try`/`catch`/`finally` example.
3. Explain the Node event loop with the queue and thread pool.
4. Compare a callback, a promise and `async`/`await`.

## Question bank

**Module 3**

1. Explain the basic event model and the Node.js event model with a suitable diagram.
2. Write a Node.js program using event emitters to handle events within JavaScript objects.

**Module 4**

3. Explain the different ways in which callbacks are implemented and utilised in Node.js. Highlight their roles in asynchronous programming.

*Source: `material/Full Stack/easy chat gpt.pdf`, which contains the three questions above. No text-based IA or model paper is present: `FSD (N19).pdf` and `MOD-1.pdf` to `MOD-4.pdf` are scans, and the two IA photographs are topic lists, not question papers, so no further questions or marks are claimed.*
