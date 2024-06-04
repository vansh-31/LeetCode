# Problem : Longest Palindrome
# Problem Statement : Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.Letters are case sensitive, for example, "Aa" is not considered a palindrome.
from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        ans = odd = 0
        for cnt in count.values():
            if cnt & 1:
                ans += (cnt // 2) * 2
                odd = 1
            else:
                ans += cnt
        return ans + odd
