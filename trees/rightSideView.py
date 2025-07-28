"""
Level BFS. We consider each level using BFS and add nodes from right to left from
each level as what interests us is rightmost element on each level
"""

from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if root is None:
            return result
        
        queue = deque([root])
        size = 1

        while queue:
            rightmost = queue.popleft()
            result.append(rightmost.val)
            size -= 1
            new_size = 0
            if rightmost.right:
                queue.append(rightmost.right)
                new_size += 1
            if rightmost.left:
                queue.append(rightmost.left)
                new_size += 1
            
            for _ in range(size):
                node = queue.popleft()
                if node.right:
                    queue.append(node.right)
                    new_size += 1
                if node.left:
                    queue.append(node.left)
                    new_size += 1
            
            size = new_size
        
        return result
