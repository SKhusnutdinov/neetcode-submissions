class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS = Counter(s)

        for ch in t:
            countS[ch] -= 1
            if countS[ch] < 0:
                return False
        
        for val in countS.values():
            if val > 0:
                return False
        
        return True