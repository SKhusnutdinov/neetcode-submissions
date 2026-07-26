class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        freq = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            count[num] += 1
        
        for key, val in count.items():
            freq[val].append(key)

        res = []
        
        for i in range(len(freq) - 1, -1, -1):
            for j in range(len(freq[i]) - 1, -1, -1):
                res.append(freq[i][j])
                if len(res) == k:
                    return res
                    