class MyHashMap:

    def __init__(self):
        self.arr = [-1] * 1_000_001

    def put(self, key: int, value: int) -> None:
        self.arr[hash(key) % 1_000_001] = value

    def get(self, key: int) -> int:
        return self.arr[hash(key) % 1_000_001]

    def remove(self, key: int) -> None:
        self.arr[hash(key) % 1_000_000] = -1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)