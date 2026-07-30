class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        count = 0
        ROW, COL = len(grid), len(grid[0])
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    count += 1
        
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        time = 0
        while q and count > 0:
            for i in range(len(q)):
                
                x, y = q.popleft()
                
                for dx, dy in dirs:
                    newX, newY = x + dx, y + dy

                    if min(newX, newY) < 0 or newX >= ROW or newY >= COL or grid[newX][newY] != 1:
                        continue
                    
                    q.append((newX, newY))
                    grid[newX][newY] = 2
                    count -= 1
            time += 1
                
        return time if count == 0 else -1