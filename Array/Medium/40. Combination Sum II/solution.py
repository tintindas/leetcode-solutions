from typing import List


class Solution:
    def helper(self, candidates, path, target, idx):
        if target == 0:
            self.res.append(path)
            return

        if target < 0 or idx > len(candidates) - 1:
            return

        for i in range(idx, len(candidates)):
            if i > idx and candidates[i] == candidates[i - 1]:
                continue
            self.helper(candidates, path + [candidates[i]], target - candidates[i], i + 1)

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        candidates.sort()
        self.res = []
        self.helper(candidates, [], target, 0)
        return self.res