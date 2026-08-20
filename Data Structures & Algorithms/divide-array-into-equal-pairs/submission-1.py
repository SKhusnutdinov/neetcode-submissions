class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        hm = Counter(nums)

        for value in hm.values():
            if value % 2 == 1:
                return False
        
        return True