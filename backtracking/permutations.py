from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        def backtrack(curr, used):
            if len(curr) == n:
                res.append(curr.copy())
                return
            
            for idx, num in enumerate(nums):
                if not used[idx]:
                    curr.append(num)
                    used[idx] = True
                    backtrack(curr, used)
                    curr.pop()
                    used[idx] = False

        backtrack([], [False] * n)
        return res
    