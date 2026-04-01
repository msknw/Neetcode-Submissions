class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 改进的的sliding window：用dict
        # Time: O(n), Space:O(m)
        if not s:
            return 0

        # 最后一次出现的位置
        mp = {}
        res = 1
        n = len(s)
        l = 0

        for r in range(n):
            if s[r] in mp:
                l = max(mp[s[r]]+1, l)
            mp[s[r]] = r
            res = max(res, r - l +1)
        
        return res