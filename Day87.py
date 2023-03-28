# Problem : Minimum Cost For Tickets
# Problem Statement : You have planned some train traveling one year in advance. The days of the year in which you will travel are given as an integer array days. Each day is an integer from 1 to 365.

# Train tickets are sold in three different ways:

# a 1-day pass is sold for costs[0] dollars,
# a 7-day pass is sold for costs[1] dollars, and
# a 30-day pass is sold for costs[2] dollars.
# The passes allow that many days of consecutive travel.

# For example, if we get a 7-day pass on day 2, then we can travel for 7 days: 2, 3, 4, 5, 6, 7, and 8.
# Return the minimum number of dollars you need to travel every day in the given list of days.
class Solution:
    def mincostTickets(self, days: list[int], costs: list[int]) -> int:
        n = len(days)
        dp = [-1 for x in range(n+1)]
        def solve(i):
            if i >= n:
                return 0
            if dp[i] != -1:
                return dp[i]
            one_day = costs[0] + solve(i+1)
            index = i

            while index < n and days[index] < days[i]+7:
                index+=1
            one_week = costs[1] + solve(index)

            while index < n and days[index] < days[i]+30:
                index+=1
            one_month = costs[2] + solve(index)
            dp[i] = min(one_day,one_week,one_month)
            return dp[i]

        return solve(0)