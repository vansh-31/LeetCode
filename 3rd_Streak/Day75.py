# Problem : Continuous Subarray Sum
# Problem Statement : Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.
# A good subarray is a subarray where:
# its length is at least two, and
# the sum of the elements of the subarray is a multiple of k.
# Note that:
# A subarray is a contiguous part of the array.
# An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.
class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        n = len(nums)
        if n < 2:
            return False
        mod_k = {}
        prefix = 0
        mod_k[0] = -1
        for i, x in enumerate(nums):
            prefix += x
            prefix %= k
            print(mod_k)
            if prefix in mod_k:
                if i > mod_k[prefix] + 1:
                    return True
            else:
                mod_k[prefix] = i
        return False
