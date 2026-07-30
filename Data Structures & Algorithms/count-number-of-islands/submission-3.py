class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        ROW, COL = len(grid), len(grid[0])

        def dfs(x, y):
            if min(x, y) < 0 or x >= ROW or y >= COL or grid[x][y] == '0':
                return

            grid[x][y] = '0'
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)
        
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == '1':
                    dfs(r, c)
                    res += 1
        
        return res