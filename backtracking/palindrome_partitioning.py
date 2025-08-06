from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        curr = []

        def backtrack(start):
            if start >= len(s):
                res.append(curr.copy())
            
            for i in range(start, len(s)):
                if self.is_palindrome(s, start, i):
                    curr.append(s[start:i+1])
                    backtrack(i + 1)
                    curr.pop()

        backtrack(0)
        return res

    def is_palindrome(self, s, i, j):
        word = s[i:j+1]
        n = len(word)
        for i in range(n // 2):
            if word[i] != word[n - i - 1]:
                return False
        
        return True
