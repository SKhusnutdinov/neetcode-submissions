class ListNode:
    def __init__(self, left = None, right = None, key = None, val = 0):
        self.left = left
        self.right = right
        self.key = key
        self.val = val

class LRUCache:

    def __init__(self, capacity: int):
        self.mem = {}
        self.leftBound = ListNode()
        self.rightBound = ListNode(self.leftBound)
        self.leftBound.right = self.rightBound
        self.size = 0
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.mem:
            self._nodeUsage(self.mem[key])
            return self.mem[key].val
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.mem:
            self._nodeUsage(self.mem[key])
            self.mem[key].val = value
        else:
            node = ListNode(key=key, val=value)
            self.mem[key] = node
            self._addNode(self.mem[key])
            self.size += 1
            if self.size > self.capacity:
                self._removeLastNode()
                self.size -= 1
    
    def _nodeUsage(self, node):
        left, right = node.left, node.right
        left.right, right.left = right, left

        self._addNode(node)
    
    def _addNode(self, node):
        rightNeigh = self.leftBound.right

        self.leftBound.right = node
        rightNeigh.left = node
        node.left, node.right = self.leftBound, rightNeigh
    
    def _removeLastNode(self):
        lastNode = self.rightBound.left

        left, right = lastNode.left, lastNode.right
        left.right, right.left = right, left
        self.mem.pop(lastNode.key)

            

        
