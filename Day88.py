# Problem : Reducing Dishes
# Problem Statement : A chef has collected data on the satisfaction level of his n dishes. Chef can cook any dish in 1 unit of time.
# Like-time coefficient of a dish is defined as the time taken to cook that dish including previous dishes multiplied by its satisfaction level i.e. time[i] * satisfaction[i].
# Return the maximum sum of like-time coefficient that the chef can obtain after dishes preparation.
# Dishes can be prepared in any order and the chef can discard some dishes to get this maximum value.
class Solution:
    def maxSatisfaction(self, sat: List[int]) -> int:
        n = len(sat)
        sat.sort()
        dp = [[0 for x in range(n+2)] for y in range(n+2)]
        for i in range(n-1,-1,-1):
            for time in range(n,0,-1):
                take = time*sat[i] + dp[i+1][time+1]
                not_take = dp[i+1][time]
                dp[i][time] = max(take,not_take)
        return dp[0][1]