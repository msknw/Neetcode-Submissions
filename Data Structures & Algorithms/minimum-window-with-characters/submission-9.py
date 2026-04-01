class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Time: O(n*m); Space: O(m)

        tmap = defaultdict(int)

        for c in t:
            tmap[c] += 1
        
        res = s + '0'
        l = 0
        n = len(s)

        for r in range(n):
            c = s[r]
            if c in tmap:
                tmap[c] -= 1

            # print(tmap)

            if s[l] not in tmap:
                l += 1

            while self.checkWhetherAllMinus(tmap.values()):
                print('inside', tmap)
                #符合
                res = s[l:r+1] if r-l+1 < len(res) else res

                tmap[s[l]] += 1
                l += 1

                # 移动到最近的目标字符
                while l < r and s[l] not in tmap:
                    l += 1
        
        return "" if len(res) > n else res

    def checkWhetherAllMinus(self, values):
        for num in values:
            if num > 0:
                return False
        
        return True