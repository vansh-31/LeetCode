# Problem : Minimum Swaps to Group All 1's Together II
# Problem Statement : A swap is defined as taking two distinct positions in an array and swapping the values in them.
# A circular array is defined as an array where we consider the first element and the last element to be adjacent.
# Given a binary circular array nums, return the minimum number of swaps required to group all 1's present in the array together at any location.
class Solution:
    def minSwaps(self, nums: list[int]) -> int:
        n = len(nums)
        k = sum(nums)
        if k == 0 or k == n:
            return 0
        extended_nums = nums + nums[: k - 1]
        current_zeros = sum(1 for i in range(k) if extended_nums[i] == 0)
        min_zeros = current_zeros

        for i in range(1, n):
            if extended_nums[i - 1] == 0:
                current_zeros -= 1
            if extended_nums[i + k - 1] == 0:
                current_zeros += 1
            min_zeros = min(min_zeros, current_zeros)
        return min_zeros
