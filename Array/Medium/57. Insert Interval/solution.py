from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        left = []
        right = []
        new_start, new_end = newInterval

        for interval in intervals:
            cur_start, cur_end = interval

            if cur_end < new_start:
                left.append(interval)

            elif cur_start > new_end:
                right.append(interval)

            else:
                new_start = min(new_start, cur_start)
                new_end = max(new_end, cur_end)

        return left + [[new_start, new_end]] + right