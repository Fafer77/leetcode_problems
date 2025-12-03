from typing import List
from collections import defaultdict

class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        y_map = defaultdict(int)
        mod = 10**9 + 7
        res = 0
        total_edges = 0

        for _, y in points:
            y_map[y] += 1

        for p in y_map.values():
            edges = p * (p - 1) // 2
            res += edges * total_edges
            total_edges += edges
        
        return res % mod
