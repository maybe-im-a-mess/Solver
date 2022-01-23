from boolean_parsers import *
from arithmetical_parsers import *


class ParseExpr(Parser):
    def __init__(self):
        self.parser = ParseBExpr() ^ ParseAExpr()


def printExpr(inp):
    print(result(ParseExpr().parse(inp)))


def evalExpr(inp, env):
    return result(ParseExpr().parse(inp)).ev(env)
