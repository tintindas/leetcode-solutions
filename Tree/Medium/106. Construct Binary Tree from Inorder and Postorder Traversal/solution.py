from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def helper(self, post_start, in_start, in_end, postorder, inorder):
        if post_start < 0 or in_start > in_end:
            return None

        root = TreeNode(postorder[post_start])

        in_index = inorder.index(root.val)

        root.left = self.helper(post_start - (in_end - in_index) - 1, in_start, in_index - 1, postorder, inorder)
        root.right = self.helper(post_start - 1, in_index + 1, in_end, postorder, inorder)

        return root

    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        return self.helper(len(postorder) - 1, 0, len(inorder) - 1, postorder, inorder)
