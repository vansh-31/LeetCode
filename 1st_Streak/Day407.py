# Problem : Cherry Pickup II
# Problem Statement : You are given a rows x cols matrix grid representing a field of cherries where grid[i][j] represents the number of cherries that you can collect from the (i, j) cell.
# You have two robots that can collect cherries for you:
# Robot #1 is located at the top-left corner (0, 0), and
# Robot #2 is located at the top-right corner (0, cols - 1).
# Return the maximum number of cherries collection using both robots by following the rules below:
# From a cell (i, j), robots can move to cell (i + 1, j - 1), (i + 1, j), or (i + 1, j + 1).
# When any robot passes through a cell, It picks up all cherries, and the cell becomes an empty cell.
# When both robots stay in the same cell, only one takes the cherries.
# Both robots cannot move outside of the grid at any moment.
# Both robots should reach the bottom row in grid.
from typing import List
from functools import cache


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        steps = [(1, -1), (1, 0), (1, 1)]

        @cache
        def solve(r1, r2):
            if r1[0] == n and r2[0] == n:
                return 0
            if r1[1] < 0 or r1[1] >= m or r2[1] < 0 or r2[1] >= m:
                return -float("inf")
            ans = 0
            if r1 == r2:
                ans = grid[r1[0]][r1[1]]
            else:
                ans = grid[r1[0]][r1[1]] + grid[r2[0]][r2[1]]
            temp = 0
            for x in steps:
                for y in steps:
                    temp = max(
                        temp,
                        solve(
                            (r1[0] + x[0], r1[1] + x[1]), (r2[0] + y[0], r2[1] + y[1])
                        ),
                    )
            return ans + temp

        return solve((0, 0), (0, m - 1))  # type: ignore
