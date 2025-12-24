from typing import List

class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort() # O(nlogn)
        apples_left = sum(apple)
        boxes_needed = 0

        for c in capacity[::-1]:
            boxes_needed += 1
            apples_left -= c
            if apples_left <= 0:
                break
        
        return boxes_needed

