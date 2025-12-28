from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n
        nums[:] = nums[-k:] + nums[:-k]

sol = Solution()
sol.rotate([1, 2, 3, 4, 5, 6, 7], 3)
