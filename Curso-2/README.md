# Advanced Control Flow, Iteration & Data Sequences

Advanced Control Flow, Iteration & Data Sequences is a comprehensive collection of programs developed to strengthen intermediate knowledge of the Python programming language. Each project addresses a specific programming concept, including structural pattern matching, loop structures, string operations, and tuple sequence processing.

With a problem-solving oriented approach, this repository provides a centralized reference for exploring more advanced control flow mechanisms and data sequence operations in Python.
It demonstrates how these principles can be applied to implement efficient and structured solutions, while serving as both a learning resource and a portfolio showcase.

## Tech Stack

<p align="center">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" width="45" height="45" alt="Python" />
  &nbsp;&nbsp;
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/vscode/vscode-original.svg" width="45" height="45" alt="VS Code" />
</p>

* **Language:** Python
* **IDEs:** Visual Studio Code
* **Operating System:** Windows

## Key Features

* Comprehensive set of exercises covering advanced Python control flow concepts.
* Implementation of structural pattern matching using `match-case`.
* Exploration of definite and indefinite iteration with `for` and `while` loops.
* Processing and transformation of string data using built-in methods.
* Manipulation and unpacking of immutable tuple sequences.
* Emphasis on iterative problem-solving and data processing.
* Designed to serve both as a learning resource and as a portfolio showcase.

## Projects Included

---

### `1.Match/`

**Objective:**
Apply Python 3.10+ Structural Pattern Matching (`match-case`) for clean conditional branching.

**Concepts Applied:**

* Structural pattern matching (`match-case`)
* Guard conditions (`if` guards inside `case`)
* Default fallback cases (`case _`)

**Description:**
Includes scripts for basic integer matching, parity checking (even/odd), and a range evaluation script (`range_evaluator.py`) that checks if an integer is negative, within `[0, 10)`, or greater than 10.

**Output:**

Dynamic console output identifying the matched case or range.

**Potential Applications:**

* Replacing complex nested `if-elif` blocks with readable menu-driven logic or command processing.

---

### `2.Bucle For/`

**Objective:**
Iterate over definite data sequences and compute aggregated data.

**Concepts Applied:**

* Sequence iteration (`for`)
* Loop control (`break`)
* Exponentiation and mathematical list processing

**Description:**
Demonstrates iterating through lists of strings and numbers. Features `square_calculator.py` to calculate squares of elements, and `average_calculator.py` to iterate over a list and compute its average value.

**Output:**

Printed sequence items, mathematical calculations per item, and final average summaries.

**Potential Applications:**

* Batch processing of datasets, mathematical series calculations, and list transformations.

---

### `3.Bucle While/`

**Objective:**
Construct indefinite iterations managed by sentinel values or break conditions.

**Concepts Applied:**

* Indefinite loops (`while`)
* Decrementing counters
* Input accumulation with exit conditions

**Description:**
Contains a countdown script for New Year's, a step counter script, and an dynamic accumulator (`accumulator.py`) that continuously prompts for positive integers and calculates their sum until a negative number is entered.

**Output:**

Step-by-step counter displays and the accumulated sum upon exit.

**Potential Applications:**

* Interactive CLI tools, game execution loops, and continuous data acquisition pipelines.

---

### `4.Cadenas/`

**Objective:**
Process, transform, and search text data using built-in string methods.

**Concepts Applied:**

* String length (`len()`)
* Case conversion (`upper()`, `lower()`)
* String splitting (`split()`) and replacement (`replace()`)
* Sequence membership (`in`)

**Description:**
Demonstrates various string transformation functions on text variables, as well as a search script (`word_search.py`) that verifies whether a user-entered word exists inside a defined word list.

**Output:**

Transformed text outputs, sliced strings, and search confirmation messages.

**Potential Applications:**

* Text cleanup, log parsing, word searching, and input sanitization.

---

### `5.Tuplas/`

**Objective:**
Store, unpack, and process immutable sequence structures.

**Concepts Applied:**

* Tuple creation and indexing
* Tuple unpacking within loops
* Sequence aggregation (`sum()`)

**Description:**
Covers tuple operations including accessing elements by index, calculating totals with `sum()`, and unpacking nested tuple pairs `(name, age)` inside a loop to filter individuals who are 18 or older.

**Output:**

Filtered records based on tuple contents and calculated arithmetic sums.

**Potential Applications:**

* Handling fixed database records, coordinates, and immutable configuration data.
