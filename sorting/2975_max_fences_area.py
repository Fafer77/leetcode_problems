from typing import List

class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        def get_diffs(size, fences):
            coords = sorted(fences + [1, size])
            diffs = set()
            for i in range(len(coords)):
                for j in range(i + 1, len(coords)):
                    diffs.add(coords[j] - coords[i])
            return diffs
        
        h_diffs = get_diffs(m, hFences)
        v_diffs = get_diffs(n, vFences)

        common = h_diffs & v_diffs
        
        if not common:
            return -1

        max_ = max(common)
        return (max_ * max_) % (10**9 + 7)
