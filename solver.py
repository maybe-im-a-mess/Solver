from general_expressions import *
from z3 import *


def solve(exprs):
    s = Solver()
    for el in exprs:
        s.add(result(ParseExpr().parse(el)).toZ3())
    if s.check() == sat:
        solutions = set()
        for var in s.model():
            solutions.add(f'{var} = {s.model()[var]}')
        return solutions
    else:
        print("No solution!")


print(solve(["x + y +z = 10", "x < y", "x < 3", "0 < x"]))
