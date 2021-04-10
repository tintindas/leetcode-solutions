from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def helper(self, node: TreeNode, res: List[int]) -> None:
        if not node:
            return

        res.append(node.val)
        self.helper(node.left, res)
        self.helper(node.right, res)

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.helper(root, res)
        return res