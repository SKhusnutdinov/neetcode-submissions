class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]

        for i in range(1, len(intervals)):
            start, end = res[-1]
            st, ed = intervals[i]
            if end >= st:
                res.pop()
                res.append([start, max(end, ed)])
            else:
                res.append(intervals[i])
        
        return res