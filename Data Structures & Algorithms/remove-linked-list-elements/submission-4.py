# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return None

        dummy = ListNode(-1, head)

        prev = dummy
        cur = dummy.next

        while cur:
            next = cur.next

            if cur.val == val:
                prev.next = next
            else:
                prev = cur
                
            cur = next
        
        return dummy.next


