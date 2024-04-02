class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    if not self.is_valid(board, i, j):
                        return False
        return True
    
    def is_valid(self, board, row, col):
        target = board[row][col]
        
        # Check row
        for k in range(9):
            if col != k and target == board[row][k]:
                return False
        
        # Check column
        for l in range(9):
            if row != l and target == board[l][col]:
                return False
        
        # Check subgrid
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for m in range(start_row, start_row + 3):
            for n in range(start_col, start_col + 3):
                if row != m and col != n and target == board[m][n]:
                    return False
        
        return True
