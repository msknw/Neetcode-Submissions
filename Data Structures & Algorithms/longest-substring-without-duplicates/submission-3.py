class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 蛮有意思的，普通的sliding window
        # Time: O(n), Space:O(m)
        if not s:
            return 0

        window = set()
        res = 1
        n = len(s)
        l = 0
        window.add(s[0])

        for r in range(1, n):
            while s[r] in window:
                # 重复
                window.remove(s[l])
                l += 1
            window.add(s[r])
            res = max(res, r - l +1)
        
        return res