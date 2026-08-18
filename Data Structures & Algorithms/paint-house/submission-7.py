class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)

        dp = [[-1] * 4 for _ in range(n)]
        
        def dfs(i, prevColor):
            if i == n:
                return 0
            
            if dp[i][prevColor + 1] != -1:
                return dp[i][prevColor + 1]

            cost = float("inf")
            for j in range(3):
                if j == prevColor:
                    continue
                cost = min(cost, costs[i][j] + dfs(i+1, j))
            
            dp[i][prevColor + 1] = cost
            return cost
        
        return dfs(0, -1)
