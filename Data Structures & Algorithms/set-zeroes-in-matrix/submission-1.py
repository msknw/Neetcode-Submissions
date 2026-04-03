class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # 用另一个copy做，这个就相当于是brute force
        # T: O((m*n)*(m+n)); S:O(m*n)
        m, n = len(matrix), len(matrix[0])
        mark = [[matrix[r][c] for c in range(n)] for r in range(m)]

        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    for k in range(n):
                        mark[r][k] = 0
                    for kk in range(m):
                        mark[kk][c] = 0

        for r in range(m):
            for c in range(n):
                matrix[r][c] = mark[r][c]
                
        