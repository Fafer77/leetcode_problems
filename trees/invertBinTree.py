from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(v):
            v.left, v.right = v.right, v.left
            dfs(v.left)
            dfs(v.right)
            return
        
        dfs(root)
        return root