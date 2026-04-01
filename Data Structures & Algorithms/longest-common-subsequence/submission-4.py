from functools import cache


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # dfs

        @cache
        def dfs(s1, s2, i1, i2):
            if i1 == len(text1) or i2 == len(text2):
                return 0

            if s1[i1] == s2[i2]:
                return 1+dfs(s1,s2, i1+1, i2+1)
            else:
                return max(dfs(s1,s2,i1+1, i2), dfs(s1, s2, i1, i2+1))
        
        return dfs(text1, text2, 0, 0)