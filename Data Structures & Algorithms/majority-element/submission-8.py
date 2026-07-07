class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cur = nums[0]

        freq = 1

        for i in range(1, len(nums)):
            if nums[i] != cur:
                freq -= 1
                if freq == 0:
                    freq = 1
                    cur = nums[i]
            else:
                freq += 1
        
        return cur