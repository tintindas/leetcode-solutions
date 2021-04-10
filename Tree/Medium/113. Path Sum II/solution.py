from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def helper(self, node: TreeNode, targetSum: int) -> None:
        if not node:
            return

        if not node.left and not node.right:
            if targetSum == node.val:
                self.ans.append(self.stack + [node.val])
            return

        self.stack.append(node.val)
        self.helper(node.left, targetSum - node.val)
        self.helper(node.right, targetSum - node.val)
        self.stack.pop()

    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        self.ans = []
        self.stack = []
        if not root:
            return []
        self.helper(root, targetSum)
        return self.ans