class Solution:
    def longestPalindrome(self, s: str) -> str:
        left, right = 0, 0


        for i in range(len(s)):
            l = r = i
            while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
                l -= 1
                r += 1
            r -= 1
            l += 1
            if right - left + 1 < r - l + 1:
                left, right = l, r

            l, r = i, i + 1
            while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
                l -= 1
                r += 1
            l += 1
            r -= 1
            if right - left + 1 < r - l + 1:
                left, right = l, r

        return s[left : right + 1]