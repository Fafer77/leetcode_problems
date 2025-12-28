from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum_ = sum(nums)
        n = len(nums)
        expected_sum = n * (n + 1) // 2

        return expected_sum - sum_


sol = Solution()
print(sol.missingNumber([0, 3, 1]))
