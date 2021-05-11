class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        m = len(s1) + 1
        n = len(s2) + 1

        dp = [[False] * (n) for _ in range(m)]

        dp[0][0] = True

        for i in range(1, m):
            dp[i][0] = s1[i - 1] == s3[i - 1] and dp[i - 1][0]

        for j in range(1, n):
            dp[0][j] = s2[j - 1] == s3[j - 1] and dp[0][j - 1]

        for i in range(1, m):
            for j in range(1, n):

                if s1[i - 1] == s3[i + j - 1]:
                    dp[i][j] = dp[i - 1][j]

                if s2[j - 1] == s3[i + j - 1]:
                    dp[i][j] = dp[i][j] or dp[i][j - 1]

        return dp[-1][-1]