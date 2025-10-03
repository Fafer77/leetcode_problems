from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = []
        intervals.sort(key=lambda x: x[1])
        res.append(intervals[0])

        for interval in intervals[1:]:
            cs, _ = interval
            if cs >= res[-1][1]:
                res.append(interval)
        
        return len(intervals) - len(res)

sol = Solution()
sol.eraseOverlapIntervals(intervals=[[1,2],[2,4],[1,4]])
