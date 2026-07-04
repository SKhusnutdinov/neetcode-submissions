class Solution:
    def check(self, nums: List[int]) -> bool:
        drop = 0
        for i in range(len(nums)):
            if nums[i] < nums[i-1]:
                drop += 1
                if drop == 2:
                    return False
        
        return True
