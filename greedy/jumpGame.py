"""
Our goal is to reach at least last index.
Idea is to check each time if it is possible to reach particular idx
and if it is we can extend our max_reach further by num on this idx.
If we can't reach that idx then return False
"""

from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        n = len(nums)

        for idx, num in enumerate(nums):
            if idx > max_reach:
                return False
            
            max_reach = max(max_reach, idx + num)

        return max_reach >= n - 1