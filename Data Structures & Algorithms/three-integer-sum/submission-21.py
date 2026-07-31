class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for l, a in enumerate(nums):
            if a > 0:
                break
            if l > 0 and a == nums[l - 1]:
                continue
            mid = l + 1
            r = len(nums) - 1

            while mid < r:
                threeSum = a + nums[mid] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    mid += 1
                else:
                    res.append([a, nums[mid], nums[r]])
                    mid += 1
                    r -= 1
                    while nums[mid] == nums[mid - 1] and mid < r:
                        mid += 1
        return res