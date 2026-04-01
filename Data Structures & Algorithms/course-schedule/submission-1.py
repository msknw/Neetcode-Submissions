from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        
        finished = {}

        # 通过点序列，然后创建邻接表
        graph = defaultdict(list)
        for pair in prerequisites:
            graph[pair[0]].append(pair[1])
    
        def dfs(i):
            if i in finished:
                if finished[i] == False:
                    # 被添加了并且被访问过，looped
                    return False
                elif finished[i] == True:
                    return True
            
            # 加入
            finished[i] = False

            if not graph[i]:
                # 结束
                finished[i] = True
                return True
            else:
                # 还有，一个个递归
                for x in graph[i]:
                    result = dfs(x)
                    if not result:
                        return False
                # 都true
                finished[i] = True
                return True
        
        for course in list(graph.keys()):
            if not dfs(course):
                return False

        return True


                    