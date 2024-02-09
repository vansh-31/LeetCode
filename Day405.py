# Problem : Largest Divisible Subset
# Problem Statement : Given a set of distinct positive integers nums, return the largest subset answer such that every pair (answer[i], answer[j]) of elements in this subset satisfies:
# answer[i] % answer[j] == 0, or
# answer[j] % answer[i] == 0
# If there are multiple solutions, return any of them.
class Solution:
    def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        def dfs(i, prevInd):
            nonlocal n
            if i >= n:
                return []
            if (i, prevInd) in memo:
                return memo[(i, prevInd)]
            skip = dfs(i + 1, prevInd)
            take = []
            if prevInd == -1:
                take = [nums[i]] + dfs(i + 1, i)
            elif prevInd != -1 and nums[i] % nums[prevInd] == 0:
                take = [nums[i]] + dfs(i + 1, i)
            memo[(i, prevInd)] = max(skip, take, key=len)
            return memo[(i, prevInd)]

        n = len(nums)
        nums = sorted(nums)
        memo = dict()
        return dfs(0, -1)
