from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False for _ in range(n)]
        res = 0

        def dfs(u):
            visited[u] = True
            for v in graph[u]:
                if not visited[v]:
                    dfs(v)
        
        for node in range(n):
            if not visited[node]:
                dfs(node)
                res += 1
        
        return res
