# Problem : Rearrange Array Elements by Sign
# Problem Statement : You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and negative integers.
# You should rearrange the elements of nums such that the modified array follows the given conditions:
# Every consecutive pair of integers have opposite signs.
# For all integers with the same sign, the order in which they were present in nums is preserved.
# The rearranged array begins with a positive integer.
# Return the modified array after rearranging the elements to satisfy the aforementioned conditions.
class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        negatives = [i for i in nums if i < 0]
        positives = [i for i in nums if i >= 0]
        for index, position in enumerate(range(0, len(nums), 2)):
            nums[position] = positives[index]
            nums[position + 1] = negatives[index]
        return nums
