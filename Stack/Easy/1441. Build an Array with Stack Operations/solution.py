from typing import List


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        i = 0
        j = 1
        res = []

        while i < len(target):
            if target[i] == j:
                res.append("Push")
                i += 1
            else:
                res.extend(["Push", "Pop"])

            j += 1

        return res