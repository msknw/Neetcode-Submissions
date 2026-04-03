class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
    
        def helper(start, end, matrix):
            # [start, end]
            for i in range(end-start):
                uleft, uright = matrix[start][start+i], matrix[start+i][end]
                dright, dleft = matrix[end][end-i], matrix[end-i][start]
                matrix[start][start+i] = dleft
                matrix[start+i][end] = uleft
                matrix[end][end-i] = uright
                matrix[end-i][start] = dright

        n = len(matrix)
        for i in range(n//2):
            helper(i, n-i-1, matrix)

        # print(matrix)
        # return matrix