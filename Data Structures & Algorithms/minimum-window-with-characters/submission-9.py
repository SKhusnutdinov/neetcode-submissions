class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        idx = -1
        ln = float("inf")
        
        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        
        have, need = 0, len(countT)

        l = 0

        for r in range(len(s)):
            charR = s[r]

            window[charR] = 1 + window.get(charR, 0)

            if charR in countT and window[charR] == countT[charR]:
                have += 1
            
            if have == need and r - l + 1 < ln:
                idx = l
                ln = r - l + 1
            
            while have == need:
                print("Debug: " + s[idx:idx + ln])
                if r - l + 1 < ln:
                    idx = l
                    ln = r - l + 1
                charL = s[l]

                window[charL] -= 1

                if charL in countT and window[charL] < countT[charL]:
                    have -= 1
                
                l += 1


        
        return s[idx:idx + ln] if idx >= 0 else ""
            