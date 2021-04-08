# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: "Node") -> int:

        if not root:
            return 0

        depths = [self.maxDepth(child) for child in root.children]

        if len(depths):
            return 1 + max(depths)
        else:
            return 1