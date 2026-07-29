class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        hs = set()
        subset = []

        def dfs(i, curSum):
            if curSum == target and tuple(subset) not in hs:
                res.append(subset.copy())
                hs.add(tuple(subset))
                return
            if curSum > target or i >= len(nums):
                return
            
            dfs(i+1, curSum)
            subset.append(nums[i])
            curSum += nums[i]
            dfs(i, curSum)
            dfs(i+1, curSum)
            subset.pop()
            curSum -= nums[i]

            return
        
        dfs(0, 0)
        return res
            