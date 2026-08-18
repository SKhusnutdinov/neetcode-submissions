"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        res = []
        heap = [(emp[0].start, empId, 0) for empId, emp in enumerate(schedule)]
        heapq.heapify(heap)

        prevEnd = min(emp[0].start for emp in schedule)

        while heap:
            start, empId, jobIdx = heapq.heappop(heap)

            if prevEnd < start:
                res.append(Interval(prevEnd, start))
            prevEnd = max(prevEnd, schedule[empId][jobIdx].end)
            
            if jobIdx + 1 < len(schedule[empId]):
                heapq.heappush(heap, (schedule[empId][jobIdx + 1].start , empId, jobIdx + 1))
        
        return res
        