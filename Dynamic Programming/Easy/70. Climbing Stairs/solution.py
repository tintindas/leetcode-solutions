class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1

        last = 1
        second_last = 1
        ans = 0

        for _ in range(2, n + 1):
            ans = last + second_last
            second_last = last
            last = ans

        return ans