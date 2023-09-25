from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        if root is None:
            return None
        if root.val == p.val or root.val == q.val:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left or right


s = Solution()
root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)
print(s.lowestCommonAncestor(root, root.left, root.right).val)  # 3
print(s.lowestCommonAncestor(root, root.left, root.left.right.right).val)  # 5
print(s.lowestCommonAncestor(root, root.left, root.left.right.left).val)  # 2

root = TreeNode(1)
root.left = TreeNode(2)
print(s.lowestCommonAncestor(root, root, root.left).val)  # 1
