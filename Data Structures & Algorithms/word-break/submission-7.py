class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # top-down with hash and pruning, T:O((t^2 ∗n)+m), S:O(n+(m∗t))
        memo = {}
        res = False
        wordSet = set(wordDict)

        # 引入一个t剪枝
        t = 0
        for w in wordSet:
            t = max(t, len(w))

        def dfs(i):
            if i in memo:
                return memo[i]
            if i == len(s):
                return True
            
            for j in range(i, min(len(s), i+t)):
                if s[i:j+1] in wordSet:
                    if dfs(j+1):
                        memo[i] = True
                        return True
            
            memo[i] = False
            return False
        
        return dfs(0)
