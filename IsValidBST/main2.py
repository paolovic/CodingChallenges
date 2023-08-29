from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
import numpy as np
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValidBSTHelper(root, -np.inf, np.inf)

    def isValidBSTHelper(self, root, min, max):
        if root is None:
            return True
        if root.val <= min:
            return False
        if root.val >= max:
            return False
        return self.isValidBSTHelper(root.left, min, root.val) and self.isValidBSTHelper(root.right, root.val, max)

s = Solution()
root = TreeNode(2, TreeNode(1), TreeNode(3))
print(s.isValidBST(root))  # True

root = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
print(s.isValidBST(root))  # False