from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        len_longest = len(max(wordDict, key=len))
        word_set = set(wordDict)
        n = len(s)
        dp = [False for _ in range(n + 1)]
        dp[0] = True

        for i in range(1, n + 1):
            start_idx = max(0, i - len_longest)
            for j in range(start_idx, i):
                if dp[j]:
                    search_word = s[j:i]
                    if search_word in word_set:
                        dp[i] = True
                        break
        
        return dp[n]

sol = Solution()
sol.wordBreak('neetcode', ['neet', 'code'])
