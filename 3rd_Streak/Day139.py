# Problem : Minimum Number of Days to Disconnect Island
# Problem Statement : You are given an m x n binary grid grid where 1 represents land and 0 represents water. An island is a maximal 4-directionally (horizontal or vertical) connected group of 1's.
# The grid is said to be connected if we have exactly one island, otherwise is said disconnected.
# In one day, we are allowed to change any single land cell (1) into a water cell (0).
# Return the minimum number of days to disconnect the grid.
class Solution:
    def minDays(self, grid: list[list[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        def count(grid):
            vis = [[False] * m for i in range(n)]

            def isValid(i, j):
                if i < 0 or i >= n or j < 0 or j >= m or vis[i][j] or not grid[i][j]:
                    return False
                return True

            def dfs(i, j):
                if isValid(i, j):
                    vis[i][j] = True
                    dfs(i + 1, j)
                    dfs(i - 1, j)
                    dfs(i, j + 1)
                    dfs(i, j - 1)

            cnt = 0
            for i in range(n):
                for j in range(m):
                    if grid[i][j] and not vis[i][j]:
                        cnt += 1
                        dfs(i, j)
            return cnt

        islands = count(grid)
        if islands != 1:
            return 0
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    grid[i][j] = 0
                    islands = count(grid)
                    if islands != 1:
                        return 1
                    grid[i][j] = 1
        return 2
