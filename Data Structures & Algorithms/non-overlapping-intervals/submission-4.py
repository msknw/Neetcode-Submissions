class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # 试试取消小的
        intervals.sort()

        res = 0
        lastl, lastr = intervals[0]
        n = len(intervals)

        print(intervals)

        for i in range(1, n):
            l, r = intervals[i]
            if l < lastr:
                # overlapped
                res += 1
                lastr = min(r, lastr)
            else:
                lastl, lastr = l, r

        return res