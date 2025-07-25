from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot is None:
            return True
        
        def dfs(v, u):
            if v is None and u is None:
                return True
            elif v is None and u is not None:
                return False
            elif v is not None and u is None:
                return False
            elif v.val != u.val:
                return False

            return dfs(v.left, u.left) and dfs(v.right, u.right)
        
        def check_each_node(v):
            if v is None:
                return False
            elif dfs(v, subRoot):
                return True
            else:
                return check_each_node(v.left) or check_each_node(v.right)
        
        return check_each_node(root)
