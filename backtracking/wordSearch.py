from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])
        visited = [[False for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    visited[i][j] = True
                    result = self.backtrack(board, word, visited, i, j, 1)
                    if result:
                        return True
                    visited[i][j] = False
        
        return False
                    
    def backtrack(self, board, word, visited, row, col, word_index):
        if word_index == len(word):
            return True

        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nr, nc = row + dx, col + dy
            if 0 <= nr < len(board) and 0 <= nc < len(board[0]) and not visited[nr][nc]:
                if board[nr][nc] == word[word_index]:
                    visited[nr][nc] = True
                    result = self.backtrack(board, word, visited, nr, nc, word_index + 1)
                    if result:
                        return True
                    visited[nr][nc] = False
        
        return False
    