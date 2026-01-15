from typing import List

class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        longest_inc_h = 1
        longest_inc_v = 1
        hBars.sort()
        vBars.sort()

        last_bar_h = hBars[0]
        consecutive_h = 1
        for bar in hBars[1:]:
            if bar - 1 == last_bar_h:
                consecutive_h += 1
                longest_inc_h = max(longest_inc_h, consecutive_h)
            else:
                consecutive_h = 1
            last_bar_h = bar
        
        last_bar_v = vBars[0]
        consecutive_v = 1
        for bar in vBars[1:]:
            if bar - 1 == last_bar_v:
                consecutive_v += 1
                longest_inc_v = max(longest_inc_v, consecutive_v)
            else:
                consecutive_v = 1
            last_bar_v = bar
        
        return (min(longest_inc_h, longest_inc_v) + 1) ** 2
