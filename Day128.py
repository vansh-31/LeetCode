# Problem : Matrix Diagonal Sum
# Problem Statement : Given a square matrix mat, return the sum of the matrix diagonals.
# Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.
class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        ans = 0
        n = len(mat)
        for i in range(n//2):
            ans += mat[i][i] + mat[i][ n - i - 1 ] + mat[ n - i - 1 ][i] + mat[ n - i - 1 ][ n - i - 1 ]
        if n%2 == 1:
            ans += mat[n//2][n//2]
        return ans