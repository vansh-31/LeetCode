# Problem : Sort Array by Increasing Frequency
# Problem Statement : Given an array of integers nums, sort the array in increasing order based on the frequency of the values. If multiple values have the same frequency, sort them in decreasing order.
# Return the sorted array.
from typing import List
from collections import Counter


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        return sorted(nums, key=lambda x: (freq[x], -x))
