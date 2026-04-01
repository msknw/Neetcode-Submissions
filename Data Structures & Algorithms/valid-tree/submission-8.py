class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n-1:
            return False
        
        # 这个相当于连通分量，不需要remove
        visited = set()
        # 更高效的，可以用一个list解决
        graph = [[] for _ in range(n)]
        for src, dst in edges:
            graph[src].append(dst)
            graph[dst].append(src)

        def dfs(i, pred):
            # 检测looped
            if i in visited:
                return False

            # 先加
            visited.add(i)
            for nei in graph[i]:
                if nei == pred:
                    continue
                if not dfs(nei, i):
                    return False

            return True
        
        return dfs(0, None) and len(visited) == n
    
            