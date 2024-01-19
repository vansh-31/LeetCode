# Problem : Minimum Falling Path Sum
# Problem Statement : Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.
# A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).
from functools import cache
from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])

        @cache
        def solve(row, col):
            if col >= m or col < 0:
                return float("inf")
            if row == n:
                return 0
            left = solve(row + 1, col - 1)
            center = solve(row + 1, col)
            right = solve(row + 1, col + 1)
            ans = matrix[row][col] + min([left, center, right])
            return ans

        ans = float("inf")
        for i in range(n):
            ans = min(ans, solve(0, i))
        return ans
