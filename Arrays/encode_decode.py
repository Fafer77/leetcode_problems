from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res = res + str(len(s)) + '#' + s
        
        return res

    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []
        res = []
        n = len(s)
        i = 0
        while i < n:
            j = i
            while j < n and s[j] != '#':
                j += 1
            
            if j == n:
                break

            shift = s[i:j]
            try:
                length = int(shift)
            except ValueError:
                return []
            
            start_of_string = j + 1
            end_of_string = start_of_string + length

            if end_of_string > n:
                return []

            curr_s = s[start_of_string:end_of_string]
            res.append(curr_s)

            i = end_of_string
        
        return res


sol = Solution()
print(sol.encode(["we","say",":","yes","!@#$%^&*()"]))
print(sol.decode("4neet4code4love3you"))
