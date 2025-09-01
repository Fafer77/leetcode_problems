from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [float('inf') for _ in range(n + 1)]
        dp[0] = float('-inf')

        for i, num in enumerate(nums):
            to_put_idx = self.bin_search(i, dp, num)
            dp[to_put_idx] = num
        
        for idx, val in enumerate(dp):
            if val == float('inf'):
                return idx - 1
        
        return n

    def bin_search(self, right, dp, num):
        l, r = 1, right + 1
        while l < r:
            mid = l + (r - l) // 2
            if num > dp[mid]:
                l = mid + 1
            else:
                r = mid
        
        return l
