"""
Idea: First create directed graph using prerequisites
Second check if there is a cycle in this graph using DFS
O(V + E)
"""

from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            adj_list[b].append(a)
        
        visited = [False for _ in range(numCourses)]
        rec_stack = [False for _ in range(numCourses)]
        for i in range(numCourses):
            if not visited[i] and self.dfs_cycle(i, adj_list, visited, rec_stack):
                return False
        return True

    def dfs_cycle(self, v, graph, visited, rec_stack):
        visited[v] = True
        rec_stack[v] = True
        for u in graph[v]:
            if rec_stack[u]:
                return True
            if not visited[u] and self.dfs_cycle(u, graph, visited, rec_stack):
                return True
        
        rec_stack[v] = False
        return False


