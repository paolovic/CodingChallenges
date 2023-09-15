from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

import numpy as np

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max = root.val
        self.maxPathSumHelper(root)
        return self.max
    
    def maxPathSumHelper(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        left = max(self.maxPathSumHelper(root.left), 0)
        right = max(self.maxPathSumHelper(root.right), 0)
        curMax = left + right + root.val
        self.max = max(self.max, curMax)
        return root.val + max(left, right)


s = Solution()
root = TreeNode(1, TreeNode(2), TreeNode(3))
print(s.maxPathSum(root))  # 6

root = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(s.maxPathSum(root))  # 42

root = TreeNode(-3)
print(s.maxPathSum(root))  # -3

root = TreeNode(2, TreeNode(-1))
print(s.maxPathSum(root))  # 2

root = TreeNode(1, TreeNode(-2, TreeNode(1, TreeNode(-1)), TreeNode(3)), TreeNode(-3, TreeNode(-2)))
print(s.maxPathSum(root))  # 3

root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
print(s.maxPathSum(root))  # 18
