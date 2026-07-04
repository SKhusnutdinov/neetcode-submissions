# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        p1 = head
        p2 = head.next

        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next
        print(p1.val)
        
        sec = p1.next
        prev = p1.next = None

        while sec:
            nxt = sec.next
            sec.next = prev
            prev = sec
            sec = nxt
    
        l1, l2 = head, prev

        while l2:
            nxt1, nxt2 = l1.next, l2.next
            l1.next = l2
            l2.next = nxt1
            l1, l2 = nxt1, nxt2
