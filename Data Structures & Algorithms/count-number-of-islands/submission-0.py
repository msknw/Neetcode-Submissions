class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cnt = 0
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == '0':
                return 0
            
            grid[r][c] = '0'
            # ==1
            dfs(r, c+1)
            dfs(r+1, c)
            dfs(r, c-1)
            dfs(r-1, c)
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    dfs(r,c)
                    cnt += 1
        
        return cnt