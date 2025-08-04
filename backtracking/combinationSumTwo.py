from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(curr, i, target_left):
            if target_left == 0:
                res.append(curr.copy())
                return
            if i >= len(candidates) or target_left < 0:
                return

            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue

                curr.append(candidates[j])
                backtrack(curr, j + 1, target_left - candidates[j])
                curr.pop()

        backtrack([], 0, target)
        return res
