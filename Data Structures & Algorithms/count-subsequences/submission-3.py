class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo = {}

        def dfs(i1, i2):
            if i2 == len(t):
                return 1
            if i1 == len(s):
                return 0
            if (i1, i2) in memo:
                return memo[(i1,i2)]

            res = dfs(i1+1, i2)
            if s[i1] == t[i2]:
                res += dfs(i1+1, i2+1)

            memo[(i1, i2)] = res

            return res

        res = dfs(0, 0)
        return res