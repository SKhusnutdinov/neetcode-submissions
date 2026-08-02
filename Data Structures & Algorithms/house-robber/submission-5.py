class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-1] * len(nums)

        def work(i):
            if i >= len(nums):
                return 0
            if dp[i] != -1:
                return dp[i]
            dp[i] = max(work(i+1), nums[i] + work(i+2))
            return dp[i]
        
        return work(0)