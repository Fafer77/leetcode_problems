from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    area = self.dfs(grid, i, j)
                    max_area = max(max_area, area)
        return max_area

    # return 2 values -> updated grid and island size
    def dfs(self, map, i, j):
        map[i][j] = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        local_area = 1

        for dr, dc in directions:
            nr, nc = i + dr, j + dc
            if 0 <= nr < len(map) and 0 <= nc < len(map[0]):
                if map[nr][nc] == 1:
                    area = self.dfs(map, nr, nc)
                    local_area += area
        
        return local_area
