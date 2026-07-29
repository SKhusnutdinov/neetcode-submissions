# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        res = 0
        
        def dfs(root, res):
            if not root:
                return False
            res += root.val

            if not root.left and not root.right:
                return res == targetSum
            
            return dfs(root.left,res) or dfs(root.right,res)
        
        return dfs(root,0)