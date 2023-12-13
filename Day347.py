# Problem : Special Positions in a Binary Matrix
# Problem Statement : Given an m x n binary matrix mat, return the number of special positions in mat.
# A position (i, j) is called special if mat[i][j] == 1 and all other elements in row i and column j are 0 (rows and columns are 0-indexed).
class Solution:
    def numSpecial(self, mat: list[list[int]]) -> int:
        result = 0
        row_sums = [0] * len(mat)
        col_sums = [0] * len(mat[0])
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                row_sums[i] += mat[i][j]
                col_sums[j] += mat[i][j]
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j] == 1 and row_sums[i] == 1 and col_sums[j] == 1:
                    result += 1
        return result
