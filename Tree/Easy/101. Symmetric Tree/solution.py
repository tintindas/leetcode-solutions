# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def helper(self, l: TreeNode, r: TreeNode) -> bool:
        if not l and not r:
            return True

        if not l or not r:
            return False

        return l.val == r.val and self.helper(l.left, r.right) and self.helper(l.right, r.left)

    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return False

        return self.helper(root.left, root.right)
