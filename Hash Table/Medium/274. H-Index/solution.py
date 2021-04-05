from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:

        citations.sort(reverse=True)

        i = 0

        while i < len(citations):
            if citations[i] <= i + 1:
                if citations[i] == i + 1:
                    return i + 1
                else:
                    return i
            i += 1

        return i