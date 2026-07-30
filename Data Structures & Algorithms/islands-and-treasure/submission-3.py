class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        inf = 2147483647
        
        q = deque()
        ROW, COL = len(grid), len(grid[0])
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 0:
                    q.append((r, c))
        

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        while q:
            x, y = q.popleft()
            
            
            for dx, dy in dirs:
                newX, newY = x + dx, y + dy
                if (
                    min(newX, newY) < 0
                    or newX >= ROW
                    or newY >= COL
                    or grid[newX][newY] != inf
                    ):
                    continue
                grid[newX][newY] = grid[x][y] + 1
                q.append((newX, newY))
            