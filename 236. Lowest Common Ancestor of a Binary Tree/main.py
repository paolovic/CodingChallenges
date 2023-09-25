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
        if left is not None and right is not None:
            return root
        return left or right

    def lowestCommonAncestorHelper(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ):
        if root is None:
            return None
        if root.val == p.val or root.val == q.val:
            return root
        left = self.lowestCommonAncestorHelper(root.left, p, q)
        right = self.lowestCommonAncestorHelper(root.right, p, q)
        if left is not None and right is not None:
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

p = TreeNode(5)
q = TreeNode(1)
print(s.lowestCommonAncestor(root, p, q).val)  # 3

p = TreeNode(5)
q = TreeNode(4)
print(s.lowestCommonAncestor(root, p, q).val)  # 5

root = TreeNode(1)
root.left = TreeNode(2)

p = TreeNode(1)
q = TreeNode(2)
print(s.lowestCommonAncestor(root, p, q).val)  # 1
