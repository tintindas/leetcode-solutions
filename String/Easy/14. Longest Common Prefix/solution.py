from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        idx = -1
        for j in range(len(strs[0])):
            c = strs[0][j]
            for i in range(1, len(strs)):
                if j == len(strs[i]) or strs[i][j] != c:
                    return strs[0][: idx + 1]
            idx = j

        return strs[0]
