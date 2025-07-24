from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_len = 0
        def dfs(v):
            nonlocal max_len
            left_len = dfs(v.left) if v.left else 0
            right_len = dfs(v.right) if v.right else 0

            local_max_diam = left_len + right_len
            max_len = max(max_len, local_max_diam)

            return max(left_len, right_len) + 1


        dfs(root)
        return max_len