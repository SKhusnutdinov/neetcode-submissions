class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        weight.sort()
        allowed = 5000
        for i in range(len(weight)):
            if allowed - weight[i] < 0:
                return i
            allowed -= weight[i]

        return len(weight)