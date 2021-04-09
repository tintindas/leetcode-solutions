class Solution:
    def numTrees(self, n: int) -> int:

        dp = [1, 1]

        for i in range(2, n + 1):

            ans = 0

            for k in range(0, i):

                ans += dp[k] * dp[i - k - 1]

            dp.append(ans)

        return dp[n]