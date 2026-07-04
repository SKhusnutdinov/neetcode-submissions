# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        l1 = dummy.next

        for _ in range(1, left):
            prev = prev.next
            l1 = l1.next


        revPrev = None

        for _ in range(right - left + 1):
            nxt = l1.next
            l1.next = revPrev
            revPrev = l1
            l1 = nxt
        
        # l1 = 4, 5
        # revPrev = 3, 2, 1
        # prev = 0, 1

        prev.next.next = l1
        prev.next = revPrev

        
        return dummy.next