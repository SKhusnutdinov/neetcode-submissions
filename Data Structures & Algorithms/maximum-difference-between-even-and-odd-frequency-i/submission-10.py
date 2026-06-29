class Solution:
    def maxDifference(self, s: str) -> int:
        arr = [0] * 26

        for ch in s:
            arr[ord(ch) - ord('a')] += 1
        
        odd = 0
        even = 100

        for num in arr:
            if num % 2 == 0 and num != 0:
                even = min(even, num)
            else:
                odd = max(odd, num)
        
        print(odd, even)
        return odd - even