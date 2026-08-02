class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        st = []
        st.append(intervals[0])
        
        for inter in intervals:
            if (inter[0] >= st[-1][0] and inter[0] <= st[-1][1]):
                st[-1][1] = max(st[-1][1], inter[1])
            else:
                st.append(inter)

        return st