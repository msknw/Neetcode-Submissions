"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        events = []
        for interval in intervals:
            events.append((interval.start, 1))
            events.append((interval.end, -1))
        
        events.sort()

        cnt = 0
        res = 0

        for _, ttype in events:
            cnt += ttype

            res = max(res, cnt)
        
        return res
