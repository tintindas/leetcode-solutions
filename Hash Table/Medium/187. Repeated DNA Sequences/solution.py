from collections import Counter
from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:

        count = Counter()

        for i in range(len(s) - 9):
            count[s[i : i + 10]] += 1

        ans = [x for x in count if count[x] > 1]

        return ans