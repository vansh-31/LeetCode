# Problem : The Number of Beautiful Subsets
# Problem Statement : You are given an array nums of positive integers and a positive integer k.
# A subset of nums is beautiful if it does not contain two integers with an absolute difference equal to k.
# Return the number of non-empty beautiful subsets of the array nums.
# A subset of nums is an array that can be obtained by deleting some (possibly none) elements from nums. Two subsets are different if and only if the chosen indices to delete are different.
class Solution:
    def beautifulSubsets(self, nums: list[int], k: int) -> int:
        def solve(start, current_subset):
            nonlocal count
            if current_subset:
                count += 1
            for i in range(start, len(nums)):
                can_add = True
                for num in current_subset:
                    if abs(num - nums[i]) == k:
                        can_add = False
                        break
                if can_add:
                    current_subset.append(nums[i])
                    solve(i + 1, current_subset)
                    current_subset.pop()

        nums.sort()
        count = 0
        solve(0, [])
        return count
