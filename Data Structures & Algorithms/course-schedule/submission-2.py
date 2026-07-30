class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            graph[crs].append(pre)
        
        visits = set()

        def dfs(crs):
            if crs in visits:
                return False
            if graph[crs] == []:
                return True
            
            visits.add(crs)

            for pre in graph[crs]:
                if not dfs(pre):
                    return False
            visits.remove(crs)
            graph[crs] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        
        return True