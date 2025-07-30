from typing import List
import heapq
from collections import deque, Counter

# queue state (freq, letter, time_when_can_come_back)

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        queue = deque()
        max_heap = []
        freq_list = Counter(tasks)

        for char, freq in freq_list.items():
            heapq.heappush(max_heap, (-freq, char))

        time = 0

        while queue or max_heap:
            while queue and queue[0][2] <= time:
                new_freq, letter, _ = queue.popleft()
                heapq.heappush(max_heap, (new_freq, letter))
            
            if max_heap:
                freq, letter = heapq.heappop(max_heap)
                freq += 1
                
                if freq < 0:
                    queue.append((freq, letter, time + n + 1))
            
            time += 1
        
        return time