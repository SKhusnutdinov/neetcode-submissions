class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        st = []

        for i, h in enumerate(heights):
            start = i
            while st and st[-1][1] > h:
                idx, height = st.pop()
                maxArea = max(maxArea, height * (i - idx))

                start = idx
            st.append((start, h))
        
        for i, h in st:
            maxArea = max(maxArea, h * (len(heights) - i))
        
        return maxArea