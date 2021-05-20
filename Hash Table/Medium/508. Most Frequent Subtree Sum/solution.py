from collections import Counter
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def helper(self, node):
        if not node:
            return 0

        s = node.val + self.helper(node.left) + self.helper(node.right)

        self.count[s] += 1

        return s

    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        self.count = Counter()
        self.helper(root)

        _, f = self.count.most_common(1)[0]

        ans = []
        for key, val in self.count.most_common():
            if val == f:
                ans.append(key)
            else:
                break

        return ans
