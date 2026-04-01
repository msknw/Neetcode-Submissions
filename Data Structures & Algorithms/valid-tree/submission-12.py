from collections import deque

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # bfs, T/S:O(V+E)
        if len(edges) > n-1:
            return False
        
        # 这个相当于连通分量，不需要remove
        visited = set()
        # 更高效的，可以用一个list解决
        graph = [[] for _ in range(n)]
        for src, dst in edges:
            graph[src].append(dst)
            graph[dst].append(src)

        q = deque([(0, -1)])
        visited.add(0)

        while q:
            node, pred = q.popleft()

            for nei in graph[node]:
                if nei == pred:
                    continue
                if nei in visited:
                    return False
                # 开始处理正常节点
                visited.add(nei)
                q.append((nei, node))
        
        return len(visited) == n
            