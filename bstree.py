class BSTreeNode(object):
    def __init__(self, key, value, parent=None):
        self.key = key
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None


class BSTree(object):
    def __init__(self):
        self.root = None

    def set(self, key, value):
        if self.root is None:
            self.root = self.insert(self.root, key, value, None)
        else:
            self.insert(self.root, key, value, self.root)

    def get(self, key):
        return self.search_value_by_key(key, self.root)

    def delete(self, key):
        node_to_del = self.search_node_by_key(key, self.root)
        new_parent = node_to_del.parent
        # Potomek lewy i prawy jest pusty
        if node_to_del.left is None and node_to_del.right is None:
            # Jedyny element. Sprawdzenie warunku można wynieść wyżej
            if node_to_del == self.root:
                self.root = None
            # Wiele elementów
            elif new_parent.left == node_to_del:
                new_parent.left = None
            else:
                new_parent.right = None
        # potomek lewy i prawy istnieje
        elif node_to_del.left is not None and node_to_del.right is not None:
            # Przeniesienie minimum w miejsce węzła do usunięcia
            minimum_right = self.find_minimum(node_to_del.right)
            node_to_del.key = minimum_right.key
            node_to_del.value = minimum_right.value
            # Usuwanie minimum
            minimum_parent = minimum_right.parent
            minimum_child = minimum_right.right
            if minimum_child is not None:
                minimum_child.parent = minimum_parent
            minimum_parent.left = minimum_child
        # jeden potomek istnieje, drugi jest pusty
        else:
            child = node_to_del.left or node_to_del.right
            if new_parent is None:
                child.parent = None
                self.root = child
            elif new_parent.left == node_to_del:
                child.parent = new_parent
                new_parent.left = child
            else:
                child.parent = new_parent
                new_parent.right = child

    def list(self):
        if self.root is not None:
            print('{', end='', flush=True)
            self.print_from_top(self.root)
            print('}')

            # print('{', end='', flush=True)
            # self.print_from_bottom(self.root)
            # print('}')
        else:
            print('Lista jest pusta')

    def insert(self, node, key, value, parent):
        if node is None:
            node = BSTreeNode(key, value)
            node.parent = parent
        elif key == node.key:
            node.value = value
        elif key < node.key:
            node.left = self.insert(node.left, key, value, node)
        else:
            node.right = self.insert(node.right, key, value, node)
        return node

    def search_value_by_key(self, key, node):
        if node is None:
            return None
        elif key == node.key:
            return node.value
        elif key < node.key:
            return self.search_value_by_key(key, node.left)
        else:
            return self.search_value_by_key(key, node.right)

    def search_node_by_key(self, key, node):
        if key == node.key or node is None:
            return node
        elif key < node.key:
            return self.search_node_by_key(key, node.left)
        else:
            return self.search_node_by_key(key, node.right)

    def find_minimum(self, node):
        if node.left is None:
            return node
        else:
            self.find_minimum(node.left)

    def print_from_top(self, node):
        print("'", node.key, "': '", node.value, "'", end='', sep='', flush=True)
        if node.left is not None:
            print(", ", end='', flush=True)
            self.print_from_top(node.left)
        if node.right is not None:
            print(", ", end='', flush=True)
            self.print_from_top(node.right)

    def print_from_bottom(self, node):
        if node.left is not None:
            self.print_from_bottom(node.left)
        if node.right is not None:
            self.print_from_bottom(node.right)
        print("'", node.key, "': '", node.value, "'", end='', sep='', flush=True)
