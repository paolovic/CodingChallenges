from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.longest = 0
        self.diameterOfBinaryTreeHelper(root)
        return self.longest

    def diameterOfBinaryTreeHelper(self, root):
        if root is None:
            return 0
        left = self.diameterOfBinaryTreeHelper(root.left)
        right = self.diameterOfBinaryTreeHelper(root.right)
        self.longest = max(self.longest, right + left)
        return 1 + max(left, right)


s = Solution()
root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
print(s.diameterOfBinaryTree(root))  # 3

root = TreeNode(1, TreeNode(2), TreeNode(3))
print(s.diameterOfBinaryTree(root))  # 2

root = TreeNode(1)
print(s.diameterOfBinaryTree(root))  # 0
