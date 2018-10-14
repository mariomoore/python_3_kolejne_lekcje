from test_scanner import TOKENS, code
from scanner import *
from punypyparser import PunyPyParser


def test_parser():
    scanner = Scanner(TOKENS, code)
    scanner.scan()
    parser = PunyPyParser(scanner)
    assert parser.match('XXX') is None
    assert parser.match('DEF') == 'def'
    parser.skip()  # ' '
    assert parser.peek() == 'NAME'
    assert parser.match('NAME') == 'sumoftwo'
    assert parser.match('DEF', 'LPAREN') == '('
    assert parser.match() is None


def test_punypyparser():
    scanner = Scanner(TOKENS, code)
    # scanner.scan()
    parser = PunyPyParser(scanner)
    results = parser.parse()
    print(results)


if __name__ == '__main__':
    test_punypyparser()
