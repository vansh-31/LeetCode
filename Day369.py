# Problem : Minimum Number of Operations to Make Array Empty
# Problem Statement : You are given a 0-indexed array nums consisting of positive integers.
# There are two types of operations that you can apply on the array any number of times:
# Choose two elements with equal values and delete them from the array.
# Choose three elements with equal values and delete them from the array.
# Return the minimum number of operations required to make the array empty, or -1 if it is not possible.
from collections import defaultdict
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        ans = 0
        for x in freq.values():
            while x:
                if x == 1:
                    return -1
                if 2 <= x <= 3:
                    ans += 1
                    break
                elif 4 <= x <= 6:
                    ans += 2
                    break
                x -= 3
                ans += 1
        return ans
