# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longest_path(self, node: TreeNode) -> int:
        if not node:
            return 0

        l = self.longest_path(node.left)
        r = self.longest_path(node.right)

        self.diameter = max(self.diameter, l + r)

        return 1 + max(l, r)

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.diameter = 0

        self.longest_path(root)
        return self.diameter
