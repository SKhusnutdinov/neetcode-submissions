class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        matrix = [[] for _ in range(len(edges) + 1)]

        def dfs(node, par):
            if visit[node]:
                return True
            
            visit[node] = True
            for neigh in matrix[node]:
                if neigh == par:
                    continue
                if dfs(neigh, node):
                    return True
            return False

        for u, v in edges:
            matrix[u].append(v)
            matrix[v].append(u)
            visit = [False] * (len(edges) + 1)
            if dfs(u, -1):
                return [u, v]
        
        return []