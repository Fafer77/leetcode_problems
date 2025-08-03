from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.result = float('-inf')

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.result

    def dfs(self, v: Optional[TreeNode]) -> int:
        if not v:
            return 0
        
        left = max(0, self.dfs(v.left))
        right = max(0, self.dfs(v.right))

        self.result = max(self.result, v.val + left + right)
        return v.val + max(left, right)
