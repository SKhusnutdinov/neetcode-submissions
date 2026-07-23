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
        hm = {None:None}
        newHead = None
        cur = head

        while cur:
            hm[cur] = Node(cur.val, cur.next, cur.random)
            cur = cur.next

        cur = head

        while cur:
            newHead = hm[cur]
            newHead.next = hm[newHead.next]
            newHead.random = hm[newHead.random]

            cur = cur.next
            newHead = newHead.next
        
        return hm[head]


            