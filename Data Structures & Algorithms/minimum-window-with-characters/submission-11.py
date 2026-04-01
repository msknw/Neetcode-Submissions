class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 优化一下checkWhetherAllMinus的O(m)问题为O(1)
        # Time: O(n+m); Space: O(m)
        # 但还是有一些冗余和重复计算
        tmap = defaultdict(int)

        for c in t:
            tmap[c] += 1

        # 引入required去看这个品种是否齐全
        required = len(tmap)
        formed = 0

        res = s + '0'
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
                res = s[l:r+1] if r-l+1 < len(res) else res

                out_c = s[l]
                if tmap[out_c] == 0:
                    # 异变
                    formed -= 1
                tmap[s[l]] += 1
                l += 1

                # 移动到最近的目标字符
                while l < r and s[l] not in tmap:
                    l += 1
        
        return "" if len(res) > n else res
