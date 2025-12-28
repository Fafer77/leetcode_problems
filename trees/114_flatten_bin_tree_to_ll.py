from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if root is None:
            return
        
        def dfs(v):
            if v is None:
                return None
            
            tail_left = dfs(v.left)
            tail_right = dfs(v.right)
            
            if tail_left:
                tail_left.right = v.right
                v.right = v.left
                v.left = None

            if tail_right:
                return tail_right
            elif tail_left:
                return tail_left
            return v

        dfs(root)


        