class SingleLinkedListNode(object):

    def __init__(self, value, nxt):
        self.value = value
        self.next = nxt

    def __repr__(self):
        nval = self.next and self.next.value or None
        return f"[{self.value}:{repr(nval)}]"


class SingleLinkedList(object):

    def __init__(self):
        self.begin = None
        self.end = None

    def push(self, obj):
        """Dołącza nową wartość na końcu listy"""
        new_node = SingleLinkedListNode(obj, None)
        if self.begin is None:
            self.begin = new_node
            self.end = self.begin
        else:
            self.end.next = new_node
            self.end = new_node

    def pop(self):
        """Usuwa ostatni element i zwraca go"""
        if self.end is None:
            return None
        elif self.end == self.begin:
            element = self.begin
            self.begin = self.end = None
            return element.value
        else:
            element = self.begin
            while element.next != self.end:
                element = element.next
            temp = self.end
            self.end = element
            element.next = None
            return temp.value

    def shift(self, obj):
        """Inna nazwa dla push"""
        new_node = SingleLinkedListNode(obj, None)
        if self.begin is None:
            self.begin = new_node
            self.end = self.begin
        else:
            new_node.next = self.begin
            self.begin = new_node

    def unshift(self):
        """Usuwa pierwszy element i zwraca go"""
        if self.end is None:
            return None
        elif self.end == self.begin:
            temp = self.begin
            self.begin = self.end = None
            return temp.value
        else:
            temp = self.begin
            self.begin = temp.next
            return temp.value

    def remove(self, obj):
        """Znajduje pasujący element i usuwa go z listy"""
        if self.begin is None:
            return -1  # Lista jest pusta
        else:
            node = self.begin
            if node.value == obj:
                self.begin = node.next
                return 0  # Pierwszy element na liście
            else:
                previous = self.begin
                node = previous.next  # Albo drugi element, albo None
                index = 1
                while node:
                    if node.value == obj:
                        previous.next = node.next
                        return index
                    else:
                        previous = previous.next
                        node = node.next
                        index += 1
                return -1  # Nic nie znaleziono na liście

    def first(self):
        """Zwraca *referencję* do pierwszego elementu, ale go nie usuwa"""
        if self.begin is None:
            return None
        else:
            node = self.begin
            return node.value

    def last(self):
        """Zwraca referencję do ostatniego elementu, ale go nie usuwa"""
        if self.end is None:
            return None
        else:
            node = self.end
            return node.value

    def count(self):
        """Liczy liczbę elementów na liście"""
        counter = 0
        node = self.begin
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
            for i in range(1, index + 1):
                node = node.next
                if node is None:
                    return None
            return node.value

    def dump(self, mark):
        """Funkcja debugowania, która zrzuca zawartość listy"""
        print(mark)
        if self.begin is not None:
            node = self.begin
            while node:
                print(node.value)
                node = node.next
