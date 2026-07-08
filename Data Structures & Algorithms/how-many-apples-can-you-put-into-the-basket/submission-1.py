class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        weight.sort()

        left = 5000
        for i in range(len(weight)):
            if left - weight[i] < 0:
                return i
            left -= weight[i]
        
        return len(weight)