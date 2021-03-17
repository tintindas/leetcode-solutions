from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        rev = digits[::-1]

        i = 0
        carry = 1
        while i < len(rev) and carry == 1:
            digit = carry + rev[i]
            rev[i] = digit % 10
            carry = digit // 10
            i += 1

        if carry:
            rev.append(1)

        return rev[::-1]
