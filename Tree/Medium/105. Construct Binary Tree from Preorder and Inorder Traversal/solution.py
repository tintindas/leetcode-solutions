from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def helper(self, pre_start, in_start, in_end, preorder, inorder):
        if pre_start > len(preorder) - 1 or in_start > in_end:
            return None

        root = TreeNode(preorder[pre_start])

        in_index = inorder.index(preorder[pre_start])

        root.left = self.helper(pre_start + 1, in_start, in_index - 1, preorder, inorder)
        root.right = self.helper(pre_start + in_index - in_start + 1, in_index + 1, in_end, preorder, inorder)

        return root

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        return self.helper(0, 0, len(inorder) - 1, preorder, inorder)
