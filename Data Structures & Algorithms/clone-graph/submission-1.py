"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        q = deque()
        q.append(node)
        hm = {}
        hm[node] = Node(node.val)

        while q:
            for _ in range(len(q)):
                curNode = q.popleft()
                for neigh in curNode.neighbors:
                    if neigh not in hm:
                        hm[neigh] = Node(neigh.val)
                        q.append(neigh)
                    hm[curNode].neighbors.append(hm[neigh])
        
        return hm[node]
                        