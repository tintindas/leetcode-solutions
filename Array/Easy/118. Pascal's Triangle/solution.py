from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        if numRows <= 0:
            return [[]]
        ans = []
        first_row = [1]

        ans.append(first_row)

        for i in range(1, numRows):
            row = []
            prev_row = ans[-1]
            row.append(1)
            for j in range(1, i):
                row.append(prev_row[j - 1] + prev_row[j])
            row.append(1)
            ans.append(row)

        return ans
