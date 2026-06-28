"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    
    
    def postorder(self, root: 'Node') -> List[int]:
        arr = []


        def trav(root):
            if not root:
                return
            for ch in root.children:
                trav(ch)
            arr.append(root.val)

        trav(root)

        return arr


    
   
