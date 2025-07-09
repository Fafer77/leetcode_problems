from typing import List
from collections import defaultdict

# store indices instead of strings to decrease memory 
# usage to O(m), where m is number of strings

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = defaultdict(list)

        for s in strs:
            letters_count = [0] * 26
        
            for c in s:
                letters_count[ord(c) - ord('a')] += 1
        
            freq[tuple(letters_count)].append(s)
        
        return freq.values()


sol = Solution()
print(sol.groupAnagrams(["act","pots","tops","cat","stop","hat"]))      
