class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()    

    def addWord(self, word: str) -> None:
        curr_node = self.root
        for letter in word:
            if letter in curr_node.children:
                curr_node = curr_node.children[letter]
            else:
                new_node = TrieNode()
                curr_node.children[letter] = new_node
                curr_node = new_node
        curr_node.is_end_of_word = True

    def search(self, word: str) -> bool:
        def backtrack(node, index):
            if index == len(word):
                return node.is_end_of_word

            char = word[index]

            if char == '.':
                for child in node.children.values():
                    if backtrack(child, index + 1):
                        return True
            elif char in node.children:
                return backtrack(node.children[char], index + 1)
            
            return False
        

        return backtrack(self.root, 0)
            


