from string import ascii_uppercase


class Solution:
    def convertToTitle(self, n: int) -> str:
        letters = ascii_uppercase

        ans = ""

        while n:
            c = letters[(n - 1) % 26]
            ans = c + ans
            n = (n - 1) // 26

        return ans
