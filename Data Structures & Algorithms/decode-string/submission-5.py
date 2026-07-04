class Solution:
    def decodeString(self, s: str) -> str:
        stS = []
        stC = []

        cur = ""
        k = 0

        for ch in s:
            if ch.isdigit():
                k = k * 10 + int(ch)
            elif ch == '[':
                stC.append(k)
                stS.append(cur)
                cur = ""
                k = 0
            elif ch == ']':
                temp = cur
                cur = stS.pop()
                count = stC.pop()
                cur += temp * count
            
            else:
                cur += ch
    
        return cur