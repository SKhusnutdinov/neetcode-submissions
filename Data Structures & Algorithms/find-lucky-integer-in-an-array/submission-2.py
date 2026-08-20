class Solution:
    def findLucky(self, arr: List[int]) -> int:
        hm = Counter(arr)
        res = -1

        for key, value in hm.items():
            if key == value:
                res = max(res, key)
        
        return res