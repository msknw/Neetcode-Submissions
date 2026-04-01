class PrefixTreeNode:
    # 限定26个字母

    def __init__(self):
        self.children = [None] * 26
        self.isword = False

class PrefixTree:

    def __init__(self):
        self.root = PrefixTreeNode()
        

    def insert(self, word: str) -> None:
        curr = self.root

        for c in word:
            i = ord(c) - ord('a')
            if not curr.children[i]:
                curr.children[i] = PrefixTreeNode()
            curr = curr.children[i]
        curr.isword = True


    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            i = ord(c) - ord('a')
            if not curr.children[i]:
                return False
            curr = curr.children[i]
        return curr.isword

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            i = ord(c) - ord('a')
            if not curr.children[i]:
                return False
            curr = curr.children[i]
        return True
        