class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROW, COL = len(board), len(board[0])

        def dfs(x, y):
            if (min(x, y) < 0 or
                x >= ROW or y >= COL or
                board[x][y] != 'O'
            ):
                return
            board[x][y] = 'T'

            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)
        
        for c in range(COL):
            if board[0][c] == 'O':
                dfs(0, c)
            if board[ROW - 1][c] == 'O':
                dfs(ROW - 1, c)
        
        for r in range(ROW):
            if board[r][0] == 'O':
                dfs(r, 0)
            if board[r][COL - 1] == 'O':
                dfs(r, COL - 1)
        
        for r in range(ROW):
            for c in range(COL):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'T':
                    board[r][c] = 'O'
        
        return