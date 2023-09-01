from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.res = None
        self.count = 0
        self.kthSmallestHelper(root, k)
        return self.res

    def kthSmallestHelper(self, root, k):
        if root is None:
            return None
        self.kthSmallestHelper(root.left, k)
        self.count+=1
        if self.count==k:
            self.res = root
        self.kthSmallestHelper(root.right, k)
        

s = Solution()
root = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
print(s.kthSmallest(root, 1).val)

root = TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)), TreeNode(6))
print(s.kthSmallest(root, 3).val)

root = TreeNode(2, TreeNode(1), TreeNode(3))
print(s.kthSmallest(root, 1).val)

root = TreeNode(1, None, TreeNode(2))
print(s.kthSmallest(root, 2).val)
