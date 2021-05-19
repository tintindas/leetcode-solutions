from typing import List
from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(p)
        pattern = Counter(p)
        window = Counter(s[:n])

        res = []
        flag = True

        for key, val in window.items():
            if val != pattern[key]:
                flag = False
                break

        if flag:
            res.append(0)

        for idx in range(n, len(s)):
            c = s[idx]
            prev = s[idx - n]

            window[prev] -= 1
            if window[prev] == 0:
                window.pop(prev)

            if c in window:
                window[c] += 1
            else:
                window[c] = 1

            if pattern == window:
                res.append(idx - n + 1)

        return res
