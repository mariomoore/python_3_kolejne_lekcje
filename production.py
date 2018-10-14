class Production(object):

    def analyze(self, world):
        """Tu zaimplementuj swój analizator"""


class FuncCall(Production):

    def __init__(self, name, params):
        self.name = name
        self.params = params

    def analyze(self, world):
        print("> FuncCall:", self.name)
        self.params.analyze(world)


class FuncDef(Production):

    def __init__(self, name, params, body):
        self.name = name
        self.params = params
        self.body = body

    def analyze(self, world):
        print("> FuncDef:", self.name)
        self.params.analyze(world)


class Parameters(Production):

    def __init__(self, expressions):
        self.expressions = expressions

    def analyze(self, world):
        print(">> Parameters:")
        for expr in self.expressions:
            expr.analyze(world)


class Expr(Production):
    pass


class NameExpr(Expr):

    def __init__(self, name):
        self.name = name

    def analyze(self, world):
        print(">>>> NameExpr:", self.name)


class IntExpr(Expr):

    def __init__(self, integer):
        self.integer = integer

    def analyze(self, world):
        print(">>>> IntExpr:", self.integer)


class AddExpr(Expr):

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def analyze(self, world):
        print(">>> AddExpr:")
        self.left.analyze(world)
        self.right.analyze(world)


