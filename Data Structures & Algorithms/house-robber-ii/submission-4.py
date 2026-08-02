class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        mp = {}
        
        def run(i, flag):
            if flag and i == (n-1):
                return 0
            if i >= n:
                return 0
            pair = (i, flag)
            if pair in mp:
                return mp[pair]
            
            mp[pair] = max(run(i+1, flag), nums[i] + run(i+2, flag or i == 0))
            return mp[pair]


        return max(run(0, True), run(1, False))