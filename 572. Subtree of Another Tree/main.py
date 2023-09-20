from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        if self.compare(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def compare(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None and subRoot is None:
            return True
        if root is None or subRoot is None or root.val != subRoot.val:
            return False
        return self.compare(root.left, subRoot.left) and self.compare(root.right, subRoot.right)


s = Solution()
# [-1,-4,8,-6,-2,3,9,null,-5,null,null,0,7]
root = TreeNode(
    -1,
    TreeNode(-4, TreeNode(-6), TreeNode(-2, TreeNode(-5))),
    TreeNode(8, TreeNode(3), TreeNode(9, None, TreeNode(0, None, TreeNode(7)))),
)
subRoot = TreeNode(3, TreeNode(0), TreeNode(5848))
print(s.isSubtree(root, subRoot))


root = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5))
subRoot = TreeNode(4, TreeNode(1), TreeNode(2))
print(s.isSubtree(root, subRoot))  # True

root = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2, TreeNode(0))), TreeNode(5))
subRoot = TreeNode(4, TreeNode(1), TreeNode(2))
print(s.isSubtree(root, subRoot))  # False
