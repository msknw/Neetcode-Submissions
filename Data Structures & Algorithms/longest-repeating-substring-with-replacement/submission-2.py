class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0
        
        # 对每一个c都进行这么操作
        charSet = set(s)
        res = 0
        n = len(s)

        for c in charSet:
            err, l = 0, 0
            for r in range(n):
                if s[r] != c:
                    err += 1
                while err > k:
                    if s[l] != c:
                        err -= 1
                    l += 1
                
                res = max(res, r - l + 1)
        
        return res