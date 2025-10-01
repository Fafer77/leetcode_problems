"""
Idea: Let's create a graph where nodes are words and there exists edge 
between nodes if they differ in 1 character. This will allow us to easily
move between the forms and make allowed moves only.
Then when we have proper graph we want to return minimum steps which will
allow us to go from begin to end word. For this we will use BFS because
it will make sure that the first time we touch endWord will be the quickest
way to get there.
"""

from typing import List
from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words_set = set(wordList)
        words_set.add(beginWord)
        if endWord not in wordList:
            return 0
        
        graph = {}
        for word in words_set:
            graph[word] = []
        
        n = len(beginWord)
        for word in words_set:
            for i in range(n):
                original_char = word[i]
                for ch in range(ord('a'), ord('z') + 1):
                    new_char = chr(ch)
                    if new_char == original_char:
                        continue

                    next_word = word[:i] + new_char + word[i+1:]
                    if next_word in words_set:
                        graph[word].append(next_word)
        
        visited = set()
        queue = deque([(beginWord, 1)])
        visited.add(beginWord)

        while queue:
            word, turn = queue.popleft()
            if word == endWord:
                return turn

            for one_diff_word in graph[word]:
                if one_diff_word not in visited:
                    queue.append((one_diff_word, turn + 1))
                    visited.add(one_diff_word)

        return 0

