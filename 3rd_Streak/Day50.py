# Problem : Path with Maximum Gold
# Problem Statement : In a gold mine grid of size m x n, each cell in this mine has an integer representing the amount of gold in that cell, 0 if it is empty.
# Return the maximum amount of gold you can collect under the conditions:
# Every time you are located in a cell you will collect all the gold in that cell.
# From your position, you can walk one step to the left, right, up, or down.
# You can't visit the same cell more than once.
# Never visit a cell with 0 gold.
# You can start and stop collecting gold from any position in the grid that has some gold.
class Solution:
    def getMaximumGold(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        vis = [[False for _ in range(n)] for _ in range(m)]

        def Possible(x, y):
            return (
                (0 <= x < m) and (0 <= y < n) and (not vis[x][y]) and (grid[x][y] != 0)
            )

        def solve(x, y):
            if not Possible(x, y):
                return 0
            vis[x][y] = True
            up = solve(x - 1, y)
            down = solve(x + 1, y)
            left = solve(x, y - 1)
            right = solve(x, y + 1)
            vis[x][y] = False
            return grid[x][y] + max([up, down, left, right])

        ans = 0
        for x in range(m):
            for y in range(n):
                ans = max(ans, solve(x, y))
        return ans
