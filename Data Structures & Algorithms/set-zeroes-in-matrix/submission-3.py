class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # T:O(m*n), S:O(1)， inplace的旋转
        rowZero = 1

        m, n = len(matrix), len(matrix[0])
        
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0

                    if r > 0:
                        matrix[r][0] = 0
                    elif r == 0:
                        rowZero = 0
        
        for r in range(1, m):
            for c in range(1, n):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0


        # first col
        if matrix[0][0] == 0:
            for r in range(1, m):
                matrix[r][0] = 0
        
        # first row
        if rowZero == 0:
            for c in range(n):
                matrix[0][c] = 0
        
        