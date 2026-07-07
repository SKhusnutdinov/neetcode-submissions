class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        c = 0

        for ch in s:
            if ch == '1':
                c += 1
            
        return "".join(('1' * (c-1)) + (len(s) - c) * '0' + '1')