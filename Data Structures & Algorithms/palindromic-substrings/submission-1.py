class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        n = len(s)

        def helper(s, l, r):
            res = 0
            while l >= 0 and r < n:
                if s[l] == s[r]:
                    res += 1
                    l -= 1
                    r += 1
                else:
                    break
            
            return res

        for i in range(n):
            res += helper(s, i, i)
            res += helper(s, i, i+1)
            
        return res