# Problem : Count Nice Pairs in an Array
# Problem Statement : You are given an array nums that consists of non-negative integers. Let us define rev(x) as the reverse of the non-negative integer x. For example, rev(123) = 321, and rev(120) = 21. A pair of indices (i, j) is nice if it satisfies all of the following conditions:
# 0 <= i < j < nums.length
# nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])
# Return the number of nice pairs of indices. Since that number can be too large, return it modulo 109 + 7.
from typing import List
from collections import defaultdict


class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        mod = 10**9 + 7

        def rev(x):
            x = str(x)
            x = x[::-1]
            x = x.lstrip("0")
            if len(x) == 0:
                return 0
            return int(x)

        total_number, total_count = defaultdict(int), 0
        for num in nums:
            rev_num = num - rev(num)
            total_count += total_number[rev_num]
            total_number[rev_num] += 1
        return total_count % mod
