class TicTacToe:

    def __init__(self, n: int):
        self.rows = [0] * n
        self.columns = [0] * n
        self.diagonal = 0
        self.antiDiagonal = 0

    def move(self, row: int, col: int, player: int) -> int:
        change = 1 if player == 1 else -1

        self.rows[row] += change
        self.columns[col] += change

        if row == col:
            self.diagonal += change
        
        if col == (len(self.columns) - row - 1):
            self.antiDiagonal += change
        
        n = len(self.rows)

        if (abs(self.rows[row]) == n or
            abs(self.columns[col]) == n or
            abs(self.diagonal) == n or
            abs(self.antiDiagonal) == n):
            return player
        
        return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
