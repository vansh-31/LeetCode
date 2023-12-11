# Problem : Element Appearing More Than 25% In Sorted Array
# Problem Statement : Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time, return that integer.
class Solution:
    def findSpecialInteger(self, arr: list[int]) -> int:
        n = len(arr)
        ans =  arr[0]
        count = 0
        for x in arr:
            if x != ans:
                ans = x
                count = 1
            else:
                count += 1
            if count > n/4:
                return ans
        return -1