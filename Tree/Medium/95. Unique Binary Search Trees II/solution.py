from collections import defaultdict
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def helper(self, start, end):
        if start > end:
            return [None]

        if (start, end) in self.cache:
            return self.cache[(start, end)]

        else:
            all_trees = []

            for cur_root_val in range(start, end + 1):

                left_subtrees = self.helper(start, cur_root_val - 1)
                right_subtrees = self.helper(cur_root_val + 1, end)

                for left_subtree in left_subtrees:
                    for right_subtree in right_subtrees:

                        cur_root = TreeNode(cur_root_val)
                        cur_root.left = left_subtree
                        cur_root.right = right_subtree

                        self.cache[(start, end)] += [cur_root]

                        all_trees.append(cur_root)

            return all_trees

    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        self.cache = defaultdict(list)
        return self.helper(1, n)
