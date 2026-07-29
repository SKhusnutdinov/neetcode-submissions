class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        hs = set()
        ROW = len(board)
        COL = len(board[0])
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        
        def dfs(r, c, i):
            if i == len(word):
                return True
                
            if (min(r, c) < 0 or r >= ROW or c >= COL or word[i] != board[r][c] or (r, c) in hs):
                return False
            
            
            hs.add((r, c))
            for dx, dy in dirs:
                newC = c + dx
                newR = r + dy
                if dfs(newR, newC, i+1):
                    return True
            hs.remove((r, c))
            return False
        
        for r in range(ROW):
            for c in range(COL):
                if dfs(r, c, 0):
                    return True
        return False