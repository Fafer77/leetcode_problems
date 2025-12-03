from typing import List

class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        batteries.sort()
        additional_power = sum(batteries[:-n])
        running = batteries[-n:]

        for i in range(n - 1):
            if additional_power // (i + 1) < running[i + 1] - running[i]:
                return running[i] + additional_power // (i + 1)
            
            additional_power -= (i + 1) * (running[i + 1] - running[i])
        
        return running[-1] + additional_power // n
