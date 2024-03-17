# Problem : Minimum Number of Steps to Make Two Strings Anagram
# Problem Statement : You are given two strings of the same length s and t. In one step you can choose any character of t and replace it with another character.
# Return the minimum number of steps to make t an anagram of s.
# An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.
from collections import Counter


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count_s = Counter(s)
        count_t = Counter(t)
        total_steps = sum((count_s - count_t).values())
        return total_steps
