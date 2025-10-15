'''
Idea: Think about it in dynamic programming terms.
We have problem but build solution on subproblem when array is smaller.
We add new element but it can't be on its original position, so it can choose n - 1 positions.
2 scenarios:
a) it went on position i and element on position i went to his position (swap). Then element that are left can be chosen for dp(n-2) possibilites
b) it went on position i but this element went on other position then we have to mix n - 1 elements still so dp(n-1)
Therefore dp(n) = (n - 1) * (dp(n - 1) + dp(n - 2))
'''

class Solution:
    def findDerangement(n: int) -> int:
        res = 0
        MOD = 10**9 + 7

        dp = [0 for _ in range(n + 1)]
        dp[0] = 1
        dp[2] = 1
        for i in range(3, n + 1):
            dp[i] = ((i - 1) * (dp[i - 1] + dp[i - 2])) % MOD

        return dp[n]
