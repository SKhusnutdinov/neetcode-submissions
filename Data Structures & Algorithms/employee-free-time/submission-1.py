class Solution(object):
    def employeeFreeTime(self, schedule):
        res = []
        minHeap = [(emp[0].start, empId, 0) for empId, emp in enumerate(schedule)]
        heapq.heapify(minHeap)
        prevEnd = min(emp[0].start for emp in schedule)
        while minHeap:
            start, empId, jobIdx = heapq.heappop(minHeap)
            if prevEnd < start:
                res.append(Interval(prevEnd, start))
            prevEnd = max(prevEnd, schedule[empId][jobIdx].end)
            if jobIdx + 1 < len(schedule[empId]):
                heapq.heappush(minHeap, (schedule[empId][jobIdx+1].start, empId, jobIdx+1))

        return res
