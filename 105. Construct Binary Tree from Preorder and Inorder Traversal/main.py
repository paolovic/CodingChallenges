from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        pass

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
s = Solution()
s.buildTree(preorder, inorder)  # [3,9,20,null,null,15,7]

preorder = [-1]
inorder = [-1]
s.buildTree(preorder, inorder)  # [-1]