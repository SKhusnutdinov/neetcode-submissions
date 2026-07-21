class Solution:
    def maxArea(self, heights: List[int]) -> int:
        bestArea = 0
        p1, p2 = 0, len(heights) - 1
        curHeight = 0

        while p1 < p2:
            curHeight = min(heights[p1], heights[p2])
            bestArea = max(bestArea, curHeight * (p2 - p1))

            if heights[p1] > heights[p2]:
                p2 -= 1
            elif heights[p2] > heights[p1]:
                p1 += 1
            else:
                p1 += 1
        
        return bestArea