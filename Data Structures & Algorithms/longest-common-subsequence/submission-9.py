# class Solution:
#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:
#         # dp
#         M,N = len(text1), len(text2)
#         dp = [[0]*(N+1) for _ in range(M+1)]

#         for i in range(M):
#             for j in range(N):
#                 if text1[i] == text2[j]:
#                     dp[i+1][j+1] = 1 + dp[i][j]
#                 else:
#                     dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
        
#         return dp[M][N]

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # dp min space
        M,N = len(text1), len(text2)
        dp = [0]*(N+1)

        for i in range(M):
            curRow = [0]*(N+1)
            for j in range(N):
                if text1[i] == text2[j]:
                    curRow[j+1] = 1 + dp[j]
                else:
                    curRow[j+1] = max(dp[j+1], curRow[j])
            dp = curRow
        return curRow[N]