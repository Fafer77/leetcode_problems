'''
Problem: Given string s we want to find length of the longest substring that repeats in s
Idea: We will use dynamic programming and try solving smaller problems and build on them answer for bigger problem.
Compare string s with string s using O(n^2) memory. dp[i][j] - length of repeating substring that ends on i-1 and j-1.
dp[i][j] = dp[i-1][j-1] + 1 if s[i-1]==s[j-1] else 0 (i != j).
If letter on index i == j then we can lengthen substring that was 1 letter shorter.
'''

class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        n = len(s)
        res = 0
        dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(i + 1, n + 1):
                if s[i-1] == s[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    res = max(res, dp[i][j])

        return res
