# Problem : Subsets
# Problem Statement : Given an integer array nums of unique elements, return all possible subsets (the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        ans = set()

        def solve(i, curr):
            if i == len(nums):
                ans.add(tuple(curr[:]))
                return
            curr.append(nums[i])
            solve(i + 1, curr)
            curr.pop()
            solve(i + 1, curr)

        solve(0, [])
        return [list(x) for x in ans]
