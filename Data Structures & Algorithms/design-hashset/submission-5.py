class MyHashSet:

    def __init__(self):
        self.arr = [False] * 1_000_000

    def add(self, key: int) -> None:
        self.arr[hash(key) % 1_000_000] = True

    def remove(self, key: int) -> None:
        self.arr[hash(key) % 1_000_000] = False

    def contains(self, key: int) -> bool:
        return self.arr[hash(key) % 1_000_000]
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)