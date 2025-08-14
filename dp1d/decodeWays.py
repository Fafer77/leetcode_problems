class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if s[0] == '0':
            return 0
        elif n == 1:
            return 1
        
        dp = [0 for _ in range(n + 1)]
        
        dp[0] = 1
        if s[0] != '0':
            dp[1] = 1
        else:
            dp[1] = 0

        for i in range(2, n + 1):
            if s[i-1] != '0':
                dp[i] += dp[i-1]
            
            two_digit_val = int(s[i-2:i])
            if 10 <= two_digit_val <= 26:
                dp[i] += dp[i-2]

        return dp[n]
