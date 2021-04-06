# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not (root.left or root.right):
            return 0

        stack = [root]
        ans = 0

        while stack:
            node = stack.pop()
            if node.right:
                stack.append(node.right)

            if node.left:
                if not (node.left.left or node.left.right):
                    ans += node.left.val
                else:
                    stack.append(node.left)

        return ans
