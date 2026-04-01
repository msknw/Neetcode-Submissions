class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # 利用maxf，O(n)

        # windows里面的出现的次数
        counts = defaultdict(int)
        res = 0

        maxf = 0
        l = 0

        for r in range(len(s)):
            counts[s[r]] += 1
            maxf = max(maxf, counts[s[r]])

            while (r-l+1) - maxf > k:
                # counts是要window里的
                counts[s[l]] -= 1
                l += 1

            res = max(res, r-l+1)
        
        return res