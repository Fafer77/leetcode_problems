from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        max_product = float('-inf')

        def dfs_total(v):
            if v is None:
                return 0
            
            left_sum = dfs_total(v.left)
            right_sum = dfs_total(v.right)

            return left_sum + right_sum + v.val
        
        total_sum = dfs_total(root)

        def dfs_subsums(v):
            nonlocal max_product

            if v is None:
                return 0
            
            left_sum = dfs_subsums(v.left)
            right_sum = dfs_subsums(v.right)
            subtree_sum = left_sum + right_sum + v.val
            curr_product = (total_sum - subtree_sum) * subtree_sum
            max_product = max(max_product, curr_product)

            return subtree_sum

        dfs_subsums(root)

        return max_product % (10**9 + 7)
