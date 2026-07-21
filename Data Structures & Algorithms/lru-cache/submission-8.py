class ListNode:
    def __init__(self, key, val, left=None, right=None):
        self.left = left
        self.right = right
        self.key = key
        self.val = val

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0

        self.hm = {}
        self.leftNode = ListNode(-1, -1)
        self.rightNode = ListNode(-1, -1, self.leftNode)
        self.leftNode.right = self.rightNode

    def get(self, key: int) -> int:
        node = self.hm.get(key, None)
        if node:
            node.left.right = node.right
            node.right.left = node.left
            self._place_last(node)
        return node.val if node else -1

    def put(self, key: int, value: int) -> None:
        node = None
        if key in self.hm:
            node = self.hm.get(key)
            node.val = value
            
            node.left.right = node.right
            node.right.left = node.left
        else:
            node = ListNode(key, value)
            self.hm[key] = node
            self.size += 1
        self._place_last(node)

        if self.size > self.capacity:
            lruNode = self.leftNode.right
            self.leftNode.right = lruNode.right
            lruNode.right.left = self.leftNode

            lruNode.left, lruNode.right = None, None
            self.hm.pop(lruNode.key)
            self.size -= 1
            
        
    def _place_last(self, node):
        prev = self.rightNode.left

        prev.right = node
        self.rightNode.left = node

        node.left = prev
        node.right = self.rightNode