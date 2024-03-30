# Problem : Subarrays with K Different Integers
# Problem Statement : Given an integer array nums and an integer k, return the number of good subarrays of nums.
# A good array is an array where the number of different integers in that array is exactly k.
# For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
# A subarray is a contiguous part of an array.
from collections import defaultdict


class Solution:
    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        def atMostK(nums, k):
            counter = defaultdict(int)
            distinct = 0
            left = 0
            result = 0
            for right in range(len(nums)):
                if counter[nums[right]] == 0:
                    distinct += 1
                counter[nums[right]] += 1
                while distinct > k:
                    counter[nums[left]] -= 1
                    if counter[nums[left]] == 0:
                        distinct -= 1
                    left += 1
                result += right - left + 1
            return result

        return atMostK(nums, k) - atMostK(nums, k - 1)
