class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        opn = 0
        res = [''] * len(s)

        for i in range(len(s)):
            if s[i] == ')':
                if opn > 0:
                    opn -= 1
                else:
                    continue
            elif s[i] == '(':
                opn += 1
            res[i] = s[i]
        
        p2 = i
        while opn > 0:
            if res[p2] == '(':
                res[p2] = ''
                opn -= 1
            p2 -= 1

        return "".join(res)