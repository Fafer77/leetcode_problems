"""
Idea is to check all palindromers starting on each index.
We expand our current palindrome to the left and to the right, but to not check for
palindrome using all letters we consider 2 cases
1) odd length palindrome (centrum consists of 1 letter)
2) even length palindrome (centrum consists of 2 letters)
Thanks to it we can expand both pointers to the left and right as long as
letters are the same
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res_l = 0
        res_r = 0
        n = len(s)
        for i in range(n):
            # odd length case
            l_odd, r_odd = i, i
            while l_odd >= 0 and r_odd < n and s[l_odd] == s[r_odd]:
                if r_odd - l_odd > res_r - res_l:
                    res_l, res_r = l_odd, r_odd
                l_odd -= 1
                r_odd += 1

            # even length case
            l_even, r_even = i, i + 1
            while l_even >= 0 and r_even < n and s[l_even] == s[r_even]:
                if r_even - l_even > res_r - res_l:
                    res_l, res_r = l_even, r_even
                l_even -= 1
                r_even += 1
            
        return s[res_l:res_r + 1]
