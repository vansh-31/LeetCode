# Problem : Unique Number of Occurrences
# Problem Statement : Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.
from collections import defaultdict


class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        d = defaultdict(int)
        for num in arr:
            d[num] += 1
        return len(d.values()) == len(set(d.values()))
