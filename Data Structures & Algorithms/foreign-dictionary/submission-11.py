from collections import deque

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # bfs
        if not words:
            return ""

        # graph = defaultdict(list)
        graph = { c:[] for w in words for c in w }
        indegree = { c:0 for c in graph }

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
                        indegree[w2[k]] += 1
                    break

        
        cnt = 0
        q = deque([c for c in indegree if indegree[c] == 0])
        res = []

        while q:
            poped = q.popleft()
            res.append(poped)
            cnt += 1
            for nei in graph[poped]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        print(cnt, len(graph))

        return "".join(res) if cnt == len(graph) else ""
                        
