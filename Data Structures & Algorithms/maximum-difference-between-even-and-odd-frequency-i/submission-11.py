class Solution:
    def maxDifference(self, s: str) -> int:
        hashmap = Counter(s)
        max_odd, min_even = 0, float('inf')
        for el in hashmap:
            if hashmap[el] % 2 == 0:
                min_even = min(min_even, hashmap[el])
            else:
                max_odd = max(max_odd, hashmap[el])
        
        return max_odd - min_even
