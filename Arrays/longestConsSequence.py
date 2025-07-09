from typing import List

"""
time complexity O(n)
loop through nums -> O(n)
We get unique set which length is m <= n
In second loop we iterate through each element max 2 times as:
1) if there is num - 1 in unique we do nothing
2) if there isn't num - 1 we go higher as long as we can, so we travel
numbers in set but there will be only one num in set for which we will use while
to iterate other particular numbers
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set()
        for num in nums:
            unique.add(num)
        
        longest_seq = 0

        for num in unique:
            # valid start
            if num - 1 not in unique:
                curr_seq = 1
                curr = num + 1
                while curr in unique:
                    curr_seq += 1
                    curr += 1
                
                if curr_seq > longest_seq:
                    longest_seq = curr_seq
        
        return longest_seq
