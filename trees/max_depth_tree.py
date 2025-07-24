from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        def dfs(v):
            depth_left = dfs(v.left) if v.left else 0
            depth_right = dfs(v.right) if v.right else 0
            
            return max(depth_left, depth_right) + 1

        max_depth = dfs(root)
        return max_depth
