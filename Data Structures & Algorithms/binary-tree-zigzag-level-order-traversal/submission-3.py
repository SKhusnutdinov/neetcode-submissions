# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque([root])
        res = []

        while q:
            size = len(q)
            cur = [0] * size
            for i in range(size):
                node = q.popleft()
                idx = size - i - 1 if len(res) % 2 else i
                cur[idx] = node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        
            res.append(cur)
    
        return res
