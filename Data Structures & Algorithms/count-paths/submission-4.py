from functools import cache

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dfs-dp top-down memorize, T/S: O(n*m)
        # @cache
        # cache = [[0]*n for _ in range(m)]
        def dfs(r, c):
            if r == m or c == n:
                return 0
            # if cache[r][c] != 0:
            #     return cache[r][c]
            if r == m - 1 and c == n - 1:
                return 1

            cache = (dfs(r+1, c) + dfs(r, c+1))
            return cache

        
        return dfs(0, 0)