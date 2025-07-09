from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n

        for i in range(1, n):
            prefix[i] = nums[i - 1] * prefix[i - 1]
        
        for i in range(n - 2, -1, -1):
            suffix[i] = nums[i + 1] * suffix[i + 1]
        
        output = [0] * n

        for i in range(n):
            output[i] = prefix[i] * suffix[i]
        
        return output

sol = Solution()
sol.productExceptSelf([5, 8, 3, 4, 2, 6])
