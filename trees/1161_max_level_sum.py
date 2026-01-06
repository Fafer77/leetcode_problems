"""
Idea: Let's use BFS because it will allow us to process everything level by level.
While traversing we will keep variables:
- max_sum (current maximum sum up to particular level)
- level_max_sum -> level at which max sum is held
- curr_sum, curr_level in order to keep track of current level values
"""
from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        queue = deque([root])
        level_max_sum = 1
        max_sum = root.val
        curr_level = 0

        while queue:
            curr_level += 1
            curr_sum = 0
            q_size = len(queue)

            for _ in range(q_size):
                node = queue.popleft()
                curr_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if curr_sum > max_sum:
                max_sum = curr_sum
                level_max_sum = curr_level
        
        return level_max_sum
