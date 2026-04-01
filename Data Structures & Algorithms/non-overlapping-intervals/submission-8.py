class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # 二分 + binary search
        intervals.sort(key = lambda x:x[1])

        res = 0
        n = len(intervals)

        def bs(r, target):
            # 找这个>target的第一个，然后再去-1，这样就是max的一个比target小的了
            # [l, r)，最后如果找不到就是0
            l = 0
            while l < r:
                mid = (l+r) >> 1
                if intervals[mid][1] > target:
                    r = mid
                else:
                    l = mid + 1

            return l
            
        print(intervals)
            
        dp = [0] * (n)
        dp[0] = 1
        for i in range(1, n):
            idx = bs(i, intervals[i][0])

            if idx == 0:
                # 没有找到 全部都在start 之后结束，只能skip了
                dp[i] = dp[i-1]
            else:
                dp[i] = max(dp[i-1], 1 + dp[idx-1])

        return n-dp[n-1]