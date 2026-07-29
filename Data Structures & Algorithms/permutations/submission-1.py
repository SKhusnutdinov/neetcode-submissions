class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        chose = [False] * len(nums)

        def dfs():
            if len(subset) == len(nums):
                res.append(subset[:])
                return
            
            for j in range(len(chose)):
                if not chose[j]:
                    subset.append(nums[j])
                    chose[j] = True
                    dfs()
                    subset.pop()
                    chose[j] = False
        
        dfs()
        return res
            