class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = 0

        for c in set(s):
            left = s.find(c)
            right = s.rfind(c)

            if right - left > 1:
                middle = set(s[left + 1:right])
                res += len(middle)

        return res