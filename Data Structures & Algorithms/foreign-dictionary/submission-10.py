from collections import defaultdict

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        if not words:
            return ""

        # graph = defaultdict(list)
        graph = { c:[] for w in words for c in w }

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            mlen = min((len(w1), len(w2)))
            if len(w1) > len(w2) and w1[:mlen] == w2[:mlen]:
                return ""

            for k in range(min(len(w1), len(w2))):
                # 找到不一样了
                if w1[k] != w2[k]:
                    if w2[k] not in graph[w1[k]]:
                        graph[w1[k]].append(w2[k])
                    break
        
        print(graph)
        # 图遍历只有pre和post
        # post

        # 还要判定环
        visited = {}
        res = []

        def dfs(c):
            if c in visited:
                return visited[c]
            
            visited[c] = False
            for nei in graph[c]:
                if not dfs(nei):
                    return False
            
            visited[c] = True
            res.append(c)

            return True
        
        for c in graph:
            if not dfs(c):
                return ""

        return "".join(res[::-1])
                        
