# Solver
This solver was created as a part of a programming assignment.

The aim of this project is to implement a function that solves systems of equations and inequations. The (in)equations are given as lists of strings. For example, the system


>x + y + z = 10
> 
> x < y
> 
> 0 < x
> 
> x < 3

is expressed as the list
> exprs = [”x + y +z = 10”, ”x < y”, ”x < 3”, ”0 < x”]

<h3>Requirements:</h3>
- z3

To install z3, run the following command:
```pip install z3-solver```

<h3>How to use:</h3>
- Run "solver.py" and enter your equation as a parameter.
