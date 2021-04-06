from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        ans = []

        stack = [(root, "")]

        while stack:
            node, path = stack.pop()

            if not node.left and not node.right:
                ans.append(path + str(node.val))

            if node.left:
                stack.append((node.left, path + str(node.val) + "->"))
            if node.right:
                stack.append((node.right, path + str(node.val) + "->"))

        return ans