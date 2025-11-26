class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0:
            return -1
        
        n = 0
        rem = 0
        while True:
            rem = (rem * 10 + 1) % k
            n += 1
            if rem == 0:
                break
        
        return n