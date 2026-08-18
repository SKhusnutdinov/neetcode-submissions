class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        if n == 0:
            return 0

        dp = [[0] * 3 for _ in range(n)]
        for c in range(3):
            dp[0][c] = costs[0][c]

        for i in range(1, n):
            for c in range(3):
                dp[i][c] = (
                    costs[i][c] +
                    min(dp[i - 1][(c + 1) % 3], dp[i - 1][(c + 2) % 3])
                )

        return min(dp[n - 1])