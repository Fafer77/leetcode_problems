"""
We use backtracking. We put queens in each row and then try putting in different columns.
We check varticals up into considered row and diagonals. If it is good we continue else take a step back.
"""

from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        start_board = [['.' for _ in range(n)] for _ in range(n)]
        res = []

        def backtrack(board, row):
            if row == n:
                solution = ["".join(r) for r in board]
                res.append(solution)
                return

            for i in range(n):
                board[row][i] = 'Q'
                if self.check_vertical(board, row, i) and self.check_diagonal(board, n, row, i):
                    backtrack(board, row + 1)
                board[row][i] = '.'

        backtrack(start_board, 0)
        return res
    
    def check_vertical(self, board, row, col):
        for j in range(row):
            if board[j][col] == 'Q':
                return False
        
        return True

    def check_diagonal(self, board, n, row, col):
        for dx, dy in [(-1, -1), (-1, 1)]:
            new_x, new_y = row, col
            new_x += dx
            new_y += dy

            while 0 <= new_x < row and 0 <= new_y < n:
                if board[new_x][new_y] == 'Q':
                    return False
                new_x += dx
                new_y += dy
        
        return True
