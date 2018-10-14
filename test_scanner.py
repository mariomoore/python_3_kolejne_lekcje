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


def test_token():
    token = Token("Name", "Value", 0, 4)
    assert token.name == 'Name'
    assert token.value == 'Value'
    assert token.line == 0
    assert token.start == 4
    assert token.length == 5


def test_scan():
    scanner = Scanner(TOKENS)
    result = scanner.scan()
    assert result is None
    result = scanner.scan(code)
    assert result[0].name == 'DEF'
    assert result[2].name == 'NAME'


def test_match_peek_skip():
    scanner = Scanner(TOKENS, code)
    scanner.scan()
    scanner.skip()  # 'def'
    scanner.skip("XXX")
    scanner.skip()  # ' '
    assert scanner.match("NAME").value == "sumoftwo"
    assert scanner.match("XXX") is None
    assert scanner.match() is None
    scanner.skip("LPAREN")
    assert scanner.peek().name == "NAME"
    assert scanner.peek("NAME").name == "NAME"
    assert scanner.peek().length == 1
    assert scanner.peek("XXX", 'YYY') is None
    assert scanner.match("NAME").value == "x"
    scanner.skip("COMMA", "INDENT")
    assert scanner.match("NAME").value == "y"
    scanner.skip("RPAREN", "COLON")
    assert scanner.match("INDENT").value == "    "
    assert scanner.match("NAME").value == "print"
    scanner.skip("LPAREN")
    assert scanner.match("NAME").value == "x"
    assert scanner.match("PLUS").name == "PLUS"
    assert scanner.match("NAME").value == "y"
    scanner.skip("RPAREN")
    assert scanner.peek() != "INDENT"
    assert scanner.match("NAME").value == "sumoftwo"
    scanner.skip("LPAREN")
    assert scanner.match("INTEGER").value == "10"
    scanner.skip("COMMA")
    assert scanner.match("INTEGER").value == "20"
    scanner.skip("RPAREN")


if __name__ == '__main__':
    test_match_peek_skip()
