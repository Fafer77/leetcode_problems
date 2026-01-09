"""
Idea: DFS where we pass vertex and depth. We increase depth each time by 1 because we are diving deeper.
DFS will be returning (depth at which deepest vertex in subtree is, root of that subtree)
Base case: if it is None then return depth - 1, because we don't want to count that depth and None as vertex
Otherwise we compare information collected from children and choose to either maintain information from
one of the children if it dives deeper, otherwise we return that deepest depth and current vertex to merge
the subtrees.
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(v, depth):
            if v is None:
                return depth - 1, None

            left_best_depth, left_sb_root = dfs(v.left, depth + 1)
            right_best_depth, right_sb_root = dfs(v.right, depth + 1)

            if left_best_depth > right_best_depth:
                return left_best_depth, left_sb_root
            elif right_best_depth > left_best_depth:
                return right_best_depth, right_sb_root
            else:
                return left_best_depth, v
        
        _, sb_root = dfs(root, 0)
        return sb_root
