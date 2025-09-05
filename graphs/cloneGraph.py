from typing import Optional

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        old_to_new = {}
        
        def dfs(org_node):
            if org_node in old_to_new:
                return old_to_new[org_node]
            
            copy_node = Node(org_node.val)
            old_to_new[org_node] = copy_node

            for v in org_node.neighbors:
                copy_node.neighbors.append(dfs(v))
            
            return copy_node
        
        if node is None:
            return None
        
        return dfs(node)
