class TrieNode:

    def __init__(self):
        self.children = {}
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def addWord(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # 用dfs + Trie
        t = Trie()
        for w in words:
            t.addWord(w)
        
        res, visited = set(), set()

        ROWS, COLS = len(board), len(board[0])
        def dfs(r, c, node, word):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or
            (r,c) in visited or board[r][c] not in node.children):
                return
            
            visited.add((r,c))
            word += board[r][c]
            if node.children[board[r][c]].isWord:
                res.add(word)
            
            node = node.children[board[r][c]]
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r + 1, c, node, word)
            dfs(r, c - 1, node, word)

            visited.remove((r,c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, t.root, "")

        return list(res)

