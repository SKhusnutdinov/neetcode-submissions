class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [-1] * n
        
        def run(i):
            if i >= n:
                return 0
            if dp[i] != -1:
                return dp[i]
            
            dp[i] = min(run(i+1), run(i+2)) + cost[i]

            return dp[i]

        return min(run(0), run(1))