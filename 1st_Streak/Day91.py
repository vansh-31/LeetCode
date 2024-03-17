# Problem : Binary Search
# Problem : Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
# You must write an algorithm with O(log n) runtime complexity.
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        st,end = 0,len(nums)-1
        while st <= end:
            mid = (st+end)//2
            if nums[mid]==target:
                return mid
            if nums[mid] < target:
                st = mid+1
            else:
                end = mid-1
        return -1