# ✎ᝰ.ᐟ⋆⑅˚₊ Z3 Equation Solver ✎ᝰ.ᐟ⋆⑅˚₊

## Overview

**Solver** is a Python-based tool designed to solve systems of equations and inequations using the [Z3 Theorem Prover](https://github.com/Z3Prover/z3). It was originally created as part of a programming assignment.

The core goal of this project is to implement a robust function that parses and solves systems of mathematical (in)equations when provided as a list of strings.

### 📝 Example

For instance, consider the following mathematical system:
> x + y + z = 10  
> x < y  
> 0 < x  
> x < 3  

In this solver, the system is expressed simply as a list of strings:
```python
exprs = ["x + y + z = 10", "x < y", "0 < x", "x < 3"]
```

## Project Structure

The codebase is organized into modular Python files to handle parsing and different types of expressions:
* `solver.py` - The main executable script that ties everything together.
* `parsers.py` / `arithmetical_parsers.py` / `boolean_parsers.py` - Scripts responsible for parsing strings into computable logic.
* `general_expressions.py` / `arithmetical_expressions.py` / `boolean_expressions.py` - Scripts defining the logical rules and structures for Z3 evaluation.

## Getting Started

### Requirements
This project relies on the Microsoft Z3 Theorem Prover Python binding. You need to install the `z3-solver` package to run the program.

Install it via `pip`:
```bash
pip install z3-solver
```

### Installation
Clone the repository to your local machine:
```bash
git clone https://github.com/maybe-im-a-mess/Solver.git
cd Solver
```

### Usage
To use the solver, run the main `solver.py` script from your terminal and pass your equations as parameters (or modify the script logic based on your desired inputs).

```bash
python solver.py
```
---
*Developed for parsing and solving equations efficiently using Z3.*
