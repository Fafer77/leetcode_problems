from typing import List
from collections import defaultdict

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        count_map = {}

        for num in nums:
            if num in count_map:
                return num
            count_map[num] = 1

