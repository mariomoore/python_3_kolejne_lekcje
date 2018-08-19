class DoubleLinkedListNode(object):

    def __init__(self, value, nxt, prev):
        self.value = value
        self.next = nxt
        self.prev = prev

    def __repr__(self):
        nval = self.next and self.next.value or None
        pval = self.prev and self.prev.value or None
        return f"[{self.value}, {repr(nval)}, {repr(pval)}]"


class DoubleLinkedList(object):

    def __init__(self):
        self.begin = None
        self.end = None

    def push(self, obj):
        """Dołącza nową wartość na końcu listy"""
        new_node = DoubleLinkedListNode(obj, None, None)
        if self.begin is None:
            self.begin = new_node
            self.end = self.begin
        else:
            last_node = self.end
            last_node.next = new_node
            new_node.prev = last_node
            self.end = new_node

    def pop(self):
        """Usuwa ostatni element i zwraca go"""
        if self.begin is None:
            return None
        elif self.begin == self.end:
            single_node = self.begin
            self.begin = self.end = None
            return single_node.value
        else:
            last_node = self.end
            previous_node = last_node.prev
            self.end = previous_node
            previous_node.next = None
            return last_node.value

    def shift(self, obj):
        """Inna nazwa dla push"""
        new_node = DoubleLinkedListNode(obj, None, None)
        if self.begin is None:
            self.begin = new_node
            self.end = self.begin
        else:
            first_node = self.begin
            self.begin = new_node
            new_node.next = first_node
            first_node.prev = new_node

    def unshift(self):
        """Usuwa pierwszy element (z początku) i zwraca go"""
        if self.begin is None:
            return None
        elif self.begin == self.end:
            single_node = self.begin
            self.begin = self.end = None
            return single_node.value
        else:
            first_node = self.begin
            new_first = first_node.next
            self.begin = new_first
            new_first.prev = None
            return first_node.value

    def detach_node(self, node):
        """Czasami trzeba użyć tej operacji, ale głównie wewnątrz
        remove(); powinna przyjmować węzeł i usuwać go z listy, bez względu
        na to, czy znajduje się na początku, w środku czy na końcu"""
        if node == self.begin:
            self.unshift()
        elif node == self.end:
            self.pop()
        else:
            previous_node = node.prev
            next_node = node.next
            previous_node.next = next_node
            next_node.prev = previous_node

    def remove(self, obj):
        """Znajduje pasujący element i usuwa go z listy"""
        if self.begin is None:
            return -1
        else:
            node = self.begin
            index = 0
            while node:
                if node.value == obj:
                    self.detach_node(node)
                    return index
                node = node.next
                index += 1
            return -1

    def first(self):
        """Zwraca *referencję* do pierwszego elementu, ale go nie usuwa"""
        if self.begin is None:
            return None
        else:
            node = self.begin
            return node.value

    def last(self):
        """Zwraca referencję do ostatniego elementu, ale go nie usuwa"""
        if self.begin is None:
            return None
        else:
            node = self.end
            return node.value

    def count(self):
        """Liczy liczbę elementów na liście"""
        if self.begin is None:
            return 0
        else:
            node = self.begin
            counter = 0
            while node:
                counter += 1
                node = node.next
            return counter

    def get(self, index):
        """Pobiera wartość z indeksu"""
        if self.begin is None:
            return None
        else:
            node = self.begin
            if index == 0:
                return node.value
            for i in range(1, index+1):
                node = node.next
                if node is None:
                    return None
            return node.value

    def dump(self, mark):
        """Funkcja debugowania, która zrzuca zawartość listy"""
        print(mark)
        if self.begin is None:
            print('Lista jest pusta!')
        else:
            node = self.begin
            while node:
                print(node.value)
                node = node.next
