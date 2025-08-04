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

    def search(self, word: str) -> bool:
        curr_node = self.root
        for letter in word:
            if letter not in curr_node.children:
                return False
            curr_node = curr_node.children[letter]
        
        return curr_node.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        curr_node = self.root
        for letter in prefix:
            if letter not in curr_node.children:
                return False
            curr_node = curr_node.children[letter]
        
        return True
        