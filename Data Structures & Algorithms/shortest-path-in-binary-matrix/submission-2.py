class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        if grid[0][0] == 1 or grid[ROWS - 1][COLS - 1] == 1:
            return -1

        q = deque()
        q.append((0, 0))
        grid[0][0] = 1


        path = 1

        while q:
            for i in range(len(q)):
                x, y = q.popleft()
                if x == ROWS - 1 and y == COLS - 1:
                    return path
                
                dirs = [(
                    1, 0),
                    (-1, 0),
                    (0, 1),
                    (0, -1),
                    (1, 1),
                    (-1, -1),
                    (-1, 1),
                    (1, -1)
                    ]
                for dx, dy in dirs:
                    if min((x + dx), (y + dy)) < 0 or (x + dx) >= ROWS or (y + dy) >= COLS or grid[x + dx][y + dy] == 1:
                        continue
                    q.append((x + dx, y + dy))
                    grid[x][y] = 1
            path += 1

        return -1
                