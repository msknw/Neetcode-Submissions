class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sorted
        intervals = sorted(intervals, key = lambda x:x[0])
        l, r = intervals[0]

        res = []
        for i in range(1, len(intervals)):
            newl, newr = intervals[i]
            if newl > r:
                res.append([l, r])
                l, r = newl, newr
            else:
                l = min(l, newl)
                r = max(r, newr)
                # res.append([l, r])
        res.append([l, r])
        return res