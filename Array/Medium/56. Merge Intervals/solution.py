from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()
        start = intervals[0][0]
        end = intervals[0][1]

        for i in range(1, len(intervals)):
            s, e = intervals[i]

            if end < s:
                res.append([start, end])
                start = s
                end = e
            else:
                end = max(e, end)

        res.append([start, end])
        return res