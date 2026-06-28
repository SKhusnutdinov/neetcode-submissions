class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        arr = [0] * 26

        for ch in s:
            arr[ord(ch) - ord('a')] += 1
        for ch in t:
            arr[ord(ch) - ord('a')] -= 1
        
        for i in range(len(arr)):
            if arr[i] == -1:
                return chr(i + ord('a'))
