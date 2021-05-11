from typing import List


class Solution:
    def helper(self, target, wordDict):
        if target in self.memo:
            return self.memo[target]

        if not target:
            return [[]]

        total_ways = []
        for word in wordDict:
            if target.find(word) == 0:
                remainder = target[len(word) :]
                remainder_ways = self.helper(remainder, wordDict)
                word_ways = [[word] + way for way in remainder_ways]
                total_ways.extend(word_ways)

        self.memo[target] = total_ways
        return total_ways

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        self.memo = {}
        ans = self.helper(s, wordDict)
        return [" ".join(l) for l in ans]
