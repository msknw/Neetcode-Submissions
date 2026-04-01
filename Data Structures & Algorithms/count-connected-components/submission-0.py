class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for src, dst in edges:
            graph[src].append(dst)
            graph[dst].append(src)
        
        cnt = 1
        cluster = {i:0 for i in range(n)}

        def dfs(i, cnt):
            if cluster[i] != 0:
                return False
            
            # 加入
            cluster[i] = cnt

            for x in graph[i]:
                dfs(x, cnt)
            
            # finished
            return True
        
        for i in range(n):
            if dfs(i, cnt):
                cnt += 1

        return cnt-1