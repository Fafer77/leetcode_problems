from typing import List
from collections import deque

class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        n = len(nums)
        mod = 10**9 + 7
        dp = [0] * (n + 1)
        prefix = [0] * (n + 1)
        min_q = deque()
        max_q = deque()

        dp[0] = 1
        prefix[0] = 1
        l = 0

        for r in range(n):
            while max_q and nums[max_q[-1]] <= nums[r]:
                max_q.pop()
            max_q.append(r)

            while min_q and nums[min_q[-1]] >= nums[r]:
                min_q.pop()
            min_q.append(r)

            while max_q and min_q and nums[max_q[0]] - nums[min_q[0]] > k:
                if max_q[0] == l:
                    max_q.popleft()
                if min_q[0] == l:
                    min_q.popleft()
                l += 1
            
            if l > 0:
                dp[r + 1] = (prefix[r] - prefix[l - 1] + mod) % mod
            else:
                dp[r + 1] = prefix[r] % mod
            prefix[r + 1] = (prefix[r] + dp[r + 1]) % mod
        
        return dp[n]

