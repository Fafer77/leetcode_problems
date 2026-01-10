class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n = len(s1)
        m = len(s2)
        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        # fill first row (first word empty)
        for i in range(1, m + 1):
            letter = s2[i - 1]
            dp[0][i] = dp[0][i - 1] + ord(letter)
        
        # fill first column (second word empty)
        for i in range(1, n + 1):
            letter = s1[i - 1]
            dp[i][0] = dp[i - 1][0] + ord(letter)
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i-1][j-1] # letters don't need to be deleted
                else:
                    # choose better option which one to delete right now based on previous calculations
                    dp[i][j] = min(dp[i - 1][j] + ord(s1[i - 1]), dp[i][j - 1] + ord(s2[j - 1]))
        
        return dp[-1][-1]
