class Solution:
    def largestGoodInteger(self, num: str) -> str:
        max = ""
        best = -1

        for i in range(1, len(num) - 1):
            if num[i] == num[i-1] and num[i] == num[i+1]:
                if int(num[i]) > best:
                    max = num[i] * 3
                    best = int(num[i])

        return max
                