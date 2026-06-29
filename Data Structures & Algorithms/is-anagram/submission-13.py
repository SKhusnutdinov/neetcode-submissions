class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr = [0] * 26

        for i in range(len(s)):
            arr[ord(s[i]) - ord('a')] += 1
        
        for i in range(len(t)):
            arr[ord(t[i]) - ord('a')] -= 1
        
        for num in arr:
            if num != 0:
                return False
        
        return True