class Solution:
    def romanToInt(self, s: str) -> int:

        values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        ans = 0

        for i, c in enumerate(s):

            ans += values[c]

            if i and (values[s[i]] > values[s[i - 1]]):
                ans -= 2 * values[s[i - 1]]

        return ans