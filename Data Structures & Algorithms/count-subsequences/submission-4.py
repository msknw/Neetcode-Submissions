class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # dp
        M, N = len(s), len(t)
        dp = [ [0]*(N+1) for _ in range(M+1)]

        for i in range(M+1):
            dp[i][N] = 1

        for i in range(M-1, -1, -1):
            for j in range(N-1, -1, -1):
                dp[i][j] = dp[i+1][j]
                if t[j] == s[i]:
                    dp[i][j] += dp[i+1][j+1]

        return dp[0][0]