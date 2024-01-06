# Problem : Maximum Profit in Job Scheduling
# Problem Statement : We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining a profit of profit[i].
# You're given the startTime, endTime and profit arrays, return the maximum profit you can take such that there are no two jobs in the subset with overlapping time range.
# If you choose a job that ends at time X you will be able to start another job that starts at time X.
class Solution:
    def jobScheduling(self, startTime: list[int], endTime: list[int], profit: list[int]) -> int:
        schedule = sorted(list(zip(startTime,endTime,profit)))
        dp = {}
        def dfs(last_end,i):
            if i == len(schedule):
                return 0
            if schedule[i][0] < last_end:
                return dfs(last_end,i+1)
            if i in dp:
                return dp[i]

            take = schedule[i][2] + dfs(schedule[i][1],i+1)
            not_take = dfs(last_end,i+1)
            dp[i] = max(take,not_take)
            return dp[i]

        return dfs(0,0)