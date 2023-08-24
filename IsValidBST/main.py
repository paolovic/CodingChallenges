from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

import numpy as np
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValidBSTHelper(root, -np.inf, np.inf)
    
    def isValidBSTHelper(self, root: Optional[TreeNode], min: float, max:float) -> bool:
        if root is None:
            return True
        if root.val <= min:
            return False
        if root.val >= max:
            return False
        return self.isValidBSTHelper(root.left, min, root.val) and self.isValidBSTHelper(root.right, root.val, max)


s = Solution()
# Test Case 1:
tree1 = TreeNode(2, TreeNode(1), TreeNode(3))
# Expected: True
print(s.isValidBST(tree1))

# Test Case 2:
tree2 = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
# Expected: False
print(s.isValidBST(tree2))
