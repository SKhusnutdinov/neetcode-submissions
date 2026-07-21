class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        lMax = 0
        rMax = 0
        res = 0

        while l < r:
            lMax = max(lMax, height[l])
            rMax = max(rMax, height[r])
            if lMax <= rMax:
                res += lMax - height[l]
                l += 1
            else:
                res += rMax - height[r]
                r -= 1

        return res