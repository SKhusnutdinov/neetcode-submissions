class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        min1 = prices[0]

        for i in range(1, len(prices)):
            res = max(res, prices[i] - min1)
            min1 = min(min1, prices[i])
        
        return res