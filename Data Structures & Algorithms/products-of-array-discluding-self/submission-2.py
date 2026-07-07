class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prfl = [1]
        prfr = [1] * (len(nums) + 1)

        res = [0] * len(nums)

        for i in range(len(nums)):
            prfl.append(prfl[i] * nums[i])
        
        for j in range(len(nums) - 1, -1, -1):
            prfr[j] = prfr[j+1] * nums[j]

        print(prfl, prfr)
        for k in range(len(res)):
            res[k] = prfl[k] * prfr[k+1]

        return res
        
