# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        if lists:
            dummy.next = lists[-1]

        for i in range(len(lists) - 2, -1, -1):
            lk = lists[i]
            def merge(alist):
                l1 = dummy.next
                l2 = alist
                cur = dummy

                while l1 and l2:
                    if l1.val < l2.val:
                        cur.next = l1
                        l1 = l1.next
                    else:
                        cur.next = l2
                        l2 = l2.next
                    cur = cur.next
                if l1:
                    cur.next = l1
                if l2:
                    cur.next = l2
                return
            merge(lk)

        return dummy.next