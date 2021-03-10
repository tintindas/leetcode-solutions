class Solution:
    def reverse(self, x: int) -> int:
        num = x
        max_int = 2 ** 31 - 1
        min_int = -1 * (2 ** 31)

        if num > max_int or num < min_int:
            return 0

        sign = 1 if num > 0 else -1

        num = abs(num)

        ans = 0
        while num:
            last_digit = num % 10
            num = num // 10
            if ans > max_int / 10:
                return 0
            ans = ans * 10 + last_digit

        return ans * sign
