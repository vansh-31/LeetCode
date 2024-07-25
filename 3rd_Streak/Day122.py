# Problem : Sort an Array
# Problem Statement : Given an array of integers nums, sort the array in ascending order and return it.
# You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.
from typing import List
from random import randint


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        flag = True

        def partition(arr, low, high):
            nonlocal flag
            pivot = arr[low + (high - low) // 2]
            if flag:
                pivot = arr[randint(low, high)]
            flag ^= True
            left = low
            right = high
            while left <= right:
                while arr[left] < pivot:
                    left += 1
                while arr[right] > pivot:
                    right -= 1
                if left <= right:
                    arr[left], arr[right] = arr[right], arr[left]
                    left += 1
                    right -= 1
            return left, right

        def quickSort(arr, low, high):
            if low < high:
                mid_left, mid_right = partition(arr, low, high)
                quickSort(arr, low, mid_right)
                quickSort(arr, mid_left, high)
            return arr

        return quickSort(nums, 0, len(nums) - 1)
