from typing import List

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        max_happiness = 0

        for i in range(k):
            max_happiness += max(happiness[i] - i, 0)
        
        return max_happiness
