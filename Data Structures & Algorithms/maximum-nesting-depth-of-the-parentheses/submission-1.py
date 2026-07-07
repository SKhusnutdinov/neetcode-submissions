class Solution:
    def maxDepth(self, s: str) -> int:
        mx = 0
        cur = 0

        for ch in s:
            if ch == '(':
                cur += 1
            elif ch == ')':
                mx = max(mx, cur)
                cur -= 1
        
        return mx