from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
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

        return dfs(p, q)
        