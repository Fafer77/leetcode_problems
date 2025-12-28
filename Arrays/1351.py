from typing import List

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        negative_count = 0

        i, j = 0, m - 1
        while i < n and j >= 0:
            if grid[i][j] < 0:
                j -= 1
            else:
                i += 1
                negative_count += (m - 1 - j)
        
        negative_count += (n - i) * (m - max(j, 0))
        
        return negative_count

