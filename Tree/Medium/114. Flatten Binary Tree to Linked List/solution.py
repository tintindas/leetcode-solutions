# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root or not (root.left or root.right):
            return root

        temp = root.right
        root.right = self.flatten(root.left)
        root.left = None

        curr = root

        while curr.right:
            curr = curr.right

        curr.right = self.flatten(temp)

        return root