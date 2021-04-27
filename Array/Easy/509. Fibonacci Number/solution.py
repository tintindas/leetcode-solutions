class Solution:
    def fib(self, n: int) -> int:
        if n < 1:
            return 0
        if n == 1:
            return 1

        s_last = 0
        last = 1

        for _ in range(2, n + 1):
            cur = s_last + last
            s_last = last
            last = cur

        return cur