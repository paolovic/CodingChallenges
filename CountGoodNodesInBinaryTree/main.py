# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.goodNodesHelper(root, root.val)

    def goodNodesHelper(self, root, max):
        if root is None:
            return 0
        if root.val >= max:
            max = root.val
            res = 1
        else:
            res = 0
        res += self.goodNodesHelper(root.left, max)
        res += self.goodNodesHelper(root.right, max)
        return res


s = Solution()
input = TreeNode(3, TreeNode(1, TreeNode(3)), TreeNode(4, TreeNode(1), TreeNode(5)))
print(s.goodNodes(input))
# Expected: 4

input = TreeNode(3, TreeNode(3, TreeNode(4), TreeNode(2)), TreeNode(1))
print(s.goodNodes(input))
# Expected: 3
