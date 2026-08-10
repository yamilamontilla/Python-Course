# Data Structures, Modular Programming & Functions

Data Structures, Modular Programming & Functions is a comprehensive collection of programs developed to strengthen knowledge of essential Python data structures, reusable functions, and modular programming techniques. Each project addresses a specific programming concept, including lists, dictionaries, custom function definitions, parameter passing, return values, and modular script architecture using custom imports.

With a problem-solving oriented approach, this repository provides a centralized reference for exploring structured data management, procedural abstraction, and code modularization in Python.
It demonstrates how these principles can be applied to create reusable and organized solutions, while serving as both a learning resource and a portfolio showcase.

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

* Comprehensive set of exercises covering essential Python data structures and modular programming.
* Implementation of ordered and mutable collections using lists.
* Exploration of key-value data structures and nested dictionaries.
* Creation of reusable functions with parameters and return values.
* Implementation of custom logic for arithmetic operations and data analysis.
* Organization of code through custom Python modules and imports.
* Emphasis on code reusability, procedural abstraction, and structured programming.
* Designed to serve both as a learning resource and as a portfolio showcase.

## Projects Included

---

### `1.Listas/`

**Objective:**
Manipulate ordered, mutable collections using index access, element modification, dynamic additions, and deletions.

**Concepts Applied:**

* List indexing and item reassignment
* Dynamic element insertion (`append()`)
* Element removal (`del`)
* List iteration (`for`) and aggregation (`sum()`)

**Description:**
Demonstrates core list operations including updating specific elements, inserting new values, deleting elements by index, traversing list items with loops, and computing the sum of numerical elements. Includes a script (`colores.py`) iterating over a predefined color sequence.

**Output:**

Updated list structures, iterated elements printed line-by-line, and calculated sum totals.

**Potential Applications:**

* Dynamic data collection, queue/stack processing, and sequential data management.

---

### `2.Diccionarios/`

**Objective:**
Store and retrieve key-value pairs, nested dictionary mappings, and capture user inputs dynamically into dictionary schemas.

**Concepts Applied:**

* Key-value data modeling
* Accessing nested dictionaries
* Dynamic key assignment via user prompt (`input()`)
* Formatted string assembly using dictionary properties

**Description:**
Covers key lookup syntax, nested structure navigation (extracting specific attributes for multiple individuals), and interactive scripts (`datos_personales.py`) that initialize empty keys with `None` before populating them with user-entered contact details.

**Output:**

Specific values retrieved by keys, structured contact profile summaries, and nested dictionary extractions.

**Potential Applications:**

* User profile schemas, JSON-like data handling, API payload mapping, and configuration storage.

---

### `3.Funciones/`

**Objective:**
Implement reusable, modular code blocks with parameter handling, return statements, and conditional evaluation.

**Concepts Applied:**

* Function definition (`def`) and parameter passing
* Value returning (`return`)
* Logical checking within functions (`is_even`)
* List analysis functions (`max()`)
* Custom multi-operation logic (`calculadora`)

**Description:**
Features basic greeting functions, arithmetic addition with returned values, a parity evaluator (`espar`), a function determining maximum values in lists, and a command-line calculator (`calculadora.py`) processing user inputs for basic arithmetic operations (`+`, `-`, `*`, `/`).

**Output:**

Evaluated results returned from function invocations and dynamic arithmetic answers based on selected operations.

**Potential Applications:**

* Code reusability, procedural abstraction, custom validation logic, and execution breakdown.

---

### `4.Módulos/`

**Objective:**
Organize Python code into reusable external files and import custom module functions across different scripts.

**Concepts Applied:**

* Creating custom module files (`miprimermodulo.py`)
* Importing custom modules (`import`)
* Function namespace resolution (`module.function()`)

**Description:**
Defines mathematical operations (`suma`, `resta`, `multiplicacion`) in an external script `miprimermodulo.py`. The main script imports this module and delegates calculation calls based on user-provided integers.

**Output:**

Console display of batch mathematical evaluations processed by imported external functions.

**Potential Applications:**

* Separating utility tools, modularizing project codebases, and creating shareable internal libraries.
