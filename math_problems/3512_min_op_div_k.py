from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        sum_ = 0
        for num in nums:
            sum_ += num
        
        sum_ %= k
        return sum_