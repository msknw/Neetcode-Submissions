"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # 直接sort也可以
        intervals.sort(key = lambda x:x.start)

        for i in range(1, len(intervals)):
            left, right = intervals[i-1], intervals[i]

            if left.end > right.start:
                return False

        return True