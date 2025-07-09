class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters_count = [0] * 26

        for c in s:
            letters_count[ord(c) - ord('a')] += 1
        
        for c in t:
            letters_count[ord(c) - ord('a')] -= 1

        for c in letters_count:
            if c != 0:
                return False
        
        return True