# Problem : Number of Increasing Paths in a Grid
# Problem Statement : You are given an m x n integer matrix grid, where you can move from a cell to any adjacent cell in all 4 directions.
# Return the number of strictly increasing paths in the grid such that you can start from any cell and end at any cell. Since the answer may be very large, return it modulo 109 + 7.
# Two paths are considered different if they do not have exactly the same sequence of visited cells.
from functools import lru_cache
class Solution:
    def countPaths(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        mod = 10 ** 9 + 7
        @lru_cache(None)
        def count(row, col):
            res = 1
            for dx, dy in [[row, col + 1], [row, col - 1], [row + 1, col], [row - 1, col]]:
                if 0 <= dx < rows and 0 <= dy < cols and grid[dx][dy] > grid[row][col]:
                    res += count(dx, dy) % mod
            return res
        ans = 0
        for i in range(rows):
            for j in range(cols):
                ans += count(i, j)
        return ans % mod