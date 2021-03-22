from typing import List


class Solution:
    def calPoints(self, ops: List[str]) -> int:
        record = []

        for op in ops:
            if op == "+":
                record.append(record[-2] + record[-1])
            elif op == "D":
                record.append(record[-1] * 2)
            elif op == "C":
                record.pop()
            else:
                record.append(int(op))

        return sum(record)