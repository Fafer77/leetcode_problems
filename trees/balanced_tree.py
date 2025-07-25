from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        def dfs(v):
            if v is None:
                return 0
            
            left_depth = dfs(v.left)
            right_depth = dfs(v.right)

            if left_depth == -1 or right_depth == -1:
                return -1
            
            if abs(left_depth - right_depth) > 1:
                return -1
            
            return max(left_depth, right_depth) + 1

        return dfs(root) != -1
