# Problem : Find in Mountain Array
# Problem Statement : (This problem is an interactive problem.)
# You may recall that an array arr is a mountain array if and only if:
# arr.length >= 3
# There exists some i with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
# Given a mountain array mountainArr, return the minimum index such that mountainArr.get(index) == target. If such an index does not exist, return -1.
# You cannot access the mountain array directly. You may only access the array using a MountainArray interface:
# MountainArray.get(k) returns the element of the array at index k (0-indexed).
# MountainArray.length() returns the length of the array.
# Submissions making more than 100 calls to MountainArray.get will be judged Wrong Answer. Also, any solutions that attempt to circumvent the judge will result in disqualification.
# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        def find_peak(mountain_arr):
            left, right = 0, mountain_arr.length() - 1
            while left < right:
                mid = left + (right - left) // 2
                if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                    left = mid + 1
                else:
                    right = mid
            return left

        def binary_search(left, right, is_increasing):
            while left <= right:
                mid = left + (right - left) // 2
                mid_val = mountain_arr.get(mid)
                if mid_val == target:
                    return mid
                if mid_val < target:
                    if is_increasing:
                        left = mid + 1
                    else:
                        right = mid - 1
                else:
                    if is_increasing:
                        right = mid - 1
                    else:
                        left = mid + 1
            return -1

        peak_index = find_peak(mountain_arr)
        result = binary_search(0, peak_index, True)
        if result == -1:
            result = binary_search(peak_index + 1, mountain_arr.length() - 1, False)
        return result