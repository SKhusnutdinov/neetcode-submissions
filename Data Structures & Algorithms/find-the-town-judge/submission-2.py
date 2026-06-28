class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        delta = [0] * (n + 1)

        for l in trust:
            a, b = l
            delta[a] -= 1
            delta[b] += 1
            
        for i in range(len(delta)):
            if delta[i] == n - 1:
                return i

        return -1