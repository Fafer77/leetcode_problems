"""
time complexity O(log(min(n,m))), memory: O(1)
We need to split it so that altogether on the left partition there are half of total number
of elements. It is enough to just use bin search on smaller array as we know how many elements
we need to take from longer one to get half of total altogether.
Size of left partition is good for median but then we have to compare whether there really is median
as in one array there might be all elements bigger than in another one. So we compare with end of left
partition in both arrays with opposite array next values. If they are lower it is good.
Else we need to bin_search on smaller array based on where there are higher values.
Consider cases for even total and odd.
"""

from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A = nums1
        B = nums2
        if len(A) > len(B):
            A, B = B, A
        
        total = len(A) + len(B)
        half = total // 2
        l = 0
        r = len(A) - 1
        while True:
            midA = (l + r) // 2
            segmentB = half - midA - 2 # -2 as both are 0-indexed
            Aleft = A[midA] if midA >= 0 else float('-inf')
            Aright = A[midA + 1] if midA + 1 < len(A) else float('inf')
            Bleft = B[segmentB] if segmentB >= 0 else float('-inf')
            Bright = B[segmentB + 1] if segmentB + 1 < len(B) else float('inf')

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright)
                return (max(Bleft, Aleft) + min(Bright, Aright)) / 2
            elif Aleft > Bright:
                r = midA - 1
            else:
                l = midA + 1