class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        subset = []

        def dfs(idx, curSum):
            if curSum == target:
                res.append(subset.copy())
                return
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                if curSum + candidates[i] > target:
                    break
                
                subset.append(candidates[i])
                dfs(i+1, curSum + candidates[i])
                subset.pop()
        
        dfs(0, 0)
        return res