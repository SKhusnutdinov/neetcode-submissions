class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = [[-1] * 2 for _ in range(len(nums))]
        
        def run(i, flag):
            if i >= n or (flag and i == (n-1)):
                return 0
            if dp[i][flag] != -1:
                return dp[i][flag]
            
            dp[i][flag] = max(run(i+1, flag), nums[i] + run(i+2, flag or i == 0))

            return dp[i][flag]


        return max(run(0, True), run(1, False))