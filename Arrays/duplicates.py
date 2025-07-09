from typing import List
from collections import defaultdict

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = defaultdict(int)

        for num in nums:
            freq[num] += 1
        
        for _, val in freq.items():
            if val > 1:
                return True
        
        return False
