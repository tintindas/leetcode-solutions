# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        l = self.minDepth(root.left)
        r = self.minDepth(root.right)

        if not l and not r:
            return 1

        if not l and r:
            return r + 1

        if not r and l:
            return l + 1

        return 1 + min(l, r)
