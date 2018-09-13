import re


class Scanner(object):
    def __init__(self, regex, code=None):
        self.regex = regex
        self.code = code
        self.tokens = []
        self.script = []
        for r in regex:
            self.tokens.append((re.compile(r[0]), r[1]))

    def match_regex(self, i, line):
        start = line[i:]
        for regex, token in self.tokens:
            match = regex.match(start)
            if match:
                begin, end = match.span()
                return token, start[:end], end
        return None, start, None

    def scan(self, code=None):
        """Takes a string and runs the scan on it, creating a list of tokens
        for later. You should keep this string around for people to access
        later."""
        if code:
            self.code = code
        if self.code:
            self.script = []  # Zerowanie listy
            for line in self.code:
                i = 0
                while i < len(line):
                    token, string, end = self.match_regex(i, line)
                    assert token, "Nie udało się dopasować linii %s" % string
                    if token:
                        i += end
                        self.script.append((token, string, i, end))
            return self.script
        else:
            return None

    def match(self, *tokens):
        """Given a list of possible tokens, return the first one that matches
        the first token in the list and removes it."""
        if tokens:
            for token in list(tokens):
                index = 0
                for tkn in self.script:
                    if token == tkn[0]:
                        found = self.script.pop(index)
                        return found
                    index += 1
            return None
        else:
            return None

    def peek(self, *tokens):
        """Given a list of possible tokens, returns which ones could work with
        match but does not remove it from the list."""
        if tokens:
            for token in list(tokens):
                index = 0
                for tkn in self.script:
                    if token == tkn[0]:
                        return self.script[index]
                    index += 1
            return None
        else:
            return self.script[0]

    def push(self):
        """Push a token back on the token stream so that a later peek or match
        will return it."""
        pass

    def skip(self, *tokens):
        if tokens:
            for token in list(tokens):
                index = 0
                for tkn in self.script:
                    if token == tkn[0]:
                        self.script.pop(index)
                        break
                    index += 1
        else:
            self.script.pop(0)
