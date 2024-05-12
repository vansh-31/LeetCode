# Problem : Largest Local Values in a Matrix
# Problem Statement : You are given an n x n integer matrix grid.
# Generate an integer matrix maxLocal of size (n - 2) x (n - 2) such that:
# maxLocal[i][j] is equal to the largest value of the 3 x 3 matrix in grid centered around row i + 1 and column j + 1.
# In other words, we want to find the largest value in every contiguous 3 x 3 matrix in grid.
# Return the generated matrix.
class Solution:
    def largestLocal(self, grid: list[list[int]]) -> list[list[int]]:
        res = []
        n = len(grid)
        for i in range(n - 2):
            res.append([])
            for j in range(n - 2):
                max_val = max(
                    grid[i][j : j + 3] + grid[i + 1][j : j + 3] + grid[i + 2][j : j + 3]
                )
                res[-1].append(max_val)
        return res
