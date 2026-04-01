class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 优化一下逻辑
        if not prerequisites:
            return True
        
        finished = {}

        # 通过点序列，然后创建邻接表
        # 手动创建graph
        graph = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            graph[crs].append(pre)
    
        def dfs(i):
            if i in finished:
                if finished[i] == False:
                    # 被添加了并且被访问过，looped
                    return False
                elif finished[i] == True:
                    return True
            
            # 加入
            finished[i] = False

            # 天然用for判断其实就可以了，没有就不会进行
            for x in graph[i]:
                result = dfs(x)
                if not result:
                    return False
            # 都true
            finished[i] = True
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False

        return True


                    