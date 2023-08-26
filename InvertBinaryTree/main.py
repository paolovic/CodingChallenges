from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return
        temp = root.left
        root.left = root.right
        root.right = temp
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


s = Solution()
root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
s.invertTree(root)
print(root.val)  # 4
print(root.left.val)  # 7
print(root.right.val)  # 2
print(root.left.left.val)  # 9
print(root.left.right.val)  # 6
print(root.right.left.val)  # 3
print(root.right.right.val)  # 1

root = TreeNode(2, TreeNode(1), TreeNode(3))
s.invertTree(root)
print(root.val)  # 2
print(root.left.val)  # 3
print(root.right.val)  # 1

root = TreeNode()
s.invertTree(root)
print(root.val)  # 0
