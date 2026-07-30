class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        hs = set()
        res = 0
        ROW, COL = len(grid), len(grid[0])

        def dfs(x, y):
            if (x, y) in hs or min(x, y) < 0 or x >= ROW or y >= COL or grid[x][y] == '0':
                return 0

            hs.add((x, y))
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)
            
            return 1
        
        for r in range(ROW):
            for c in range(COL):
                res += dfs(r, c)
        
        return res