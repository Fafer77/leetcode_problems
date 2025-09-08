"""
Idea is Multi-State BFS. First we iterate through all board and count all fruits + rotten fruits
while adding rotten fruits to queue. These fruits are rotten from minute 0.
We will then perform BFS adding only coordinates where there are healthy fruits and add them to visited.
Each time new fruit is rotten we decrease number of fruits_left and at the end if it is 0 then
we return minute variable else -1
"""
from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fruits_left = 0
        queue = deque()
        n = len(grid)
        m = len(grid[0])
        visited = [[False for _ in range(m)] for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    queue.append((i, j))
                    visited[i][j] = True
                elif grid[i][j] == 1:
                    fruits_left += 1
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        minutes = 0
        level_size = len(queue)
        
        while queue:
            for _ in range(level_size):
                r, c = queue.popleft()
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < n and 0 <= nc < m and not visited[nr][nc] \
                            and grid[nr][nc] == 1):
                        queue.append((nr, nc))
                        visited[nr][nc] = True
                        fruits_left -= 1

            level_size = len(queue)
            minutes += 1
        
        return minutes if fruits_left == 0 else -1

