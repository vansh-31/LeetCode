# Problem : Reducing Dishes
# Problem Statement : A chef has collected data on the satisfaction level of his n dishes. Chef can cook any dish in 1 unit of time.
# Like-time coefficient of a dish is defined as the time taken to cook that dish including previous dishes multiplied by its satisfaction level i.e. time[i] * satisfaction[i].
# Return the maximum sum of like-time coefficient that the chef can obtain after dishes preparation.
# Dishes can be prepared in any order and the chef can discard some dishes to get this maximum value.
class Solution:
    def maxSatisfaction(self, sat: list[int]) -> int:
        n = len(sat)
        sat.sort()
        dp = [[-1 for x in range(n+1)] for y in range(n+1)]
        def solve(i,time):
            if i >= n:
                return 0
            if dp[i][time]!=-1:
                return dp[i][time]

            take = time*sat[i] + solve(i+1,time+1)
            not_take = solve(i+1,time)
            dp[i][time] = max(take,not_take)
            return dp[i][time]
        return solve(0,1)