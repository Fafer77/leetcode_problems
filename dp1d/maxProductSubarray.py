from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        max_ = 0
        # (local_max, local_min)
        dp = [(0, 0) for _ in range(n)]
        if nums[0] > 0:
            dp[0] = (nums[0], 0)
        else:
            dp[0] = (0, nums[0])
        
        for i in range(1, n):
            num = nums[i]
            prev_max, prev_min = dp[i-1]
            if num > 0:
                local_max = max(prev_max * num, num)
                max_ = max(max_, local_max)
                dp[i] = (local_max, prev_min * num)
            elif num < 0:
                local_max = prev_min * num
                local_min = min(prev_max * num, num)
                max_ = max(max_, local_max)
                dp[i] = (local_max, local_min)
            else:
                dp[i] = (0, 0)
        
        return max_