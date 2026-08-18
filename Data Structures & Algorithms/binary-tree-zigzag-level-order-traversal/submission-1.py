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
        st = []
        res = []

        direction = False

        while q:
            cur = []
            for _ in range(len(q)):
                node = q.popleft()
                if direction:
                    if node.right:
                        st.append(node.right)
                    if node.left:
                        st.append(node.left)
                else:
                    if node.left:
                        st.append(node.left)
                    if node.right:
                        st.append(node.right)
                
                cur.append(node.val)
            while st:
                q.append(st.pop())
            res.append(cur)
            direction = not direction
    
        return res
