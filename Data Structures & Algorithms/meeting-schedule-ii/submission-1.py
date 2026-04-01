"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # using min heap
        res = 0
        pq = []
        intervals.sort(key = lambda x:x.start)
        for i in range(len(intervals)):
            interval = intervals[i]

            if pq and interval.start >= pq[0]:
                heapq.heappop(pq)
            
            heapq.heappush(pq, interval.end)
            res = max(res, len(pq))
            print(pq, res)
        
        return res
            