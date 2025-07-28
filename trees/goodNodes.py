class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        counter = 0

        def dfs(v, local_max):
            if v is None:
                return

            nonlocal counter
            if v.val >= local_max:
                counter += 1
                local_max = v.val
            
            dfs(v.left, local_max)
            dfs(v.right, local_max)

            return


        dfs(root, float('-inf'))
        return counter