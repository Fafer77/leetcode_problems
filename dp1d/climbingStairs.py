class Solution:
    def climbStairs(self, n: int) -> int:
        self.res = 0

        def dp(curr):
            if curr == n:
                self.res += 1
                return
            elif curr > n:
                return
            
            dp(curr + 1)
            dp(curr + 2)
        
        dp(0)
        return self.res
