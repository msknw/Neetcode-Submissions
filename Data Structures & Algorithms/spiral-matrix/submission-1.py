class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])

        left, right, upper, down = 0, n-1, 0, m-1

        res = []
        while True:
            
            for j in range(left, right+1):
                res.append(matrix[upper][j])
            upper += 1
            if upper > down:
                break

            for i in range(upper, down+1):
                res.append(matrix[i][right])
            right -= 1
            if right < left:
                break
            
            for j in range(right, left-1, -1):
                res.append(matrix[down][j])
            down -= 1
            if down < upper:
                break
            
            for i in range(down, upper-1, -1):
                res.append(matrix[i][left])
            left += 1
            if left > right:
                break
        
        return res

            
            