from typing import List
from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()
        n = len(grid)
        m = len(grid[0])
        visited = [[False for _ in range(m)] for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    queue.append((i, j))
                    visited[i][j] = True
        
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        level = 0
        level_size = len(queue)

        while queue:
            new_level_size = 0
            for _ in range(level_size):
                i, j = queue.popleft()
                grid[i][j] = level
                
                for dr, dc in directions:
                    nr, nc = i + dr, j + dc
                    if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] != -1 \
                        and grid[nr][nc] != 0 and not visited[nr][nc]:
                        queue.append((nr, nc))
                        visited[nr][nc] = True
                        new_level_size += 1

            level += 1
            level_size = new_level_size

sol = Solution()
sol.islandsAndTreasure([
  [2147483647,-1,0,2147483647],
  [2147483647,2147483647,2147483647,-1],
  [2147483647,-1,2147483647,-1],
  [0,-1,2147483647,2147483647]
])
