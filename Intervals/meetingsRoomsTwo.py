"""
Idea: We split each interval into tuple - [time, 1 or -1 depending on whether it is start or end]
Then we sort this list based on first value. We proceed through created list and hold counter.
If we process start tuple then we add +1 to counter meaning there is need for extra day for meeting.
If we process end tuple we subtract 1 from counter meaning that meeting ended and there is place
for a new meeting. We know counter is always >= 0 because end is never before start.

Time complexity: O(nlogn) because of sorting. for loop is O(n) with constant 2
"""

from typing import List

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        timer_list = []
        for interval in intervals:
            timer_list.append((interval.start, 1))
            timer_list.append((interval.end, -1))
        
        cntr = 0
        timer_list.sort()
        res = 0

        for _, act in timer_list:
            if act == 1:
                cntr += 1
            else:
                cntr -= 1  
            res = max(res, cntr)
        
        return res
