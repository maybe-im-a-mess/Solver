result = lambda p: p[0][0]
rest = lambda p: p[0][1]


class Parser:
    def __xor__(self, other):
        return OrElse(self, other)

    def __rshift__(self, and_then):
        return Seq(self, and_then)

    def parse(self, inp):
        return self.parser.parse(inp)


class ParseItem(Parser):
    def parse(self, inp):
        if inp == "":
            return []
        return [(inp[0], inp[1:])]


class Return(Parser):
    def __init__(self, x):
        self.x = x

    def parse(self, inp):
        return [(self.x, inp)]


class Fail(Parser):
    def parse(self, inp):
        return []


class Seq(Parser):
    def __init__(self, first, and_then):
        self.first = first
        self.and_then = and_then

    def parse(self, inp):
        p = self.first.parse(inp)
        if p == []:
            return []
        return self.and_then(result(p)).parse(rest(p))


class OrElse(Parser):
    def __init__(self, parser1, parser2):
        self.parser1 = parser1
        self.parser2 = parser2

    def parse(self, inp):
        p = self.parser1.parse(inp)
        if p != []:
            return p
        return self.parser2.parse(inp)


class ParseChar(Parser):
    def __init__(self, x):
        self.parser = ParseIf(lambda c: c == x)


class ParseIf(Parser):
    def __init__(self, pred):
        self.parser = ParseItem() >> (lambda c: Return(c) if pred(c) else Fail())


class ParseSome(Parser):
    def __init__(self, parser):
        self.parser = parser >> (lambda x: (ParseSome(parser) ^ Return([])) >> (lambda xs: Return(cons(x, xs))))


class ParseMany(Parser):
    def __init__(self, parser):
        self.parser = ParseSome(parser) ^ Return([])


def cons(x, xs):
    if xs == [] and type(x) == str:
        return x
    if type(xs) == str:
        return x + xs
    return [x] + xs


class ParseInt(Parser):
    def __init__(self):
        self.parser = (ParseChar('-') >> (lambda _: ParseNat() >> (lambda n: Return(-n)))) ^ ParseNat()


class ParseNat(Parser):
    def __init__(self):
        self.parser = Seq(ParseSome(ParseDigit()), lambda ns: Return(int(ns)))


class ParseDigit(Parser):
    def __init__(self):
        self.parser = ParseIf(lambda c: c in "0123456789")


class ParseIdent(Parser):
    def __init__(self):
        self.parser = ParseIf(str.isalpha) >> (lambda c:
                                               ParseMany(ParseIf(str.isalnum)) >> (lambda cs:
                                                                                   Return(cons(c, cs))))


class ParseToken(Parser):
    def __init__(self, parser):
        self.parser = ParseMany(ParseIf(str.isspace)) >> (lambda _:
                                                          parser >> (lambda res:
                                                                     ParseMany(ParseIf(str.isspace)) >> (lambda _:
                                                                                                         Return(res))))


class ParseString(Parser):
    def __init__(self, string):
        self.parser = Return('') if string == '' else ParseChar(string[0]) >> (
            lambda c: ParseString(string[1:]) >> (lambda cs: Return(cons(c, cs))))


class ParseSymbol(Parser):
    def __init__(self, string):
        self.parser = ParseToken(ParseString(string))


class ParseIdentifier(Parser):
    def __init__(self):
        self.parser = ParseToken(ParseIdent())
