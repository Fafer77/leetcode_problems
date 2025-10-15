'''
Unbounded knapsack where dp[i] - number of combinations that this amount can be created with
We will be iterating over coins and over amounts.
dp[i] = dp[i] + dp[i - coin]
It will be enough because we need to count number of all combinations.
If particular amount can be created using only currently considered coin then it will also be possible
to create i - coin using this coin only. So all possibilites will be included there. We just add extra coin
from all possibilites coin value less.
dp[0] = 1 because we can get 0 amount only in one way - without using any coins
'''

from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0 for _ in range(amount + 1)]
        dp[0] = 1

        for coin in coins:
            for i in range(1, amount + 1):
                if i >= coin:
                    dp[i] += dp[i - coin]
        
        return dp[-1]

