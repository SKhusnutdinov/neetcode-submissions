class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = {i : [] for i in range(n)}
        for start, dest in edges:
            graph[start].append(dest)
            graph[dest].append(start)

        visit = set()

        def dfs(node, par):
            if node in visit:
                return False

            visit.add(node)
            for neigh in graph[node]:
                if neigh == par:
                    continue
                if not dfs(neigh, node):
                    return False
            return True
        
        return dfs(0, -1) and len(visit) == n
            
