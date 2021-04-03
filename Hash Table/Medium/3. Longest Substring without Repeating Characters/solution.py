class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        window = {}
        start = end = 0
        max_len = 0

        while end < len(s):
            if s[end] not in window:
                window[s[end]] = 1
                end += 1
                max_len = max(max_len, len(window))
            else:
                del window[s[start]]
                start += 1

        return max_len
