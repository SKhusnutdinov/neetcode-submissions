"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hm = defaultdict(lambda: Node(0))
        hm[None] = None

        cur = head

        while cur:
            hm[cur].val = cur.val
            hm[cur].next = hm[cur.next]
            hm[cur].random = hm[cur.random]

            cur = cur.next
        return hm[head]


            