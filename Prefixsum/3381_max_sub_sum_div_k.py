from typing import List

class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        min_prefix_sum_mod_k = [float('inf') for _ in range(k)]
        min_prefix_sum_mod_k[0] = 0
        max_subarray_sum_div_k = float('-inf')
        curr_prefix_sum = 0
        
        for idx, num in enumerate(nums):
            curr_prefix_sum += num
            r = (idx + 1) % k
            subarray_sum = curr_prefix_sum - min_prefix_sum_mod_k[r]
            max_subarray_sum_div_k = max(max_subarray_sum_div_k, subarray_sum)
            min_prefix_sum_mod_k[r] = min(min_prefix_sum_mod_k[r], curr_prefix_sum)
        
        return max_subarray_sum_div_k
