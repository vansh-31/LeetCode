# Problem : Minimum Path Sum
# Problem Statement : Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.
# Note: You can only move either down or right at any point in time.
class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        if m == 1:
            return sum(grid[0])
        if n == 1:
            ans = 0
            for l in grid:
                ans += l[0]
            return ans
        dp = [[-1 for x in range(m+1)] for y in range(n+1)]
        def solve(i,j):
            nonlocal dp
            if i == m-1 and j == n-1:
                return grid[i][j]
            if i >= m or j >= n:
                return 1000
            if i < m and j < n and dp[i][j]!=-1:
                return dp[i][j]
            right = solve(i,j+1)
            down = solve(i+1,j)
            dp[i][j] = grid[i][j] + min(right,down)
            return dp[i][j]
        return solve(0,0)