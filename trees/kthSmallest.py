from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(v, local_k):
            if v is None:
                return (0, float('inf'))
            
            size_left, val_left = dfs(v.left, local_k)
            if val_left != float('inf'):
                return (-1, val_left)

            if size_left + 1 == local_k:
                return (-1, v.val)
            
            size_right, val_right = dfs(v.right, local_k - (size_left + 1))
            if val_right != float('inf'):
                return (-1, val_right)
            
            return (size_left + 1 + size_right, float('inf'))

        _, val = dfs(root, k)
        return val