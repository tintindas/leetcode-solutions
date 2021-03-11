class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        l = 1
        r = x // 2

        while l <= r:
            mid = (l + r) // 2

            if mid > x / mid:
                r = mid - 1
            else:
                l = mid + 1

        return r