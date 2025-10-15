'''
Idea: First as we are given list of words let's hash each word to list of indices where this word occurs.
This will allow us to quickly get access to all locations where particular words are (preprocessing)
Later when we are given 2 words that we want shortest distance between we can iterate using 2 pointers
through these 2 hashed lists and find min distance.
We will be moving pointer which is lower in value as we want pointers to approach each other
to minimize distance not make it bigger
'''

from collections import defaultdict
from typing import List

class WordDistance:
    def __init__(self, words: List[str]):
        self.words_indices = defaultdict(list)
        for idx, word in enumerate(words):
            self.words_indices[word].append(idx)
        
    def shortest(self, word1: str, word2: str) -> int:
        word1_indices = self.words_indices[word1]
        word2_indices = self.words_indices[word2]

        pntr1 = 0
        pntr2 = 0
        res = float('inf')

        while pntr1 < len(word1_indices) and pntr2 < len(word2_indices):
            res = min(res, abs(word1_indices[pntr1] - word2_indices[pntr2]))
            if word1_indices[pntr1] < word2_indices[pntr2]:
                pntr1 += 1
            else:
                pntr2 += 1
        
        return res
