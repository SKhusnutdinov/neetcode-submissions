class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st = [] # pair (i, height)
        res = 0

        for i, h in enumerate(heights):
            start = i
            while st and st[-1][1] >= h:
                idx, height = st.pop()
                area = (i - idx) * height
                res = max(res, area)
                start = idx

            st.append((start, h))


        for i, h in st:
            area = h * (len(heights) - i)
            res = max(res, area)
        return res