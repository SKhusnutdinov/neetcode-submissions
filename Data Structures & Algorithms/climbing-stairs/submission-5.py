class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {}
        def run(n):
            if n <= 1:
                return 1
            if n in dp:
                return dp[n]
            
            dp[n] = run(n-1) + run(n-2)

            return dp[n]
        
        return run(n)
