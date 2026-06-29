# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (p and not q) or (not p and q):
            return False
        q1 = deque()
        q2 = deque()
        q1.append(p)
        q2.append(q)

        while q and q2:
            if len(q1) != len(q2):
                return False
            
            for i in range(len(q1)):
                left = q1.popleft()
                right = q2.popleft()
                if not left and not right:
                    continue
                elif left and right:
                    if left.val != right.val:
                        return False
                    q1.append(left.left)
                    q1.append(left.right)
                    q2.append(right.left)
                    q2.append(right.right)
                else:
                    return False
        
        return True
            