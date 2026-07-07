class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for row in range(len(board)):
            for col in range(len(board)):
                val = board[row][col]
                if not val.isnumeric():
                    continue
                if val in rows[row]:
                    return False
                rows[row].add(val)

                if val in cols[col]:
                    return False
                cols[col].add(val)

                sx = row // 3
                sy = col // 3

                if val in squares[(sx, sy)]:
                    return False
                
                squares[(sx, sy)].add(val)
        
        return True