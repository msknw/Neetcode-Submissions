class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return 
        
        ROWS, COLS = len(heights),  len(heights[0])
        pac, atl = set(), set()
        
        def dfs(r, c, ocean, preh):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or\
             (r,c) in ocean or heights[r][c] < preh:
                return 

            ocean.add((r,c))
            
            dfs(r, c+1, ocean, heights[r][c])
            dfs(r, c-1, ocean, heights[r][c])
            dfs(r+1, c, ocean, heights[r][c])
            dfs(r-1, c, ocean, heights[r][c])

        
        for c in range(COLS):
            dfs(0, c, pac, -1)
            dfs(ROWS-1, c, atl, -1)
        for r in range(ROWS):
            dfs(r, 0, pac, -1)
            dfs(r, COLS-1, atl, -1)

        return [list(coords) for coords in (pac & atl)]
