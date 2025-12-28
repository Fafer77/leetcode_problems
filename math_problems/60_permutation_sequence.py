from math import ceil

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        if n == 1:
            return "1"
        
        def factorial(m):
            if m == 1 or m == 0:
                return 1
            return m * factorial(m - 1)
        
        res = ""
        curr_k = k
        nums_left = [str(i) for i in range(1, n + 1)]
        while len(nums_left) > 1:
            l = len(nums_left)
            n_sequences = factorial(l)
            seg_len = n_sequences // l
            curr_seg = ceil(curr_k / seg_len)
            num = nums_left.pop(max(curr_seg - 1, 0))
            res += num
            curr_k -= (curr_seg - 1) * seg_len
        
        return res + nums_left.pop(0)


sol = Solution()
print(sol.getPermutation(3, 2))
