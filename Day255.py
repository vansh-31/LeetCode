# Problem : Minimum Deletions to Make Character Frequencies Unique
# Problem Statement : A string s is called good if there are no two different characters in s that have the same frequency.
# Given a string s, return the minimum number of characters you need to delete to make s good.
# The frequency of a character in a string is the number of times it appears in the string. For example, in the string "aab", the frequency of 'a' is 2, while the frequency of 'b' is 1.
from collections import defaultdict


class Solution:
    def minDeletions(self, s: str) -> int:
        freq = defaultdict(int)
        for x in s:
            freq[x] += 1
        freq = [x for x in freq.values()]
        freq.sort()
        ans = 0
        j = len(freq) - 1
        i = j - 1
        while i >= 0:
            while i >= 0 and (freq[i] == 0 or freq[i] < freq[j]):
                i -= 1
                j -= 1
            if i < 0:
                break
            temp = freq[i]
            freq[i] = max(0, freq[j] - 1)
            ans += temp - freq[i]
        return ans
