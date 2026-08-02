class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}

        def work(i, curSum):
            if i >= len(nums):
                return curSum
            pair = (i, curSum)
            if pair in dp:
                return dp[pair]
            dp[pair] = max(work(i+1, curSum), work(i+2, curSum + nums[i]))
            return dp[pair]

        
        return work(0, 0)