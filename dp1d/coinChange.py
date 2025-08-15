from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf') for _ in range(amount + 1)]
        dp[0] = 0

        for coin in coins:
            for curr_amount in range(1, amount + 1):
                if curr_amount < coin:
                    dp[curr_amount] = dp[curr_amount]
                else:
                    dp[curr_amount] = min(dp[curr_amount], dp[curr_amount - coin] + 1)
        
        return dp[amount] if dp[amount] != float('inf') else -1
