# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def subtree_sum(self, node: TreeNode) -> int:
        if not node:
            return 0

        l = self.subtree_sum(node.left)
        r = self.subtree_sum(node.right)

        self.ans += abs(l - r)

        return node.val + l + r

    def findTilt(self, root: TreeNode) -> int:
        self.ans = 0
        self.subtree_sum(root)
        return self.ans