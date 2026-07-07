class Solution:
    def sortColors(self, nums: List[int]) -> None:
        pz = 0
        pt = len(nums) - 1
        i = 0
        while i <= pt:
            if nums[i] == 0:
                nums[pz], nums[i] = nums[i], nums[pz]
                pz += 1
            if nums[i] == 2:
                nums[pt], nums[i] = nums[i], nums[pt]
                pt -= 1
                continue
            i += 1
        
