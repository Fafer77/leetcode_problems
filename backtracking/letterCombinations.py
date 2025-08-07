from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        digit_letters_map = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        res = []

        def backtrack(i, curr):
            if i >= len(digits):
                res.append(''.join(curr))
                return

            digit = digits[i]
            for value in digit_letters_map[digit]:
                curr.append(value)
                backtrack(i + 1, curr)
                curr.pop()

        backtrack(0, [])
        return res
