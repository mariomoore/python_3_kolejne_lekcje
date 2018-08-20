from dllist import DoubleLinkedList


class Dictionary(object):
    def __init__(self, num_buckets=256):
        """Inicjalizuje mapę z daną liczbą wiaderek"""
        self.map = DoubleLinkedList()
        for _ in range(0, num_buckets):
            self.map.push(DoubleLinkedList())

    def hash_key(self, key):
        """Dla danego klucza utworzy liczbę i przekonwertuje ją na
        indeks dla wiaderek mapy"""
        return hash(key) % self.map.count()

    def get_bucket(self, key):
        """Dla danego klucza znajduje wiaderko, w którym powinien być umieszczony"""
        bucket_id = self.hash_key(key)
        return self.map.get(bucket_id)

    def get_slot(self, key, default=None):
        """Zwraca wiaderko i węzeł dla slotu albo None, None"""
        bucket = self.get_bucket(key)
        if bucket:
            node = bucket.begin
            i = 0
            while node:
                if key == node.value[0]:
                    return bucket, node
                else:
                    node = node.next
                    i += 1
        # Przechodzi zarówno przez if, jak i while powyżej
        return bucket, None

    def get(self, key, default=None):
        """Pobiera wartość z wiaderka dla danego klucza lub wartość domyślną"""
        bucket, node = self.get_slot(key, default=default)
        return node and node.value[1] or node

    def set(self, key, value):
        """Ustawia wartość dla klucza, zastępując istniejącą wartość"""
        bucket, slot = self.get_slot(key)
        if slot:
            # Jeśli klucz istnieje, zastępuje go
            slot.value = (key, value)
        else:
            # Jeśli klucz nie istnieje, dodaje go
            bucket.push((key, value))

    def delete(self, key):
        """Usuwa dany klucz z mapy"""
        bucket = self.get_bucket(key)
        node = bucket.begin
        while node:
            k, v = node.value
            if key == k:
                bucket.detach_node(node)
                break

    def list(self):
        """Wypisuje, co znajduje się w mapie"""
        bucket_node = self.map.begin
        while bucket_node:
            slot_node = bucket_node.value.begin
            while slot_node:
                print(slot_node.value)
                slot_node = slot_node.next
            bucket_node = bucket_node.next
