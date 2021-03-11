from collections import deque


class Solution:
    def addBinary(self, a: str, b: str) -> str:

        a_idx = len(a) - 1
        b_idx = len(b) - 1
        carry = 0
        digits = deque()

        while (a_idx >= 0) or (b_idx >= 0) or carry:

            a_d = int(a[a_idx]) if a_idx >= 0 else 0
            b_d = int(b[b_idx]) if b_idx >= 0 else 0

            d = a_d + b_d + carry

            carry = 1 if d > 1 else 0

            digits.appendleft(str(d % 2))

            a_idx -= 1
            b_idx -= 1

        return "".join(list(digits))
