import z3


class BExpr:
    pass


class BVar(BExpr):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def ev(self, env):
        return env[self.name]

    def toZ3(self):
        return z3.Int(f'{self.name}')


class Op2(BExpr):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return f"({self.left} {self.op} {self.right})"

    def ev(self, env):
        return self.fun(self.left.ev(env), self.right.ev(env))


class Or(Op2):
    op = "or"
    fun = lambda _, x, y: x or y

    def toZ3(self):
        return z3.Or(self.left.toZ3(), self.right.toZ3())


class And(Op2):
    op = "and"
    fun = lambda _, x, y: x and y

    def toZ3(self):
        return z3.And(self.left.toZ3(), self.right.toZ3())


class Equals(Op2):
    op = "="
    fun = lambda _, x, y: x == y

    def toZ3(self):
        return self.fun(self.left.toZ3(), self.right.toZ3())


class Less(Op2):
    op = "<"
    fun = lambda _, x, y: x < y

    def toZ3(self):
        return self.fun(self.left.toZ3(), self.right.toZ3())
