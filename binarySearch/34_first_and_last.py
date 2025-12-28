from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # search lower bound
        l = 0
        r = len(nums) - 1
        low_bound = -1
        while l <= r:
            mid = (l + r) // 2
            curr = nums[mid]
            if curr == target:
                low_bound = mid
                if mid - 1 >= 0 and nums[mid - 1] != target:
                    break
                r = mid - 1
            elif curr < target:
                l = mid + 1
            else:
                r = mid - 1

        if low_bound == -1:
            return [-1, -1]
        
        # search upper bound
        lh = 0
        rh = len(nums) - 1
        high_bound = -1
        while lh <= rh:
            mid = (lh + rh) // 2
            curr = nums[mid]
            if curr == target:
                high_bound = mid
                if mid + 1 < len(nums) and nums[mid + 1] != target:
                    break
                lh = mid + 1
            elif curr < target:
                lh = mid + 1
            else:
                rh = mid - 1
        
        return [low_bound, high_bound]


sol = Solution()
sol.searchRange([1], 1)
