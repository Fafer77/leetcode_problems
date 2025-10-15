'''
Idea: We need to be able to find smallest distance between 2 given words in a list.
We will use 2 pointers and start from the beginning. We move both of them and save last
location where each word was seen. In each iteration we check whether we have new minimum distance
'''
from typing import List


class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        pntr1 = -1
        pntr2 = -1
        res = float('inf')

        for idx, word in enumerate(words):
            if word == word1:
                pntr1 = idx
            if word == word2:
                pntr2 = idx
            if pntr1 != -1 and pntr2 != -1:
                res = min(res, abs(pntr1 - pntr2))
        
        return res

