class Solution:
    def largestGoodInteger(self, num: str) -> str:
        best = -1

        for i in range(1, len(num) - 1):
            if num[i] == num[i-1] and num[i] == num[i+1]:
                if int(num[i]) > best:
                    best = int(num[i])

        return str(best) * 3 if best != -1 else ""