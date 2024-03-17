# Problem : Painting the Walls
# Problem Statement : You are given two 0-indexed integer arrays, cost and time, of size n representing the costs and the time taken to paint n different walls respectively. There are two painters available:
# A paid painter that paints the ith wall in time[i] units of time and takes cost[i] units of money.
# A free painter that paints any wall in 1 unit of time at a cost of 0. But the free painter can only be used if the paid painter is already occupied.
# Return the minimum amount of money required to paint the n walls.
from typing import List
class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)
        dp = {}
        def solve(index,t):
            if index == n:
                return 0 if t >= 0 else float("inf")
            if t >= n - index:
                return 0
            if (index,t) in dp:
                return dp[(index,t)]
            free_painter = solve(index+1,t-1)
            paid_painter = cost[index] + solve(index+1, t + time[index] )
            dp[(index,t)] = min(free_painter,paid_painter)
            return dp[ (index,t)  ]
        return solve(0,0) # type: ignore