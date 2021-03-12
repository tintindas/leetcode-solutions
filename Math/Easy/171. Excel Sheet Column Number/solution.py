from string import ascii_uppercase


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:

        letters = ascii_uppercase

        ans = 0
        idx = len(columnTitle) - 1
        place = 1

        while idx >= 0:
            ans += place * (letters.index(columnTitle[idx]) + 1)
            place *= 26
            idx -= 1

        return ans