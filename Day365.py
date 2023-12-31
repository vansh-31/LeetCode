# Problem : Largest Substring Between Two Equal Characters
# Problem Statement : Given a string s, return the length of the longest substring between two equal characters, excluding the two characters. If there is no such substring return -1.
# A substring is a contiguous sequence of characters within a string.
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        n = len(s)
        ans = -1
        for i in range(n):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    ans = max(ans, j - i - 1)
        return ans
