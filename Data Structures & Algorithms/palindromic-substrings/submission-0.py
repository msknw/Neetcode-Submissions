class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        n = len(s)

        for i in range(n):
            l, r = i, i
            while l >= 0 and r < n:
                if s[l] == s[r]:
                    res += 1
                    l -= 1
                    r += 1
                else:
                    break
            
            l,r = i, i+1
            while l >= 0 and r < n:
                if s[l] == s[r]:
                    res += 1
                    l -= 1
                    r += 1
                else:
                    break
        
        return res