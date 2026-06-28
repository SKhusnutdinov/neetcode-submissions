"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def trav(self, root, arr):
        if not root:
            return
        for ch in root.children:
            self.trav(ch, arr)
        arr.append(root.val)
    
    def postorder(self, root: 'Node') -> List[int]:
        arr = []

        self.trav(root, arr)

        return arr


    
   
