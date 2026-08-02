class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1] * n
        def run(i):
            if n <= i:
                return i == n
            if dp[i] != -1:
                return dp[i]
            
            dp[i] = run(i+1) + run(i+2)

            return dp[i]
        
        return run(0)
