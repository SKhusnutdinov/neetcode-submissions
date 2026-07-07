class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hm = {0 : 1}
        res = 0
        curSum = 0

        for i in range(len(nums)):
            curSum += nums[i]
            diff = curSum - k

            res += hm.get(diff, 0)

            hm[curSum] = hm.get(curSum, 0) + 1
    
        return res