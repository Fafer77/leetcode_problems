from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    # '#' = null node
    # ',' = values delimiter
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        def dfs(v):
            nonlocal res
            if v is None:
                res.append('#')
                return

            res.append(str(v.val))
            dfs(v.left)
            dfs(v.right)
            return

        dfs(root)
        return ','.join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        
        vals = data.split(',')
        idx = 0
        def dfs():
            nonlocal idx
            if vals[idx] == '#':
                idx += 1
                return None

            curr_node = TreeNode(int(vals[idx]))
            idx += 1
            curr_node.left = dfs()
            curr_node.right = dfs()

            return curr_node

        root = dfs()
        return root
