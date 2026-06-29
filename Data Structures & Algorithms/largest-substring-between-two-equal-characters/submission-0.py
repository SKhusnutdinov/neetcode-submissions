class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        hm = {}
        diff = -1

        for i in range(len(s)):
            if s[i] in hm:
                diff = max(diff, i - hm[s[i]] - 1)
            else:
                hm[s[i]] = i

        return diff 