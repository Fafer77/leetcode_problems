from typing import List
from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = {}
        for i in range(0, len(nums)):
            curr = nums[i]
            needed = target - curr

            if needed in numbers:
                return [numbers[needed], i]

            if nums[i] not in numbers:
                numbers[nums[i]] = i

        return []
    

sol = Solution()
print(sol.twoSum([4,5,6], 10))
