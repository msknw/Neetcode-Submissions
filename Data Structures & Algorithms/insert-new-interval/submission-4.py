class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # binary search + insert

        n = len(intervals)
        target = newInterval[0]
        l, r = 0, n-1

        while l <= r:
            print(l, r)
            mid = (r+l) // 2
            if intervals[mid][0] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        intervals.insert(l, newInterval)

        # merge
        res = [intervals[0]]
        for l, r in intervals:
            lastone = res[-1]
            if l > lastone[1]:
                res.append([l, r])
            else:
                lastone[1] = max(lastone[1], r)
        
        return res

