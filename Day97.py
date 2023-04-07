# Problem : Number of Enclaves
# Problem Statement : You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.

# A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid.

# Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.
class Solution:
    def numEnclaves(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        def dfs(i, j):
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] != 1:
                return
            grid[i][j] = 0
            dfs(i-1, j)
            dfs(i+1,j)
            dfs(i,j-1)
            dfs(i,j+1)
            
        for i in range(m):
            if grid[i][0]==1:
                dfs(i,0)
            if grid[i][n-1]==1:
                dfs(i,n-1)
        for j in range(n):
            if grid[0][j]==1:
                dfs(0,j)
            if grid[m-1][j]==1:
                dfs(m-1,j)
        return sum(sum(row) for row in grid)