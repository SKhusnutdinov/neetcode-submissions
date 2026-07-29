class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        s = []

        def dfs(op, cl):
            if len(s) >= 2*n:
                res.append("".join(s))
                return
            
            if op < n:
                s.append('(')
                dfs(op + 1, cl)
                s.pop()
            if cl < op:
                s.append(')')
                dfs(op, cl + 1)
                s.pop()
        
        dfs(0, 0)
        return res