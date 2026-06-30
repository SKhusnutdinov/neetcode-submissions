class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        hm = defaultdict(int)

        for num in nums:
            hm[num] += 1
        
        return sorted(nums, key=lambda x: (hm[x], -x))