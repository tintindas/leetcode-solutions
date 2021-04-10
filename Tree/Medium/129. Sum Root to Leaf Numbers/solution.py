# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def helper(self, node: TreeNode) -> None:
        if not node:
            return

        if not node.left and not node.right:
            num = int("".join(self.stack + [str(node.val)]))
            self.ans += num
            return

        self.stack.append(str(node.val))
        self.helper(node.left)
        self.helper(node.right)
        self.stack.pop()

    def sumNumbers(self, root: TreeNode) -> int:
        self.ans = 0
        self.stack = []
        self.helper(root)
        return self.ans
