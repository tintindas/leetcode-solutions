class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        window = set()
        start = end = 0
        max_len = 0

        while end < len(s):
            if s[end] not in window:
                window.add(s[end])
                end += 1
                max_len = max(max_len, len(window))
            else:
                window.remove(s[start])
                start += 1

        return max_len
