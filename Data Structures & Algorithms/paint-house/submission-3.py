class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)

        dp = {}
        
        def dfs(i, prevColor):
            if i == n:
                return 0
            
            if (i, prevColor) in dp:
                return dp[(i, prevColor)]

            cost = float("inf")
            for j in range(3):
                if j == prevColor:
                    continue
                
                cost = min(cost, costs[i][j] + dfs(i+1, j))
            
            dp[(i, prevColor)] = cost
            return cost
        
        return dfs(0, -1)
