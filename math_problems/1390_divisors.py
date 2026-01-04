from typing import List
from math import sqrt

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res += self.check_num_divisors(num)
        
        return res


    def check_num_divisors(self, num):
        if num < 5:
            return 0

        cnt = 2
        sum_ = 1 + num
        for i in range(2, int(sqrt(num)) + 1):
            if num % i == 0:
                if i * i == num:
                    cnt += 1
                    sum_ += i
                else:
                    cnt += 2
                    sum_ += i + num // i

                if cnt > 4:
                    return 0
                
        return sum_ if cnt == 4 else 0
