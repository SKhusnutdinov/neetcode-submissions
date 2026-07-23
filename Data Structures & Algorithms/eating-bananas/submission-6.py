class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = l + ((r - l) // 2)
            curH = h

            for pile in piles:
                curH -= math.ceil(pile / k)
            
            if curH >= 0:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res