# Problem : Minimum Difficulty of a Job Schedule
# Problem Statement : You want to schedule a list of jobs in d days. Jobs are dependent (i.e To work on the ith job, you have to finish all the jobs j where 0 <= j < i).
# You have to finish at least one task every day. The difficulty of a job schedule is the sum of difficulties of each day of the d days. The difficulty of a day is the maximum difficulty of a job done on that day.
# You are given an integer array jobDifficulty and an integer d. The difficulty of the ith job is jobDifficulty[i].
# Return the minimum difficulty of a job schedule. If you cannot find a schedule for the jobs return -1.
from functools import cache
from typing import List


class Solution:
    def minDifficulty(self, nums: List[int], d: int) -> int:
        N = len(nums)
        if d > N:
            return -1

        @cache
        def dfs(i, cuts):
            if cuts == d - 1:
                return max(nums[i:])
            ans = 10**9
            max_v = -1
            for j in range(i, N - (d - cuts - 1)):
                max_v = max(max_v, nums[j])
                ans = min(ans, dfs(j + 1, cuts + 1) + max_v)
            return ans

        return dfs(0, 0)
