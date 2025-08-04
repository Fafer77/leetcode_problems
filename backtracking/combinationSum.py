from typing import List

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(curr, idx, target_left):
            if target_left == 0:
                res.append(curr.copy())
                return
            if idx >= len(nums) or target_left < 0:
                return
            
            # no adding
            num = nums[idx]
            curr.append(num)
            backtrack(curr, idx, target_left - num)
            curr.pop()
            backtrack(curr, idx + 1, target_left)
            

        backtrack([], 0, target)
        return res

    
