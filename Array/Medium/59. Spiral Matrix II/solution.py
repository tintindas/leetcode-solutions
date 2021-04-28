from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0] * n for x in range(n)]

        top = 0
        bottom = n - 1
        left = 0
        right = n - 1

        num = 1
        while True:

            for j in range(left, right + 1):
                res[top][j] = num
                num += 1
            top += 1

            if top > bottom:
                break

            for i in range(top, bottom + 1):
                res[i][right] = num
                num += 1
            right -= 1

            if left > right:
                break

            for j in range(right, left - 1, -1):
                res[bottom][j] = num
                num += 1
            bottom -= 1

            if top > bottom:
                break

            for i in range(bottom, top - 1, -1):
                res[i][left] = num
                num += 1
            left += 1

            if left > right:
                break

        return res