# Problem : Minimum Difference Between Largest and Smallest Value in Three Moves
# Problem Statement : You are given an integer array nums.
# In one move, you can choose one element of nums and change it to any value.
# Return the minimum difference between the largest and smallest value of nums after performing at most three moves.
class Solution:
    def minDifference(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 4:
            return 0
        nums.sort()
        case1 = abs(nums[3] - nums[-1])
        case2 = abs(nums[2] - nums[-2])
        case3 = abs(nums[1] - nums[-3])
        case4 = abs(nums[0] - nums[-4])
        return min(case1, case2, case3, case4)
