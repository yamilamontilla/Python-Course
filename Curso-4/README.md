# Object-Oriented Programming (OOP)

Object-Oriented Programming (OOP) is a comprehensive collection of programs developed to strengthen foundational knowledge of object-oriented programming in Python. Each project addresses a specific programming concept, including classes, instance instantiation, inheritance hierarchies, abstract methods, polymorphism, and data encapsulation.

With a problem-solving oriented approach, this repository provides a centralized reference for exploring the fundamental principles of object-oriented design in Python.
It demonstrates how classes and objects can be used to model real-world entities, organize application logic, promote code reuse, and protect internal state, while serving as both a learning resource and a portfolio showcase.

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

* Comprehensive set of exercises covering the fundamentals of Object-Oriented Programming in Python.
* Implementation of custom classes, constructors, instance attributes, and methods.
* Exploration of inheritance hierarchies and code reuse through parent classes.
* Implementation of abstract base classes and polymorphic behavior.
* Demonstration of method overriding across specialized subclasses.
* Application of data encapsulation using private attributes.
* Emphasis on object-oriented design, abstraction, reusability, and data protection.
* Designed to serve both as a learning resource and as a portfolio showcase.

## Projects Included

---

### `1.Clases y Objetos/`

**Objective:**
Define custom classes, instantiate objects, manage internal state with constructors (`__init__`), and implement instance methods.

**Concepts Applied:**

* Class definition (`class`) and instance instantiation
* Constructor method (`__init__`) and attribute initialization
* Method definition with instance binding (`self`)
* State accumulation vs. stateless calculation

**Description:**
Includes a foundational `Persona` class for modeling real-world entities, a stateful calculator (`calculadora1`) that accumulates calculation results across chained operation calls, a stateless calculator (`calculadora2`) that evaluates two inputs on demand, and a word counter utility (`ContadorPalabras`) that parses string sentences with `split()` to maintain a running tally.

**Output:**

Personalized greeting messages, cumulative arithmetic balances, computed operator outputs, and total word counts.

**Potential Applications:**

* Modeling complex real-world domain entities, accumulating internal application states, and encapsulating business logic.

---

### `2.Herencia y Polimorfismo/`

**Objective:**
Establish hierarchical class relationships, inherit parent properties, and leverage abstract base classes for polymorphic behavior.

**Concepts Applied:**

* Class inheritance (`ChildClass(ParentClass)`)
* Code reuse through parent attributes and methods
* Abstract Base Classes (`ABC`, `@abstractmethod`)
* Polymorphic method overriding

**Description:**
Features a base `vehiculo` class extended by specialized child classes (`coche` and `motocicleta`) inheriting common properties while declaring specific behavior. Additionally, defines an abstract `Animal` interface enforcing concrete sound implementations across subclass extensions (`Perro` and `Gato`).

**Output:**

Derived vehicle behavior calls and sound outputs from polymorphic animal subclasses.

**Potential Applications:**

* Architectural class hierarchies, shared component systems, framework interfaces, and polymorphic contract enforcement.

---

### `3.Encapsulamiento/`

**Objective:**
Restrict direct external access to internal object state using private attribute name mangling.

**Concepts Applied:**

* Private class attributes (`__attribute`)
* Attribute encapsulation and access protection
* Controlled state modification via public methods

**Description:**
Demonstrates private variable protection by prefixing internal member attributes with double underscores (`__numero`). Proves that direct external assignment attempts do not mutate the protected internal state managed by class methods.

**Output:**

Internal calculation results verifying that encapsulated variables remain protected against unexpected direct overrides.

**Potential Applications:**

* Data protection, preventing unintended state mutation, and maintaining robust class APIs.
