class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # 只用额外的两个array, 
        # T:O(m*n), S:O(m+n)
        
        m, n = len(matrix), len(matrix[0])
        
        rowMark = [False] * m
        colMark = [False] * n
        
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    rowMark[r] = True
                    colMark[c] = True
                
        for r in range(m):
            if rowMark[r]:
                for c in range(n):
                    matrix[r][c] = 0
        
        for c in range(n):
            if colMark[c]:
                for r in range(m):
                    matrix[r][c] = 0
        

        