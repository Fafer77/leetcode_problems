"""
First we use Trie and add all words into it.
Then we backtrack (DFS) in grid using created Trie.
If we come to the end of word then we add it
We dive deeper into letters if it still continues Trie s tructure 
"""


from typing import List

class TrieNode():
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr_node = self.root
        for letter in word:
            if letter in curr_node.children:
                curr_node = curr_node.children[letter]
            else:
                new_node = TrieNode()
                curr_node.children[letter] = new_node
                curr_node = new_node
        
        curr_node.is_end_of_word = True
        

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = PrefixTree()
        for word in words:
            trie.insert(word)

        res = set()
        n = len(board)
        m = len(board[0])

        def backtrack(row, col, parent_node, visited, curr_word):
            if parent_node.is_end_of_word == True:
                res.add(''.join(curr_word))
            
            for dx, dy in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
                nr = row + dx
                nc = col + dy
                if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc]:
                    char = board[nr][nc]
                    if char in parent_node.children:
                        visited[nr][nc] = True
                        curr_word.append(char)
                        backtrack(nr, nc, parent_node.children[char], visited, curr_word)
                        visited[nr][nc] = False
                        curr_word.pop()

        for i in range(n):
            for j in range(m):
                first_char = board[i][j]
                if first_char in trie.root.children:
                    visited = [[False for _ in range(m)] for _ in range(n)]
                    visited[i][j] = True
                    backtrack(i, j, trie.root.children[first_char], visited, [first_char])
        return list(res)
