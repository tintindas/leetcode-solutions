from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorder_traversal(self, node: TreeNode) -> None:
        if not node:
            return

        self.inorder_traversal(node.left)

        if self.prev != None:

            if self.prev == node.val:
                self.count += 1
            else:
                self.count = 1

        if self.count > self.max_count:
            self.max_count = self.count
            self.modes.clear()
            self.modes.append(node.val)
        elif self.count == self.max_count:
            self.modes.append(node.val)

        self.prev = node.val

        self.inorder_traversal(node.right)

    def findMode(self, root: TreeNode) -> List[int]:
        self.modes = []
        self.prev = None
        self.count = 1
        self.max_count = 0

        self.inorder_traversal(root)

        return self.modes
