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
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root


s = Solution()
root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(8)
root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)
root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)

p = TreeNode(2)
q = TreeNode(8)
print(s.lowestCommonAncestor(root, p, q).val)  # 6

p = TreeNode(2)
q = TreeNode(4)
print(s.lowestCommonAncestor(root, p, q).val)  # 2

root = TreeNode(2)
root.left = TreeNode(1)
p = TreeNode(2)
q = TreeNode(1)
print(s.lowestCommonAncestor(root, p, q).val)  # 2
