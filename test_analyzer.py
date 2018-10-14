from punypyparser import PunyPyWorld
from production import *
from analyzer import PunyPyAnalyzer


def test_analyzer():
    variables = {}
    world = PunyPyWorld(variables)
    # symulujemy hello(10 + 20)
    script = [FuncCall("hello", Parameters([AddExpr(IntExpr(10), IntExpr(20))]))]
    analyzer = PunyPyAnalyzer(script, world)
    analyzer.analyze()


if __name__ == '__main__':
    test_analyzer()
