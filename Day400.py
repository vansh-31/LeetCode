# Problem : Minimum Window Substring
# Problem Statement : Given two strings s and t of lengths m and n respectively, return the minimum window
# substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".
# The testcases will be generated such that the answer is unique.
from collections import defaultdict, deque


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count = defaultdict(int)
        window_count = defaultdict(int)
        for ch in t:
            t_count[ch] += 1
        have, need = 0, len(t_count)
        start = -1
        res, resLen = [-1, -1], float("inf")
        q = deque()
        for end, ch in enumerate(s):
            if ch not in t_count:
                continue
            if start == -1:
                start = end
            window_count[ch] += 1
            q.append(end)
            if window_count[ch] == t_count[ch]:
                have += 1
            while have == need:
                if (end - start + 1) < resLen:
                    res = [start, end]
                    resLen = end - start + 1
                window_count[s[start]] -= 1
                q.popleft()
                if window_count[s[start]] < t_count[s[start]]:
                    have -= 1
                if q:
                    start = q[0]
                else:
                    start = -1
        return "" if res[0] == -1 else s[res[0] : res[1] + 1]
