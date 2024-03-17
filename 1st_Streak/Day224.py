# Problem : Unique Paths II
# Problem Statement : You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.
# An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.
# Return the number of possible unique paths that the robot can take to reach the bottom-right corner.
# The testcases are generated so that the answer will be less than or equal to 2 * 109.
from functools import cache
from typing import List
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m,n = len(obstacleGrid),len(obstacleGrid[0])
        @cache
        def solve(row,col):
            if row == m or col == n or obstacleGrid[row][col] == 1:
                return 0
            if row == m-1 and col == n-1:
                return 1
            ans = 0
            # Down
            ans += solve(row+1,col)
            # Right
            ans += solve(row,col+1)
            return ans
        return solve(0,0)