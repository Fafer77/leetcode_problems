"""
Idea: In order to calculate median we have to be able to store data somehow in sorted fashion.
We can't use bin search because we find place for num in O(logn) but to the move it all it will
take maximum O(n).
So instead we will split our array into 2 heaps. First heap will store first sorted half
and second heap second sorted half. We need to have easy access to 2 middle elements
so one heap will be max and another min.
Find is easy just using definition and accessing apropriate elements.
"""

import heapq

class MedianFinder:
    def __init__(self):
        self.first_half = []
        self.second_half = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.first_half, -num)

        if self.first_half and self.second_half and (-self.first_half[0] > self.second_half[0]):
            to_move = -heapq.heappop(self.first_half)
            heapq.heappush(self.second_half, to_move)

        if len(self.first_half) > len(self.second_half) + 1:
            to_move = -heapq.heappop(self.first_half)
            heapq.heappush(self.second_half, to_move)
        elif len(self.second_half) > len(self.first_half):
            to_move = heapq.heappop(self.second_half)
            heapq.heappush(self.first_half, -to_move)


    def findMedian(self) -> float:
        if (len(self.first_half) + len(self.second_half)) % 2 == 0:
            return (-self.first_half[0] + self.second_half[0]) / 2
        else:
            return (-self.first_half[0])
