# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(root, mx):
            if not root:
                return 0

            parent = 1 if root.val >= mx else 0
            left = dfs(root.left, max(mx, root.val))
            right = dfs(root.right, max(mx, root.val))

            return parent + left + right
        
        return dfs(root, root.val)