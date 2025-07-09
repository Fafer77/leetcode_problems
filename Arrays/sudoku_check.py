from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        cols = [list(col) for col in zip(*board)]

        # rows iteration
        for i in range(n):
            seen = set()
            for j in range(n):
                c = board[i][j]
                if c != '.':
                    if c in seen:
                        return False
                    seen.add(c)
        
        # cols iteration
        for i in range(n):
            seen = set()
            for j in range(n):
                c = cols[i][j]
                if c != '.':
                    if c in seen:
                        return False
                    seen.add(c)
        
        # check micro squares
        for r in range(0, n, 3):
            for c in range(0, n, 3):
                seen = set()
                for x in range(3):
                    for y in range(3):
                        i = r + x
                        j = c + y
                        char = board[i][j]
                        if char != '.':
                            if char in seen:
                                return False
                            seen.add(char)
        
        return True
    