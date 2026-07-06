class Solution:
    def maxScore(self, s: str) -> int:
        o = 0
        z = 0
        res = 0

        for ch in s:
            if ch == '1':
                o += 1
        
        for i in range(len(s)-1):
            if s[i] == '0':
                z += 1
            else:
                o -= 1
            res = max(res, z + o)
        return res