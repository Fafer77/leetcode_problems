from typing import List

class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        res = 0
        total_sum = sum(nums)
        prefix_sum = 0
        for num in nums[:-1]:
            prefix_sum += num
            if abs(prefix_sum - (total_sum - prefix_sum)) % 2 == 0:
                res += 1
        
        return res
