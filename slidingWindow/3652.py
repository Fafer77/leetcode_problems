from typing import List

class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)
        m = k // 2
        
        starting_sum = sum([prices[i] * strategy[i] for i in range(n)])
        start_window_sum = sum([prices[i] * strategy[i] for i in range(k)])
        new_window_sum = sum([prices[i] for i in range(m, k)])
        curr_delta = new_window_sum - start_window_sum
        max_delta = max(0, curr_delta)

        for r in range(k, n):
            l = r - k
            mid = r - m

            curr_delta += prices[l] * strategy[l]
            curr_delta -= prices[mid]
            curr_delta -= prices[r] * strategy[r]
            curr_delta += prices[r]

            max_delta = max(max_delta, curr_delta)

        return starting_sum + max_delta




