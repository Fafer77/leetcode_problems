from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        res.append(intervals[0])

        for interval in intervals[1:]:
            start, end = res[-1]
            cs, ce = interval
            if start <= cs <= end:
                res[-1][1] = max(end, ce)
            else:
                res.append(interval)
        
        return res
