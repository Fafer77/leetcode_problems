from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        def dfs(v, min_bound, max_bound):
            if v is None:
                return True
            
            if v.val <= min_bound or v.val >= max_bound:
                return False
            
            return dfs(v.left, min_bound, v.val) and dfs(v.right, v.val, max_bound)

        return dfs(root, float('-inf'), float('inf'))
