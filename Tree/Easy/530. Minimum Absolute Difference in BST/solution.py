# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorder(self, node: TreeNode) -> None:
        if not node:
            return

        self.inorder(node.left)

        if self.prev != None:
            diff = abs(node.val - self.prev)
            if not self.ans or diff < self.ans:
                self.ans = diff

        self.prev = node.val

        self.inorder(node.right)

    def getMinimumDifference(self, root: TreeNode) -> int:
        self.ans = None
        self.prev = None

        self.inorder(root)

        return self.ans
