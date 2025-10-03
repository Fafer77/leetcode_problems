from typing import List

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        intervals.sort(key=lambda x: x.end)
        last = intervals[0]

        for interval in intervals[1:]:
            if last.end > interval.start:
                return False
            last = interval
        
        return True

