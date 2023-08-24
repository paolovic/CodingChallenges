from typing import Optional
import math

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def recurse(root):
            if root is None:
                return 0
            h_left = recurse(root.left)
            h_right = recurse(root.right)
            
            if h_left==-1 or h_right==-1:
                return -1
            
            return -1 if abs(h_left-h_right)>1 else max(h_left, h_right)+1

        return recurse(root) != -1


"""
Input: root = [3,9,20,null,null,15,7]
Output: true
"""

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.left = TreeNode(7)

s = Solution()
print(s.isBalanced(root))

"""
Input: root = [1,2,2,3,null,null,3,4,null,null,4]
Output: false
"""

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.left.left = TreeNode(4)
root.right.right = TreeNode(3)
root.right.right.right = TreeNode(4)


s = Solution()
print(s.isBalanced(root))