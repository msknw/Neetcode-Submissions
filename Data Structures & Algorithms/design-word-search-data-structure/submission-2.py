class TrieNode():
    
    def __init__(self):
        self.children = {}
        self.isword = False

class WordDictionary:
    # T:O(n) for addWord
    # T:O(n) for search
    # S:O(t+n), t is the total number of TrieNodes created in the Trie

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isword = True
    
    def search(self, word: str) -> bool:
        def dfs(j, root):
            curr = root

            for i in range(j, len(word)):
                c = word[i]
                if c == '.':
                    for child in curr.children.values():
                        if dfs(i+1, child):
                            return True
                    return False
                else:
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]
            return curr.isword

        return dfs(0, self.root)






