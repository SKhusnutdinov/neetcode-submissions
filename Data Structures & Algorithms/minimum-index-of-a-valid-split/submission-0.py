class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        count = Counter(nums)
        hm = defaultdict(int)

        for i in range(len(nums)):
            hm[nums[i]] += 1
            count[nums[i]] -= 1

            left_len = i + 1
            right_len = len(nums) - i - 1

            if 2 * hm[nums[i]] > left_len and 2 * count[nums[i]] > right_len:
                return i
        
        return -1

        