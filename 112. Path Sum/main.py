from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        targetSum-=root.val
        if root.left is None and root.right is None and targetSum==0:
            return True
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)

s = Solution()
root = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))), TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1))))
print(s.hasPathSum(root, 22))  # True
root = TreeNode(1, TreeNode(2), TreeNode(3))
print(s.hasPathSum(root, 5))  # False
root = TreeNode()
print(s.hasPathSum(root, 0))  # False