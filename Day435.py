# Problem : Custom Sort String
# Problem Statement : You are given two strings order and s. All the characters of order are unique and were sorted in some custom order previously.
# Permute the characters of s so that they match the order that order was sorted. More specifically, if a character x occurs before a character y in order, then x should occur before y in the permuted string.
# Return any permutation of s that satisfies this property.
from collections import Counter


class Solution:
    def customSortString(self, order: str, s: str) -> str:

        ctr = Counter(s)

        ans = [ch * ctr[ch] for ch in order]

        ans.extend(filter(lambda x: x not in order, s))

        return "".join(ans)
