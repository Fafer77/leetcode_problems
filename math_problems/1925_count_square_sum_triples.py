from math import sqrt

class Solution:
    def countTriples(self, n: int) -> int:
        res = 0
        for i in range(1, n + 1):
            for j in range(i, n + 1):
                number = sqrt(i**2 + j**2)
                if number.is_integer() and number <= n:
                    res += 2
        return res