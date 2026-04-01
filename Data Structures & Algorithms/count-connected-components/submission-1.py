class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for src, dst in edges:
            graph[src].append(dst)
            graph[dst].append(src)
        
        # 只用visited即可，固定的话array就够了
        visited = [False] * n

        def dfs(i):
            for nei in graph[i]:
                if not visited[nei]:
                    visited[nei] = True
                    dfs(nei)
        
        res = 0
        for i in range(n):
            if not visited[i]:
                visited[i] = True
                dfs(i)
                res += 1

        return res