from typing import List

class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [0, float('-inf'), float('-inf')]
        for num in nums:
            new_dp = dp[:]
            for r in range(3):
                nr = (r + num % 3) % 3
                new_dp[nr] = max(new_dp[nr], dp[r] + num)
            dp = new_dp
        return dp[0]
