class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        hs = set()

        def dfs(res, i):
            if i == len(nums):
                return
            hs.add(tuple(res))
            dfs(res.copy(), i+1)
            res.append(nums[i])
            hs.add(tuple(res))
            dfs(res.copy(), i+1)

            return
        
        dfs([], 0)

        return [list(x) for x in hs]