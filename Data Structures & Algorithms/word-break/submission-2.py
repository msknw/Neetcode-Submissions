class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        res = False
        wordSet = set(wordDict)

        def dfs(i):
            if i in memo:
                return memo[i]
            if i > len(s)-1:
                return False
            
            for j in range(i, len(s)):
                if s[i:j+1] in wordSet:
                    if j == len(s)-1:
                        memo[i] = True
                        return True
                    if dfs(j+1):
                        memo[i] = True
                        return True
            
            memo[i] = False
            return False
        
        return dfs(0)
