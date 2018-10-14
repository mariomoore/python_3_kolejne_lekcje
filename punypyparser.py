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


# class Fun_Def_Exp(object):
#
#     def __init__(self, type, name, params):
#         self.type = type
#         self.name = name
#         self.params = params


# class Fun_Cal_Exp(object):
#
#     def __init__(self, type, name, params):
#         self.type = type
#         self.name = name
#         self.params = params


# class Plu_Exp(object):
#
#     def __init__(self, type, left, right):
#         self.type = type
#         self.left = left
#         self.right = right


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
        self.skip('RPAREN')
        self.skip('COLON')
        return {'type': 'FUNCDEF', 'name': name, 'params': params}
        # return Fun_Def_Exp('FUNCDEF', name, params)

    def parameters(self):
        """params = expression *(COMMA expression)"""
        params = []
        start = self.peek()
        while start != 'RPAREN':
            params.append(self.expression())
            start = self.peek()
            if start != 'RPAREN':
                assert self.match('COMMA')
        return params

    def function_call(self, name):
        """funccall = name LPAREN params RPAREN"""
        self.match('LPAREN')
        params = self.parameters()
        self.match('RPAREN')
        return {'type': 'FUNCCALL', 'name': name, 'params': params}
        # return Fun_Cal_Exp('FUNCCALL', name, params)

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
                return name
        elif start == 'INTEGER':
            number = self.match('INTEGER')
            if self.peek()[0] == 'INDENT':
                self.skip('INDENT')
            if self.peek()[0] == 'PLUS':
                return self.plus(number)
            else:
                return number
        else:
            assert False, "Błąd składniowy %r" % start

    def plus(self, left):
        """plus = expression PLUS expression"""
        self.match('PLUS')
        right = self.expression()
        return {'type': 'PLUS', 'left': left, 'right': right}
        # return Plu_Exp('PLUS', left, right)
