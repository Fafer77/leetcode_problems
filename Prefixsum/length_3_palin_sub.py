from collections import Counter

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = set()
        left_set = set()
        hash_map = Counter(s)

        for mid in s:
            hash_map[mid] -= 1
            for letter in left_set:
                if hash_map[letter] > 0:
                    res.add((letter, mid))
            
            left_set.add(mid)

        return len(res)
        