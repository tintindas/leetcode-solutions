class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 0 or int(s[0]) == 0:
            return 0

        if len(s) == 1:
            return 1

        dp = [0] * len(s)

        dp[0] = 1
        if 1 <= int(s[1]) <= 9:
            dp[1] += 1

        if 1 <= int(s[0:2]) <= 26:
            dp[1] += 1

        for i in range(2, len(s)):

            if 1 <= int(s[i]) <= 9:
                dp[i] += dp[i - 1]

            if 10 <= int(s[i - 1 : i + 1]) <= 26:
                dp[i] += dp[i - 2]

        return dp[-1]