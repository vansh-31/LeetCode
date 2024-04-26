# Problem : Minimum Falling Path Sum II
# Problem Statement : Given an n x n integer matrix grid, return the minimum sum of a falling path with non-zero shifts.
# A falling path with non-zero shifts is a choice of exactly one element from each row of grid such that no two elements chosen in adjacent rows are in the same column.
class Solution:
    def minFallingPathSum(self, grid):
        self.n = len(grid)
        self.memo = [[-1] * (self.n + 1) for _ in range(self.n + 1)]
        min_sum = float("inf")
        for col in range(self.n):
            min_sum = min(min_sum, self.dfs(grid, 0, col))
        return min_sum

    def dfs(self, grid, r, c):
        if c >= self.n or c < 0:
            return 100000
        if r == self.n - 1:
            return grid[r][c]
        if self.memo[r][c] != -1:
            return self.memo[r][c]
        ans = float("inf")
        for i in range(self.n):
            if i != c:
                ans = min(ans, grid[r][c] + self.dfs(grid, r + 1, i))
        self.memo[r][c] = ans
        return ans
