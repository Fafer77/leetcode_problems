"""
Idea: Start from border's 'o' and see how far they reach.
1) in O(n+m) search for 'o' that are on 'frame' of rectangle
2) From each found 'o' perform DFS
Total time complexity: O(n + m + nm)
"""

from typing import List

class Solution:
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def solve(self, board: List[List[str]]) -> None:
        o_locations = []
        n = len(board)
        m = len(board[0])
        visited = [[False for _ in range(m)] for _ in range(n)]

        for i in range(n):
            visited[i][0] = True
            visited[i][m - 1] = True
            if board[i][0] == 'O':
                o_locations.append((i, 0))
            if board[i][m - 1] == 'O':
                o_locations.append((i, m - 1))
        
        for i in range(m):
            visited[0][i] = True
            visited[n - 1][i] = True
            if board[0][i] == 'O':
                o_locations.append((0, i))
            if board[n - 1][i] == 'O':
                o_locations.append((n - 1, i))
        
        for start_o in o_locations:
            self.dfs(start_o, board, visited, n, m)

        for i in range(n):
            for j in range(m):
                if not visited[i][j]:
                    board[i][j] = 'X'

    def dfs(self, o_cords, board, visited, n, m):
        r, c = o_cords
        for dr, dc in self.directions:
            nr, nc = r + dr, c + dc
            if 1 <= nr < n - 1 and 1 <= nc < m - 1 and not visited[nr][nc]:
                visited[nr][nc] = True
                if board[nr][nc] == 'O':
                    self.dfs((nr, nc), board, visited, n, m)

