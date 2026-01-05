"""
idea: if we have even number of (-) then we can cancel all minuses out as they can travel
as we want them to do (all pairs will get canceled)
On the other hand if there is odd number of (-) then we can't cancel everything out. There will 
be 1 (-) left. Our goal in this situation is to choose the smallest number that will be negative
"""

from typing import List

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        abs_total = 0
        neg_count = 0
        min_ = float('inf')

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                num = abs(matrix[i][j])
                abs_total += num
                min_ = min(min_, num)

                if matrix[i][j] < 0:
                    neg_count += 1

        return abs_total - 2 * min_ if neg_count % 2 else abs_total
