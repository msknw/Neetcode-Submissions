class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # error
        res = []
        for i in range(len(intervals)):
            l, r = intervals[i]
            newl, newr = newInterval
            if l > newr:
                res.append(newInterval)
                return res + intervals[i:]
            elif r < newl:
                res.append([l, r])
            else:
                # overlapped
                newInterval = [min(l, newl), max(r, newr)]

        res.append(newInterval)
        return res
            