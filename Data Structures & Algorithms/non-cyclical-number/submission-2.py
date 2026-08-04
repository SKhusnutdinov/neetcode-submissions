class Solution:
    def isHappy(self, n: int) -> bool:
        dp = set()
        
        while n != 1 and n not in dp:
            dp.add(n)
            tmp = 0
            for ch in str(n):
                tmp += (int(ch) * int(ch))
                
            n = int(tmp)
        
        return not n in dp