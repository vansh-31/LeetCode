# Problem : Relative Sort Array
# Problem Statement : Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.
# Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2. Elements that do not appear in arr2 should be placed at the end of arr1 in ascending order.
class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        freq = [0] * (max(arr1) + 1)
        for num in arr1:
            freq[num] += 1
        i = 0
        for num in arr2:
            while freq[num]:
                arr1[i] = num
                freq[num] -= 1
                i += 1
        for j, num in enumerate(freq):
            while num:
                arr1[i] = j
                num -= 1
                i += 1
        return arr1
