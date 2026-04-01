class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s

        res = ""
        n = len(s)
        i = 0
        while i < n:
            # odd case
            l,r = i, i
            while l >= 0 and r < n:
                if s[l] == s[r]:
                    res = s[l:r+1] if r-l+1 > len(res) else res
                    l -= 1
                    r += 1
                else:
                    break
            
            # even case
            l, r = i, i+1
            while l >= 0 and r < n and s[l] == s[r]:
                res = s[l:r+1] if r-l+1 > len(res) else res
                l -= 1
                r += 1

            i += 1

        return res       