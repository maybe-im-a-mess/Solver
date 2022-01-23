import z3


class AExpr:
    def __add__(self, other):
        return Plus(self, other)

    def __mul__(self, other):
        return Times(self, other)


class Con(AExpr):
    def __init__(self, val):
        self.val = val

    def __str__(self):
        return str(self.val)

    def ev(self, env):
        return self.val

    def toZ3(self):
        return self.val


class Var(AExpr):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def ev(self, env):
        return env[self.name]

    def toZ3(self):
        return z3.Int(f'{self.name}')


class BinOp(AExpr):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return f"({self.left} {self.op} {self.right})"

    def ev(self, env):
        return self.fun(self.left.ev(env), self.right.ev(env))

    def toZ3(self):
        return self.fun(self.left.toZ3(), self.right.toZ3())


class Plus(BinOp):
    fun = lambda _, x, y: x + y
    op = '+'


class Times(BinOp):
    fun = lambda _, x, y: x * y
    op = '*'
