class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [-1, -1]
        if not nums:
            return res
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2

            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        if nums[l] != target:
            return res
        res[0] = l
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r + 1) // 2

            if nums[mid] > target:
                r = mid - 1
            else:
                l = mid
        res[1] = r
        
        return res