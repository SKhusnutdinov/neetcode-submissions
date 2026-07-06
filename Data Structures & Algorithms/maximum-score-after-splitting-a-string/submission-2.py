class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        z = [0] * n
        o = [0] * n

        if s[0] == '0':
            z[0] = 1
        
        for i in range(1, n):
            z[i] = z[i-1]
            if s[i] == '0':
                z[i] += 1
        

        if s[n-1] == '1':
            o[n-1] = 1
        
        for i in range(n-2, -1, -1):
            o[i] = o[i+1]
            if s[i] == '1':
                o[i] += 1
        
        res = 0
        for i in range(1, n):
            res = max(res, z[i-1] + o[i])
        
        return res