class Solution:
    def countLetters(self, s: str) -> int:
        curr = [s[0], 1]

        res = 0
        for ch in s[1:]:
            if ch == curr[0]:
                curr[1] += 1
            else:
                res += (curr[1]*(curr[1]+1)) // 2
                curr[1] = 1
                curr[0] = ch
        
        res += (curr[1]*(curr[1]+1)) // 2
        return res