class Solution:
    def isPerfectSquare(self, num: int) -> bool:

        lo = 1
        hi = num

        while lo <= hi:
            mid = (lo + hi) // 2

            if mid * mid == num:
                return True
            elif mid * mid > num:
                hi = mid - 1
            else:
                lo = mid + 1

        return False