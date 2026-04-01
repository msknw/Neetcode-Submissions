class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dp, bottom-up, T/S:O(n*m)
        prevRow = [0] * n
        prevRow[-1] = 1
        for row in range(m-1, -1, -1):
            currRow = [0] * n
            currRow[n-1] = 1
            for col in range(n-2, -1, -1):
                currRow[col] = currRow[col+1] + prevRow[col]
            prevRow = currRow
        return prevRow[0]
        