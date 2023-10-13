# Problem : Min Cost Climbing Stairs
# Problem Statement : You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.
# You can either start from the step with index 0, or the step with index 1.
# Return the minimum cost to reach the top of the floor.
class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n = len(cost)
        dp = [0] * (n+2)
        for index in range(n-1,-1,-1):
            dp[index] = cost[index] + min(dp[index+1],dp[index+2])
        return min(dp[0],dp[1])