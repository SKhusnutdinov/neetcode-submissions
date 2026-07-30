class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        inf = 2147483647
        
        q = deque()
        ROW, COL = len(grid), len(grid[0])
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 0:
                    q.append((r, c))
        
        dist = 0

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        while q:
            for _ in range(len(q)):
                x, y = q.popleft()
                
                if grid[x][y] == inf:
                    grid[x][y] = dist
                
                for dx, dy in dirs:
                    newX, newY = x + dx, y + dy
                    if min(newX, newY) < 0 or newX >= ROW or newY >= COL or grid[newX][newY] != inf:
                        continue
                    q.append((newX, newY))
                
            dist += 1

        return
                
