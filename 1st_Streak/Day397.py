# Problem : Divide Array Into Arrays With Max Difference
# Problem Statement : You are given an integer array nums of size n and a positive integer k.
# Divide the array into one or more arrays of size 3 satisfying the following conditions:
# Each element of nums should be in exactly one array.
# The difference between any two elements in one array is less than or equal to k.
# Return a 2D array containing all the arrays. If it is impossible to satisfy the conditions, return an empty array. And if there are multiple answers, return any of them.
class Solution:
    def divideArray(self, nums: list[int], k: int) -> list[list[int]]:
        nums.sort()
        lis=[]
        for i in range(0,len(nums)-2,3):
            if nums[i+2]-nums[i]<=k:
                lis.extend([[nums[i],nums[i+1],nums[i+2]]])
        return lis if len(lis)==len(nums)//3 else []