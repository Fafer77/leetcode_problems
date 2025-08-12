"""
Idea is to use similar approach to houseRobber One.
The difference is that here first and last house are neighbors so we have to keep in mind
whether we robbed first house or not.
So to differentiate it we will divide it into subproblems:
1) first house robbed and then house robber one algorithm (can't rob last house)
2) first house not robbed and then last house robbed
"""

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        # first house robbed
        first, second = nums[0], max(nums[0], nums[1])
        for i in range(2, n - 1):
            temp = second
            second = max(first + nums[i], second)
            first = temp
        
        first_, second_ = 0, nums[1]
        for i in range(2, n):
            temp = second_
            second_ = max(first_ + nums[i], second_)
            first_ = temp
        
        return max(second, second_)
        