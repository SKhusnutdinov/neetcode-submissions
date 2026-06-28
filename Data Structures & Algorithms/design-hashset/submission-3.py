class MyHashSet:

    def __init__(self):
        self.arr = [None] * 1_000_000

    def add(self, key: int) -> None:
        self.arr[hash(key) % 1_000_000] = key

    def remove(self, key: int) -> None:
        self.arr[hash(key) % 1_000_000] = None

    def contains(self, key: int) -> bool:
        if self.arr[hash(key) % 1_000_000]:
            return True
        else:
            return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)