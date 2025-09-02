"""
Idea is to think like in a 0/1 knapsack problem. Check if total sum is even otherwise it's False.
dp[i] - is sum i reachable using numbers?
If we answer if dp[target] is reachable it means we can partition.
For each num we iterate from back in order to omit repetitions. If we had started
from beginning then we could use repetition e.g. for 3 we would have dp[3] = True and then
considering dp[6] we would use repetition dp[3].
"""
from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 == 1:
            return False
        
        target = total_sum // 2
        dp = [False for _ in range(target + 1)]
        dp[0] = True

        for num in nums:
            for j in range(target, num - 1, -1):
                dp[j] = (dp[j] or dp[j - num])
        
        return dp[target]

sol = Solution()
sol.canPartition([1,2,3,4])
