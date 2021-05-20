from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        counts = Counter(s)
        ans = ""
        for c, count in counts.most_common():
            ans += c * count
        return ans