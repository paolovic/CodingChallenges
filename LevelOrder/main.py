from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        result = []
        queue = []
        queue.append(root)

        while len(queue) > 0:
            level = []
            for _ in range(len(queue)):
                n = queue.pop(0)
                if n.left is not None:
                    queue.append(n.left)
                if n.right is not None:
                    queue.append(n.right)
                level.append(n.val)
            result.append(level)

        return result


s = Solution()
# Test Case 1:
tree1 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
# Expected: [[3],[9,20],[15,7]]
print(s.levelOrder(tree1))

# Test Case 2:
tree2 = TreeNode(1)
# Expected: [[1]]
print(s.levelOrder(tree2))

# Test Case 3:
tree3 = None
# Expected: []
print(s.levelOrder(tree3))
