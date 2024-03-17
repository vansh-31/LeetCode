# Problem : Permutations
# Problem Statement : Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []
        def solve(index):
            if index >= len(nums):
                res.append(nums[:])
                return
            for i in range(index, len(nums)):
                nums[index],nums[i] = nums[i],nums[index]
                solve(index+1)
                nums[index],nums[i] = nums[i],nums[index]
        solve(0)
        return res