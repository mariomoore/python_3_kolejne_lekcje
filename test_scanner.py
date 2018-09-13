from scanner import *

TOKENS = [
    (r"^def", "DEF"),
    (r"^[a-zA-Z_][a-zA-Z0-9_]*", "NAME"),
    (r"^[0-9]+", "INTEGER"),
    (r"^\(", "LPAREN"),
    (r"^\)", "RPAREN"),
    (r"^\+", "PLUS"),
    (r"^:", "COLON"),
    (r"^,", "COMMA"),
    (r"^\s+", "INDENT"),
]

code = [
    "def sumoftwo(x, y):",
    "    print(x + y)",
    "sumoftwo(10, 20)",
]


def test_scan():
    scanner = Scanner(TOKENS)
    result = scanner.scan()
    assert result is None
    result = scanner.scan(code)
    assert result[0][0] == 'DEF'
    assert result[2][0] == 'NAME'


def test_match_peek_skip():
    scanner = Scanner(TOKENS, code)
    scanner.scan()
    scanner.skip()
    scanner.skip("XXX")
    scanner.skip()
    assert scanner.match("NAME")[1] == "sumoftwo"
    assert scanner.match("XXX") is None
    assert scanner.match() is None
    scanner.skip("LPAREN")
    assert scanner.peek()[0] == "NAME"
    assert scanner.peek("NAME")[0] == "NAME"
    assert scanner.match("NAME")[1] == "x"
    scanner.skip("COMMA", "INDENT")
    assert scanner.match("NAME")[1] == "y"
    scanner.skip("RPAREN", "COLON")
    assert scanner.match("INDENT")[1] == "    "
    assert scanner.match("NAME")[1] == "print"
    scanner.skip("LPAREN")
    assert scanner.match("NAME")[1] == "x"
    assert scanner.match("PLUS")[0] == "PLUS"
    assert scanner.match("NAME")[1] == "y"
    scanner.skip("RPAREN")
    assert scanner.peek() != "INDENT"
    assert scanner.match("NAME")[1] == "sumoftwo"
    scanner.skip("LPAREN")
    assert scanner.match("INTEGER")[1] == "10"
    scanner.skip("COMMA")
    assert scanner.match("INTEGER")[1] == "20"
    scanner.skip("RPAREN")


if __name__ == '__main__':
    test_scan()
    test_match_peek_skip()
