"""
first we check condition for edges. For n vertices there has to be n - 1 edges.
Then we check whether created graph is connected because tree is connected
"""

from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        adj_list = [[] for _ in range(n)]
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        visited = set()

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for u in adj_list[node]:
                dfs(u)
        
        dfs(0)

        return len(visited) == n
