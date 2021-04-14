from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[-1][-1] or obstacleGrid[0][0]:
            return 0

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        for i in range(m):
            for j in range(n):
                obstacleGrid[i][j] = -1 if obstacleGrid[i][j] else 0

        obstacleGrid[0][0] = 1

        for i in range(1, m):
            if not obstacleGrid[i][0]:
                obstacleGrid[i][0] = obstacleGrid[i - 1][0]

        for i in range(1, n):
            if not obstacleGrid[0][i]:
                obstacleGrid[0][i] = obstacleGrid[0][i - 1]

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] != -1:
                    top = obstacleGrid[i - 1][j] if obstacleGrid[i - 1][j] != -1 else 0
                    left = obstacleGrid[i][j - 1] if obstacleGrid[i][j - 1] != -1 else 0

                    obstacleGrid[i][j] = top + left

        return obstacleGrid[m - 1][n - 1]
