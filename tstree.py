class TSTreeNode(object):
    def __init__(self, key, value, low, eq, high):
        self.key = key
        self.low = low
        self.eq = eq
        self.high = high
        self.value = value


class TSTree(object):
    def __init__(self):
        self.root = None

    def _get(self, node, keys):
        key = keys[0]
        if node:  # Warunek if-else dopisany do oryginalnego kodu
            if key < node.key:
                return self._get(node.low, keys)
            elif key == node.key:
                if len(keys) > 1:
                    return self._get(node.eq, keys[1:])
                else:
                    return node.value
            else:
                return self._get(node.high, keys)
        else:
            return None

    def get(self, key):
        keys = [x for x in key]
        return self._get(self.root, keys)

    def _set(self, node, keys, value):
        next_key = keys[0]
        if not node:
            # Co się stanie, jeśli dodasz wartość tutaj?
            node = TSTreeNode(next_key, None, None, None, None)
        if next_key < node.key:
            node.low = self._set(node.low, keys, value)
        elif next_key == node.key:
            if len(keys) > 1:
                node.eq = self._set(node.eq, keys[1:], value)
            else:
                # Co się stanie, jeśli NIE dodasz wartości tutaj?
                node.value = value
        else:
            node.high = self._set(node.high, keys, value)
        return node

    def set(self, key, value):
        keys = [x for x in key]
        self.root = self._set(self.root, keys, value)

    def _find_all(self, node, keys, subword, all_matching):
        if node:
            if node.value is not None:
                whole_word = subword + node.key
                all_matching.append({whole_word: node.value})
            if keys:
                key = keys[0]
                if key < node.key:
                    self._find_all(node.low, keys, subword, all_matching)
                elif key > node.key:
                    self._find_all(node.high, keys, subword, all_matching)
                elif key == node.key:
                    subword = subword + node.key
                    if len(keys) > 1:
                        self._find_all(node.eq, keys[1:], subword, all_matching)
                    elif len(keys) == 1:
                        self._find_all(node.eq, None, subword, all_matching)
            else:
                self._find_all(node.low, None, subword, all_matching)
                self._find_all(node.high, None, subword, all_matching)
                subword = subword + node.key
                self._find_all(node.eq, None, subword, all_matching)

    def find_all(self, key):
        all_matching = []
        keys = [x for x in key]
        subword = ''
        self._find_all(self.root, keys, subword, all_matching)
        if all_matching:
            return all_matching
        else:
            return None

    def find_shortest(self, key):
        all_matching = self.find_all(key)
        shortest_key = None
        shortest_value = None
        if all_matching:
            for n in all_matching:
                if shortest_key:
                    if len(list(n.keys())[0]) < len(shortest_key):
                        shortest_key = list(n.keys())[0]
                        shortest_value = n[shortest_key]
                else:
                    shortest_key = list(n.keys())[0]
                    shortest_value = n[shortest_key]
            return {shortest_key: shortest_value}
        else:
            return None

    def find_longest(self, key):
        all_matching = self.find_all(key)
        longest_key = None
        longest_value = None
        if all_matching:
            for n in all_matching:
                if longest_key:
                    if len(list(n.keys())[0]) > len(longest_key):
                        longest_key = list(n.keys())[0]
                        longest_value = n[longest_key]
                else:
                    longest_key = list(n.keys())[0]
                    longest_value = n[longest_key]
            return {longest_key: longest_value}
        else:
            return None

    def find_part(self, key):
        key_prefixes = []
        shortests = []
        for i in range(len(key)):
            key_prefixes.append(key[:i+1])
        for p in key_prefixes:
            shortest = self.find_shortest(p)
            if shortest:
                shortests.append(shortest)
        shortest_key = None
        shortest_value = None
        if shortests:
            for n in shortests:
                if shortest_key:
                    if len(list(n.keys())[0]) < len(shortest_key):
                        shortest_key = list(n.keys())[0]
                        shortest_value = n[shortest_key]
                else:
                    shortest_key = list(n.keys())[0]
                    shortest_value = n[shortest_key]
            return {shortest_key: shortest_value}
        else:
            return None
