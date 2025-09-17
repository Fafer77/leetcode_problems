from typing import List
from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = [[] for _ in range(numCourses)]
        dg_in = [0 for _ in range(numCourses)]
        for a, b in prerequisites:
            adj_list[b].append(a)
            dg_in[a] += 1

        res = []
        queue = deque()
        for idx, val in enumerate(dg_in):
            if val == 0:
                queue.append(idx)
        
        while queue:
            course = queue.popleft()
            res.append(course)
            for neighbor in adj_list[course]:
                dg_in[neighbor] -= 1
                if dg_in[neighbor] == 0:
                    queue.append(neighbor)
        
        return res if len(res) == numCourses else []


