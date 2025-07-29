from typing import List
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)

            if x < y:
                y = x - y
                heapq.heappush(stones, y)
            
        if len(stones) == 1:
            return -heapq.heappop(stones)
        else:
            return 0


sol = Solution()
sol.lastStoneWeight([2, 3, 6, 2, 4])
