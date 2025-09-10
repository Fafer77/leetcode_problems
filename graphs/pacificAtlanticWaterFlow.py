"""
Idea: We do it in reverse order. We do two BFS - one from Atlantic and one from Pacific.
We start from ocean so it will be Multi-State BFS from landline. We add to queue if
adjacent coordinate has >= value than the one we are considering (it's reverse order).
We save all these coordinates that can be reached in set.
Then we perform second Multi-State BFS from another ocean and save coordinates to lists.
After it we iterate through list and check in O(1) time if this coordinate is in set from 
first ocean. If there is we add it to answer.

Analogy -> color from 1 ocean that spreads, color from 2nd ocean that spreads
and then we check which are double-colored.
"""

from typing import List
from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        n = len(heights)
        m = len(heights[0])

        queue_pacific = deque()
        queue_atlantic = deque()

        for i in range(m):
            queue_pacific.append([0, i])
            queue_atlantic.append([n - 1, i])
            pacific.add((0, i))
            atlantic.add((n - 1, i))

        for i in range(n):
            queue_pacific.append([i, 0])
            queue_atlantic.append([i, m - 1])
            pacific.add((i, 0))
            atlantic.add((i, m - 1))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue_pacific:
            r, c = queue_pacific.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m and ((nr, nc) not in pacific) \
                        and heights[nr][nc] >= heights[r][c]:
                    queue_pacific.append([nr, nc])
                    pacific.add((nr, nc))
        
        while queue_atlantic:
            r, c = queue_atlantic.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m and ((nr, nc) not in atlantic) \
                        and heights[nr][nc] >= heights[r][c]:
                    queue_atlantic.append([nr, nc])
                    atlantic.add((nr, nc))

        res = atlantic & pacific
        return [[r, c] for r, c in res]
