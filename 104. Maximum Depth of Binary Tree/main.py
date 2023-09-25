from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


s = Solution()
print(
    s.maxDepth(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))))
)  # 3
print(s.maxDepth(TreeNode(1, None, TreeNode(2))))  # 2
print(s.maxDepth(None))  # 0
print(s.maxDepth(TreeNode(0)))  # 1
