class Solution:
    def numDecodings(self, s: str) -> int:
        # dfs
        res = 0
        n = len(s)
        memo = [-1 for _ in range(n)]

        def dfs(i):
            nonlocal res
            if i == n:
                return 1
            if s[i] == '0':
                return 0
            if memo[i] != -1:
                return memo[i]
            
            res = dfs(i+1)
            if i < n -1:
                if (s[i] == '1') or (s[i] == '2' and s[i+1] < '7'):
                    res += dfs(i+2)
            
            memo[i] = res

            return res

        return dfs(0)