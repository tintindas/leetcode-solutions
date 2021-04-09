# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def helper(self, node, lo=float("-inf"), hi=float("inf")):
        if not node:
            return True

        if not lo < node.val < hi:
            return False

        return self.helper(node.left, lo, node.val) and self.helper(node.right, node.val, hi)

    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True

        return self.helper(root)
