from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            mod = num % 3
            res += min(mod, 3 - mod)

        return res
