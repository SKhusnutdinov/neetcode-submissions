class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROW, COL = len(heights), len(heights[0])
        pac, atl = set(), set()

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(x, y, visit, prevHeight):
            if ((x, y) in visit or
                min(x, y) < 0 or
                x >= ROW or y >= COL or
                heights[x][y] < prevHeight
            ):
                return
            
            visit.add((x, y))
            
            for dx, dy in dirs:
                newX, newY = x + dx, y + dy
                dfs(newX, newY, visit, heights[x][y])
        
        for c in range(COL):
            dfs(0, c, pac, heights[0][c])
            dfs(ROW - 1, c, atl, heights[ROW - 1][c])
        
        for r in range(ROW):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COL - 1, atl, heights[r][COL - 1])
        
        res = []
        for r in range(ROW):
            for c in range(COL):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        
        return res