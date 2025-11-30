from typing import List


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total_sum = sum(nums)
        rem = total_sum % p
        if rem == 0:
            return 0

        ending_rem = {0: -1}
        curr_prefix_sum = 0
        min_length = len(nums)

        for i, num in enumerate(nums):
            curr_prefix_sum = (curr_prefix_sum + num) % p
            target_rem = (curr_prefix_sum - rem) % p

            if target_rem in ending_rem:
                min_length = min(min_length, i - ending_rem[target_rem])
            
            ending_rem[curr_prefix_sum] = i
        
        return min_length if min_length < len(nums) else -1

