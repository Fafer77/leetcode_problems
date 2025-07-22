"""
Idea is to use Floyd Tortoise and Hare algorithm to find cycle and its beginning.
The beginning will be number which is duplicate.
Cycle exists based on task description
"""

from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow_ptr = 0
        fast_ptr = 0

        while True:
            slow_ptr = nums[slow_ptr]
            fast_ptr = nums[nums[fast_ptr]]
            if slow_ptr == fast_ptr:
                break
        
        slow_ptr = 0
        
        while slow_ptr != fast_ptr:
            slow_ptr = nums[slow_ptr]
            fast_ptr = nums[fast_ptr]
        
        return slow_ptr
