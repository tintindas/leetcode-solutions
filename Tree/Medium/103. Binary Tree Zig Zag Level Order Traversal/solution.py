from collections import deque
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = []

        if not root:
            return ans

        q = deque()
        q.append(root)
        left_to_right = True

        while q:

            size = len(q)
            level = []
            q_next = deque()

            if left_to_right:
                for _ in range(size):
                    node = q.popleft()
                    level.append(node.val)
                    if node.left:
                        q_next.append(node.left)
                    if node.right:
                        q_next.append(node.right)
            else:
                for _ in range(size, 0, -1):
                    node = q.pop()
                    level.append(node.val)
                    if node.right:
                        q_next.appendleft(node.right)
                    if node.left:
                        q_next.appendleft(node.left)

            ans.append(level)
            q = q_next
            left_to_right = not left_to_right

        return ans
