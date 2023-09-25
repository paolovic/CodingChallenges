from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        result = []
        queue = [root]
        while len(queue) > 0:
            len_q = len(queue)
            popcounter = 0
            for _ in range(len_q):
                n = queue.pop(0)
                popcounter+=1
                if popcounter == len_q:
                    result.append(n.val)
                if n.left is not None:
                    queue.append(n.left)
                if n.right is not None:
                    queue.append(n.right)

        return result
                


s = Solution()
# Test Case 1:
tree1 = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4)))
# Expected: [1,3,4]
print(s.rightSideView(tree1))

# Test Case 2:
tree2 = TreeNode(1, None, TreeNode(3))
# Expected: [1,3]
print(s.rightSideView(tree2))
