"""
idea is similar to lognestPalindromicSubstring.
From each starting point (letter) we try extending it to the left and right
considering in one loop even length palindromes and in another odd length ones.
If it is paalindrome we add it.
"""

class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        n = len(s)

        for i in range(n):
            # odd length
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            # even length
            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            
        return res
