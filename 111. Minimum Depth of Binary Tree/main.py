from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        min_depth = 1
        queue = [root]
        while len(queue) > 0:
            for _ in range(len(queue)):
                node = queue.pop(0)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
                if node.right is None and node.left is None:
                    return min_depth
            min_depth += 1
        return min_depth

s = Solution()
root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(s.minDepth(root))  # 2

root = TreeNode(
    2, None, TreeNode(3, None, TreeNode(4, None, TreeNode(5, None, TreeNode(6))))
)
print(s.minDepth(root))  # 5
