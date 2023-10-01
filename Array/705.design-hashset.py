class MyHashSet:
    def __init__(self):
       self.capacity = 1000
       self.table = [[] for _ in range(self.capacity)]

    def calculate_hash_index(self, key):
        return key % self.capacity

    def add(self, key: int) -> None:
        index = self.calculate_hash_index(key)
        if not self.contains(key):
            self.table[index].append(key)

    def remove(self, key: int) -> None:
        index = self.calculate_hash_index(key)
        for i, k in enumerate(self.table[index]):
            if k == key:
                self.table[index].remove(key)

    def contains(self, key: int) -> bool:
        index = self.calculate_hash_index(key)
        for i, k in enumerate(self.table[index]):
            if k == key:
                return True
        return False