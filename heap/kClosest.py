from typing import List
from math import sqrt
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        res = []

        for p in points:
            dist = sqrt(p[0]**2 + p[1]**2)
            heapq.heappush(maxHeap, (-dist, p))
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        
        while maxHeap:
            _, p = heapq.heappop(maxHeap)
            res.append(p)

        return res
