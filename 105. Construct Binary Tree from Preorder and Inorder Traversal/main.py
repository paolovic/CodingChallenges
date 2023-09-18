from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        return self.recurse(0, len(preorder)-1, 0, len(inorder)-1)

    def recurse(self, pStart, pEnd, inStart, inEnd):
        if pStart > pEnd or inStart > inEnd:
            return None
        
        rootVal = preorder[pStart]
        inIndex = inorder.index(rootVal)
        nLeft = inIndex - inStart

        root = TreeNode(rootVal)
        root.left = self.recurse(pStart+1, pStart+nLeft, inStart, inEnd-1)
        root.right = self.recurse(pStart+1+nLeft, pEnd, inIndex+1, inEnd)

        return root

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
s = Solution()
s.buildTree(preorder, inorder)  # [3,9,20,null,null,15,7]

preorder = [-1]
inorder = [-1]
s.buildTree(preorder, inorder)  # [-1]