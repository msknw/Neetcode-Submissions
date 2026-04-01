class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Time: O(n+m); Space: O(m)
        # 去除了一些重复计算，但感觉还有些可以优化的
        if not t:
            return ""

        tmap = defaultdict(int)

        for c in t:
            tmap[c] += 1

        # 引入required去看这个品种是否齐全
        required = len(tmap)
        formed = 0

        res = [-1, -1]
        resLen = len(s)+1

        l = 0
        n = len(s)

        for r in range(n):
            c = s[r]
            if c in tmap:
                tmap[c] -= 1
                if tmap[c] == 0:
                    formed += 1

            # print(tmap)

            if s[l] not in tmap:
                l += 1

            while formed == required:
                #符合
                if (r-l+1) < resLen:
                    res = [l, r]
                    resLen = r-l+1

                out_c = s[l]
                if tmap[out_c] == 0:
                    # 异变
                    formed -= 1
                tmap[s[l]] += 1
                l += 1

                # 移动到最近的目标字符
                while l < r and s[l] not in tmap:
                    l += 1

        l,r = res[0], res[1]
        return s[l:r+1] if resLen != len(s) + 1 else ""