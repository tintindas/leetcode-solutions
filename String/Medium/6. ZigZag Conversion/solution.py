class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = len(s)
        if len(s) <= numRows:
            return s
        if numRows == 1:
            return s

        rows = ["" for _ in range(numRows)]

        direction = 1
        row = 0

        for i in range(len(s)):

            if row == 0:
                direction = 1

            if row == numRows - 1:
                direction = -1

            if direction == 1:
                rows[row] += s[i]
                row += 1

            if direction == -1:
                rows[row] += s[i]
                row -= 1

        return "".join(rows)
