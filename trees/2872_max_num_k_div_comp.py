from typing import List

class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        components = 0
        adj_list = [[] for _ in range(n)]
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        def dfs(v, parent):
            nonlocal components
            children_sum = 0
            for u in adj_list[v]:
                if u != parent:
                    children_sum += dfs(u, v)

            subtree_rem = (values[v] + children_sum) % k
            if subtree_rem == 0:
                components += 1
            
            return subtree_rem
        
        dfs(0, -1)
        return components
