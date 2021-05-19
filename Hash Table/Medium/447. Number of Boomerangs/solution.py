from collections import defaultdict
from typing import List


class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        if len(points) < 3:
            return 0

        ans = 0
        for x1, y1 in points:
            counter = defaultdict(int)
            for x2, y2 in points:
                dist = (x2 - x1) ** 2 + (y2 - y1) ** 2

                if dist in counter:
                    ans += 2 * counter[dist]

                counter[dist] += 1

        return ans