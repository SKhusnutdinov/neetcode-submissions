"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        time = []
        res = []

        for sched in schedule:
            for inter in sched:
                time.append(inter)
        
        time.sort(key=lambda x: x.start)
        end = time[0].end

        for i in range(1, len(time)):
            if end < time[i].start:
                res.append(Interval(end, time[i].start))
                end = time[i].end
            else:
                end = max(end, time[i].end)


        return res