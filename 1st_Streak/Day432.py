# Problem : Count Elements With Maximum Frequency
# Problem Statement : You are given an array nums consisting of positive integers.
# Return the total frequencies of elements in nums such that those elements all have the maximum frequency.
# The frequency of an element is the number of occurrences of that element in the array.
from collections import Counter
from typing import List


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        c = Counter(nums)
        li = [i for i in c.values()]
        m, res = max(li), 0
        for i in li:
            if i == m:
                res += i
        return res
