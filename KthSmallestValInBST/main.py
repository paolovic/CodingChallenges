from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        result = None

        def kthSmallestHelper(root: Optional[TreeNode]) -> int:
            nonlocal count, result
            if root is None:
                return
            kthSmallestHelper(root.left)
            count+=1
            if count == k:
                result = root.val
            kthSmallestHelper(root.right)

        kthSmallestHelper(root)
        return result



s = Solution()
# Test Case 1:
tree1 = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
# Expected: 1
print(s.kthSmallest(tree1, 1))

# Test Case 2:
tree2 = TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)), TreeNode(6))
# Expected: 3
print(s.kthSmallest(tree2, 3))

# Test Case 3:
tree3 = TreeNode(2, TreeNode(1), TreeNode(3))
# Expected: 2
print(s.kthSmallest(tree3, 2))
