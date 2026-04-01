class PrefixTreeNode:

    def __init__(self):
        self.children = {}
        self.isword = False

class PrefixTree:

    def __init__(self):
        self.root = PrefixTreeNode()
        

    def insert(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = PrefixTreeNode()
            curr = curr.children[c]
        curr.isword = True


    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.isword

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True
        