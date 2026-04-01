class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        self.existed = False

        path = ""
        ROWS, COLS = len(board), len(board[0])
        def dfs(r, c, board, path):
            if (r < 0 or r >= ROWS or c < 0 or c >= COLS or
                (r,c) in visited or board[r][c] not in word):
                return
            
            visited.add((r,c))

            path += board[r][c]

            if path == word or self.existed:
                self.existed = True
                return

            dfs(r, c+1, board, path)
            dfs(r+1, c, board, path)
            dfs(r, c-1, board, path)
            dfs(r-1, c, board, path)
            
            visited.remove((r,c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c,board,path)
                if self.existed:
                    return True
        
        return self.existed