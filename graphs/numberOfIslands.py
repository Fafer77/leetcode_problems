"""
Idea: DFS. First we iterate through each cell (explorer). If it is 1 - increase num of islands,
we dive into it and start DFS looking for 1s (expedition). As we are exploring island we
mark 1s as '#' so that it is visited.
Next when expedition is over we come back to our explorer who iterates to find new 1.
"""

from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    res += 1
                    grid = self.dfs(grid, i, j)
        
        return res

    def dfs(self, map, i, j):
        map[i][j] = '#'
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for dr, dc in directions:
            nr, nc = i + dr, j + dc
            if 0 <= nr < len(map) and 0 <= nc < len(map[0]):
                if map[nr][nc] == '1':
                    map = self.dfs(map, nr, nc)
        
        return map
