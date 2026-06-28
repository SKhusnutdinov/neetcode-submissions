class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        inarr = [0] * (n + 1)
        outarr = [0] * (n + 1)

        for l in trust:
            a, b = l
            outarr[a] += 1
            inarr[b] += 1
            
        for i in range(len(inarr)):
            if inarr[i] == n - 1 and outarr[i] == 0:
                return i

        return -1