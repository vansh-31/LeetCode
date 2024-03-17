# Problem : Find First and Last Position of Element in Sorted Array
# Problem Statement : Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
# If target is not found in the array, return [-1, -1].
# You must write an algorithm with O(log n) runtime complexity.
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        def firstOcc(target):
            low, high = 0, n - 1
            ans = -1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    ans = mid
                    high = mid - 1
                elif nums[mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1
            return ans

        def lastOcc(target):
            low, high = 0, n - 1
            ans = -1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    ans = mid
                    low = mid + 1
                elif nums[mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1
            return ans

        return [firstOcc(target), lastOcc(target)]
