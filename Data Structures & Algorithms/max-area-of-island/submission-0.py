class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(x, y):
            if min(x, y) < 0 or x >= ROWS or y >= COLS or grid[x][y] == 0:
                return 0
            grid[x][y] = 0
            count = 1
            count += dfs(x + 1, y)
            count += dfs(x - 1, y)
            count += dfs(x, y + 1)
            count += dfs(x, y - 1)

            return count
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    res = max(res, dfs(r, c))
            
        return res