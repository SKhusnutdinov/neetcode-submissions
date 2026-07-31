class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        matrix = [[] for __ in range(numCourses)]
        indegree = [0] * numCourses
        for nxt, pre in prerequisites:
            indegree[nxt] += 1
            matrix[pre].append(nxt)
        
        res = []

        def dfs(node):
            res.append(node)
            indegree[node] -= 1
            for neigh in matrix[node]:
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    dfs(neigh)
        
        for i in range(numCourses):
            if indegree[i] == 0:
                dfs(i)
        
        return res if len(res) == numCourses else []