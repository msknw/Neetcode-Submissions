class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # memo
        cache = [[-1]*len(text2) for _ in range(len(text1))]

        def memodfs(i1, i2, cache):
            if i1 == len(text1) or i2 == len(text2):
                return 0
            
            if cache[i1][i2] != -1:
                return cache[i1][i2]
            
            if text1[i1] == text2[i2]:
                cache[i1][i2] = 1+memodfs(i1+1, i2+1, cache)
            else:
                cache[i1][i2] = max(memodfs(i1, i2+1, cache), memodfs(i1+1, i2, cache))

            return cache[i1][i2]
            
        return memodfs(0, 0, cache)