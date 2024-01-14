# Problem : Determine if Two Strings Are Close
# Problem Statement : Two strings are considered close if you can attain one from the other using the following operations:
# Operation 1: Swap any two existing characters.
# For example, abcde -> aecdb
# Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
# For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
# You can use the operations on either string as many times as necessary.
# Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.
from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        count1 = Counter(word1)
        count2 = Counter(word2)
        condition1 = sorted(count1.keys()) == sorted(count2.keys())
        condition2 = sorted(count1.values()) == sorted(count2.values())
        return condition1 and condition2
