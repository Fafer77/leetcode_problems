"""
Idea: Use dp. Build solution based on smaller parts of arrays. Then build solution based on
previous smaller segments.
"""

from typing import List

class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        m = len(nums2)
        dp = [[float("-inf") for _ in range(m)] for _ in range(n)]
        dp[0][0] = nums1[0] * nums2[0]
        # fill 1st row
        for i in range(1, m):
            curr_product = nums1[0] * nums2[i]
            dp[0][i] = max(dp[0][i - 1], curr_product)
        
        # fill 1st column
        for j in range(1, n):
            curr_product = nums2[0] * nums1[j]
            dp[j][0] = max(dp[j - 1][0], curr_product)
        
        # perform dp inside array
        for i in range(1, n):
            for j in range(1, m):
                curr_product = nums1[i] * nums2[j]
                dp[i][j] = max(curr_product, curr_product + dp[i-1][j-1], 
                               dp[i-1][j], dp[i][j-1])
        
        return dp[-1][-1]
