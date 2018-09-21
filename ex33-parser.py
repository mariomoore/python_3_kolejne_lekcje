from scanner import *
from pprint import pprint

from test_scanner import TOKENS, code


def root(tokens):
    """root = *(funccal / funcdef)"""
    if scanner.peek()[0] == 'INDENT':
        scanner.skip('INDENT')
    first = scanner.peek()[0]

    if first == 'DEF':
        return function_definition(tokens)
    elif first == 'NAME':
        name = scanner.match('NAME')
        second = scanner.peek()[0]

        if second == 'LPAREN':
            return function_call(tokens, name)
        else:
            assert False, "To nie jest FUNCDEF ani FUNCCALL"


def function_definition(tokens):
    """
    funcdef = DEF name LPAREN params RPAREN COLON body
    W tym przykładzie ignoruję ciało, ponieważ jest to trudne
    To znaczy dlatego, żebyś sam nauczył się, jak to zrobić
    """
    scanner.skip('DEF', 'INDENT')
    name = scanner.match('NAME')[1]
    scanner.match('LPAREN')
    params = parameters(tokens)
    scanner.match('RPAREN')
    scanner.match('COLON')
    return {'type': 'FUNCDEF', 'name': name, 'params': params}


def parameters(tokens):
    """params = expression *(COMMA expression)"""
    params = []
    start = scanner.peek()[0]
    while start != 'RPAREN':
        params.append(expression(tokens))
        start = scanner.peek()[0]
        if start != 'RPAREN':
            assert scanner.match('COMMA')
    return params


def function_call(tokens, name):
    """funccall = name LPAREN params RPAREN"""
    scanner.match('LPAREN')
    params = parameters(tokens)
    scanner.match('RPAREN')
    return {'type': 'FUNCCALL', 'name': name, 'params': params}


def expression(tokens):
    """expression = name / plus / integer"""
    # scanner.skip('INDENT')
    if scanner.peek()[0] == 'INDENT':
        scanner.skip('INDENT')
    start = scanner.peek()[0]

    if start == 'NAME':
        name = scanner.match('NAME')[1]
        # scanner.skip('INDENT')
        if scanner.peek()[0] == 'INDENT':
            scanner.skip('INDENT')
        if scanner.peek()[0] == 'PLUS':
            return plus(tokens, name)
        else:
            return name
    elif start == 'INTEGER':
        number = scanner.match('INTEGER')[1]
        if scanner.peek()[0] == 'INDENT':
            scanner.skip('INDENT')
        if scanner.peek()[0] == 'PLUS':
            return plus(tokens, number)
        else:
            return number
    else:
        assert False, "Błąd składniowy %r" % start


def plus(tokens, left):
    """plus = expression PLUS expression"""
    scanner.match('PLUS')
    right = expression(tokens)
    return {'type': 'PLUS', 'left': left, 'right': right}


def main(tokens):
    results = []
    while tokens:
        results.append(root(tokens))
    return results


scanner = Scanner(TOKENS)
parsed = main(scanner.scan(code))
pprint(parsed)
