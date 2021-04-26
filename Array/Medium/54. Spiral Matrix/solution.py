from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])

        top = 0
        bottom = m - 1
        left = 0
        right = n - 1

        res = []

        while True:

            if left > right:
                break
            print("left -> right")
            for j in range(left, right + 1):
                res.append(matrix[top][j])
            top += 1

            if top > bottom:
                break
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1

            if left > right:
                break
            print("right -> left")
            for j in range(right, left - 1, -1):
                res.append(matrix[bottom][j])
            bottom -= 1

            if top > bottom:
                break
            print("bottom -> top")
            for i in range(bottom, top - 1, -1):
                res.append(matrix[i][left])
            left += 1

        return res
