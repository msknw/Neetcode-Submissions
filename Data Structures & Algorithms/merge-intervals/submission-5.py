class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 优化一下写法
        intervals = sorted(intervals, key = lambda x:x[0])

        res = [intervals[0]]
        for l, r in intervals:
            lastone = res[-1]
            if l > lastone[1]:
                res.append([l, r])
            else:
                lastone[1] = max(lastone[1], r)
        return res