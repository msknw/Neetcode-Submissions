class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        def dfs(i1, i2):
            if i2 == len(t):
                return 1
            if i1 == len(s):
                return 0

            res = dfs(i1+1, i2)
            if s[i1] == t[i2]:
                res += dfs(i1+1, i2+1)

            return res

        res = dfs(0, 0)
        return res