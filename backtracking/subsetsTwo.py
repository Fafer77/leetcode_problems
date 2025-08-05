from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(curr, i):
            res.append(curr.copy())

            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j-1]:
                    continue

                curr.append(nums[j])
                backtrack(curr, j + 1)
                curr.pop()
        
        backtrack([], 0)
        return res