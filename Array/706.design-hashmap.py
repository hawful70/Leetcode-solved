class MyHashMap:

    def __init__(self):
       self.capacity = 1000
       self.table = [[] for _ in range(self.capacity)]

    def calculate_hash_index(self, key):
        return key % self.capacity 

    def put(self, key: int, value: int) -> None:
        index = self.calculate_hash_index(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        self.table[index].append((key, value))

    def get(self, key: int) -> int:
        index = self.calculate_hash_index(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        index = self.calculate_hash_index(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return