from boolean_expressions import *
from arithmetical_parsers import *


class ParseBExpr(Parser):
    def __init__(self):
        self.parser = ParseOr() ^ ParseDisj()


class ParseDisj(Parser):
    def __init__(self):
        self.parser = ParseAnd() ^ ParseConj()


class ParseConj(Parser):
    def __init__(self):
        self.parser = ParseCmp() ^ ParseBParen()


class ParseCmp(Parser):
    def __init__(self):
        self.parser = ParseEquals() ^ ParseLess()


class ParseEquals(Parser):
    def __init__(self):
        self.parser = ParseAExpr() >> (lambda a:
                                       ParseSymbol("=") >> (lambda _:
                                                            ParseAExpr() >> (lambda b:
                                                                             Return(Equals(a, b)))))


class ParseLess(Parser):
    def __init__(self):
        self.parser = ParseAExpr() >> (lambda s:
                                       ParseSymbol("<") >> (lambda _:
                                                            ParseAExpr() >> (lambda t:
                                                                             Return(Less(s, t)))))


class ParseBVar(Parser):
    def __init__(self):
        self.parser = ParseIdentifier() >> (lambda name:
                                            Return(BVar(name)))


class ParseBParen(Parser):
    def __init__(self):
        self.parser = ParseSymbol("(") >> (lambda _:
                                           ParseBExpr() >> (lambda e:
                                                            ParseSymbol(")") >> (lambda _:
                                                                                 Return(e))))


class ParseOr(Parser):
    def __init__(self):
        self.parser = ParseDisj() >> (lambda d:
                                      ParseSymbol("or") >> (lambda _:
                                                            ParseBExpr() >> (lambda e:
                                                                             Return(Or(d, e)))))


class ParseAnd(Parser):
    def __init__(self):
        self.parser = ParseConj() >> (lambda x:
                                      ParseSymbol("and") >> (lambda _:
                                                             ParseDisj() >> (lambda y:
                                                                             Return(And(x, y)))))
