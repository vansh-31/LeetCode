# Problem : Difference Between Ones and Zeros in Row and Column
# Problem Statement : You are given a 0-indexed m x n binary matrix grid.
# A 0-indexed m x n difference matrix diff is created with the following procedure:
# Let the number of ones in the ith row be onesRowi.
# Let the number of ones in the jth column be onesColj.
# Let the number of zeros in the ith row be zerosRowi.
# Let the number of zeros in the jth column be zerosColj.
# diff[i][j] = onesRowi + onesColj - zerosRowi - zerosColj
# Return the difference matrix diff.
class Solution:
    def onesMinusZeros(self, grid: list[list[int]]) -> list[list[int]]:
        m = len(grid)
        n = len(grid[0])
        diff = [[0] * n for _ in range(m)]
        r = [sum(i) for i in grid]
        c = [sum(k[i] for k in grid) for i in range(n)]
        x = m + n
        for i in range(m):
            for j in range(n):
                diff[i][j] = 2 * (r[i] + c[j]) - x
        return diff
