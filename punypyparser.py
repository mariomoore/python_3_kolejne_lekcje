import production


class Parser(object):

    def __init__(self, scanner):
        self.scanner = scanner

    def peek(self):
        return self.scanner.peek().name

    def match(self, *tokens):
        matched = self.scanner.match(*tokens)
        if matched:
            return matched.value
        else:
            return None

    def skip(self, *tokens):
        if tokens:
            self.scanner.skip(*tokens)
        else:
            self.scanner.skip()

    def root(self):
        pass

    def parse(self):
        results = []
        tokens = self.scanner.scan()
        while tokens:
            results.append(self.root())
        return results


class PunyPyParser(Parser):

    def __init__(self, scanner):
        Parser.__init__(self, scanner)

    def root(self):
        """root = *(funccal / funcdef)"""
        if self.peek() == 'INDENT':
            self.skip('INDENT')
        first = self.peek()

        if first == 'DEF':
            return self.function_definition()
        elif first == 'NAME':
            name = self.match('NAME')
            second = self.peek()

            if second == 'LPAREN':
                return self.function_call(name)
            else:
                assert False, "To nie jest FUNCDEF ani FUNCCALL"

    def function_definition(self):
        """
        funcdef = DEF name LPAREN params RPAREN COLON body
        W tym przykładzie ignoruję ciało, ponieważ jest to trudne
        To znaczy dlatego, żebyś sam nauczył się, jak to zrobić
        """
        self.skip('DEF', 'INDENT')
        name = self.match('NAME')
        self.skip('LPAREN')
        params = self.parameters()
        self.skip('RPAREN', 'COLON')
        body = self.function_body()
        # return {'type': 'FUNCDEF', 'name': name, 'params': params}
        return production.FuncDef(name, params, body)

    def function_body(self):
        body = []
        while self.skip("INDENT"):
            body.append(self.expression())
        return body

    def parameters(self):
        """params = expression *(COMMA expression)"""
        params = []
        start = self.peek()
        while start != 'RPAREN':
            params.append(self.expression())
            start = self.peek()
            if start != 'RPAREN':
                assert self.match('COMMA')
        # return params
        return production.Parameters(params)

    def function_call(self, name):
        """funccall = name LPAREN params RPAREN"""
        self.match('LPAREN')
        params = self.parameters()
        self.match('RPAREN')
        # return {'type': 'FUNCCALL', 'name': name, 'params': params}
        return production.FuncCall(name, params)

    def expression(self):
        """expression = name / plus / integer"""
        # scanner.skip('INDENT')
        if self.peek() == 'INDENT':
            self.skip('INDENT')
        start = self.peek()

        if start == 'NAME':
            name = self.match('NAME')
            # scanner.skip('INDENT')
            if self.peek() == 'INDENT':
                self.skip('INDENT')
            if self.peek() == 'PLUS':
                return self.plus(name)
            else:
                # return name
                return production.NameExpr(name)
        elif start == 'INTEGER':
            number = self.match('INTEGER')
            if self.peek()[0] == 'INDENT':
                self.skip('INDENT')
            if self.peek()[0] == 'PLUS':
                return self.plus(number)
            else:
                # return number
                return production.IntExpr(number)
        else:
            assert False, "Błąd składniowy %r" % start

    def plus(self, left):
        """plus = expression PLUS expression"""
        self.match('PLUS')
        right = self.expression()
        # return {'type': 'PLUS', 'left': left, 'right': right}
        return production.AddExpr(left, right)


class PunyPyWorld(object):

    def __init__(self, variables):
        self.variables = variables
        self.functions = {}
