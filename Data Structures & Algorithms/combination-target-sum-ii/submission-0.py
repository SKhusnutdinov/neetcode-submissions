class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        hm = defaultdict(int)
        uniqueCan = []
        res = []
        subset = []

        for cand in candidates:
            if hm[cand] == 0:
                uniqueCan.append(cand)
            hm[cand] += 1

        def dfs(i, curSum):
            if curSum == target:
                res.append(subset.copy())
                return
            if i >= len(uniqueCan) or curSum > target:
                return
            val = uniqueCan[i]
            
            if hm[val]:
                hm[val] -= 1
                subset.append(val)
                dfs(i, curSum + val)
                hm[val] += 1
                subset.pop()
            dfs(i+1, curSum)
        
        dfs(0, 0)
            
        return res