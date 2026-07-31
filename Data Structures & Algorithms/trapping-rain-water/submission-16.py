class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        leftMax = 0
        rightMax = 0
        res = 0

        while l < r:
            leftMax = max(leftMax, height[l])
            rightMax = max(rightMax, height[r])

            if leftMax <= rightMax:
                res += (leftMax - height[l])
                l += 1
            else:
                res += (rightMax - height[r])
                r -= 1

        return res