from typing import List

class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        nums = [str(num) for num in nums]
        n = len(nums)
        res = [False for _ in range(n)]
        for i in range(n):
            bin_num = ''.join(nums[:i+1])
            print(bin_num)
            print(type(bin_num))
            if (int(bin_num, 2) % 5 == 0):
                res[i] = True
        
        return res

sol = Solution()
sol.prefixesDivBy5([1, 0, 1])
