# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        mx = 0

        def dfs(root):
            nonlocal mx
            if not root:
                return 0
            
            left, right = dfs(root.left), dfs(root.right)
            mx = max(mx, left + right)

            return 1 + max(left, right)
        
        dfs(root)

        return mx