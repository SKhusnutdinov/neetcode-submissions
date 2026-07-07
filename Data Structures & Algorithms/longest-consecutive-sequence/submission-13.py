class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hm = defaultdict(int)
        res = 0

        for num in nums:
            if hm[num] == 0:
                hm[num] = 1 + hm[num - 1] + hm[num + 1]
                hm[num - hm[num - 1]] = hm[num]
                hm[num + hm[num + 1]] = hm[num]
            res = max(res, hm[num])

        return res
