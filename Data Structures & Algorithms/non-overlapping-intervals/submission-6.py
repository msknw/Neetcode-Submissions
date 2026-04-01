class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        #dfs
        intervals.sort()
        n = len(intervals)

        def dfs(i, prev):
            if i == n:
                return 0
            
            res = dfs(i+1, prev)
            if prev == -1 or intervals[prev][1] <= intervals[i][0]:
                res = max(res, 1 + dfs(i+1, i))
            
            return res
        
        return len(intervals) - dfs(0, -1)