class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        visited = set()

        idxes = {c:[] for c in s}
        for i, c in enumerate(s):
            idxes[c].append(i)
        
        def dfs(i1, i2):
            if i2 == len(t):
                return 1
            
            # visited.add(i1)
            c = t[i2]
            if c not in idxes:
                return 0
            subidxes = idxes[c]
            
            res = 0
            for subidx in subidxes:
                if subidx > i1:
                    res += dfs(subidx, i2+1)
            
            # visited.remove(i1)

            return res

        res = dfs(-1, 0)
        return res