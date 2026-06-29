class Solution:
    def mySqrt(self, x: int) -> int:
        
        l = 0
        r = x


        res = 0

        while l <= r:
            mid = (l + r) // 2
            pw = mid * mid

            if pw > x:
                r = mid - 1
            elif pw < x:
                l = mid + 1
                res = mid
            else:
                return mid
        
        return res
            