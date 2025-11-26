'''
Idea:
too slow (first idea) -> backtracking and counting
better solution: (dynamic programming)
-> in each matrix cell store how many routes with particular reminders exist to get there.
We get value from left or top (because that's how we can travel) and after building dp matrix
check in right bottom corner how many routes with rem 0 exist
'''

from typing import List
from collections import defaultdict

class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                grid[i][j] = grid[i][j] % k
        
        dp = [[defaultdict(int) for _ in range(m)] for _ in range(n)]
        dp[0][0][grid[0][0]] += 1

        for i in range(n):
            for j in range(m):
                curr_num = grid[i][j]
                if i > 0:
                    for x, occurrences in dp[i-1][j].items():
                        new_rem = (x + curr_num) % k
                        dp[i][j][new_rem] += occurrences 
                        dp[i][j][new_rem] = dp[i][j][new_rem] % (10**9 + 7)
                if j > 0:
                    for x, occurences in dp[i][j-1].items():
                        new_rem = (x + curr_num) % k
                        dp[i][j][new_rem] += occurences
                        dp[i][j][new_rem] = dp[i][j][new_rem] % (10**9 + 7)

        return dp[-1][-1].get(0, 0)

sol = Solution()
print(sol.numberOfPaths(grid = [[0]], k = 3))
