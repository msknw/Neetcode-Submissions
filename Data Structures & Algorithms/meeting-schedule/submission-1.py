"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        events = []
        for interval in intervals:
            events.append((interval.start, 1))
            events.append((interval.end, -1))
        
        events.sort()

        cnt = 0

        for time, ttype in events:
            cnt += ttype

            if cnt > 1:
                return False
        
        return True

