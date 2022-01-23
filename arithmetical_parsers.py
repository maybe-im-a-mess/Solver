from parsers import *
from arithmetical_expressions import *


class ParseAExpr(Parser):
    def __init__(self):
        self.parser = ParsePlus() ^ ParseTerm()


class ParseTerm(Parser):
    def __init__(self):
        self.parser = ParseTimes() ^ ParseFactor()


class ParseFactor(Parser):
    def __init__(self):
        self.parser = ParseCon() ^ ParseVar() ^ ParseParen()


class ParseCon(Parser):
    def __init__(self):
        self.parser = ParseInt() >> (lambda n:
                                     Return(Con(n)))


class ParseVar(Parser):
    def __init__(self):
        self.parser = ParseIdent() >> (lambda name:
                                       Return(Var(name)))


class ParseParen(Parser):
    def __init__(self):
        self.parser = ParseSymbol('(') >> (lambda _:
                                           ParseAExpr() >> (lambda e:
                                                            ParseSymbol(')') >> (lambda _:
                                                                                 Return(e))))


class ParsePlus(Parser):
    def __init__(self):
        self.parser = ParseTerm() >> (lambda t:
                                      ParseSymbol('+') >> (lambda _:
                                                           ParseAExpr() >> (lambda e:
                                                                            Return(Plus(t, e)))))


class ParseTimes(Parser):
    def __init__(self):
        self.parser = ParseFactor() >> (lambda x:
                                        ParseSymbol('*') >> (lambda _:
                                                             ParseTerm() >> (lambda y:
                                                                             Return(Times(x, y)))))
