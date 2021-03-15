class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        i = 1

        while i <= n:
            if i == n:
                return True
            i *= 2

        return False