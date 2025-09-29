from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        res = None
        n = len(edges) + 1

        parent = [i for i in range(n)]
        size = [1] * n

        for u, v in edges:
            if not self.union(u, v, size, parent):
                res = [u, v]

        return res


    def union(self, u, v, size, parent):
        rootU = self.find(u, parent)
        rootV = self.find(v, parent)
        if rootU == rootV:
            return False
        
        if size[rootU] < size[rootV]:
            rootU, rootV = rootV, rootU
        
        parent[rootV] = rootU
        size[rootU] += size[rootV]
        return True


    def find(self, u, parent):
        if parent[u] == u:
            return u
        
        parent[u] = self.find(parent[u], parent)
        return parent[u]
