class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        s = [c for c in s]

        p = 0
        print(s)

        for i in range(len(s)):
            if s[i] == '1':
                s[p], s[i] = s[i], s[p]
                p += 1
        s[p - 1], s[len(s) - 1] = s[len(s) - 1], s[p - 1]

        return "".join(s)