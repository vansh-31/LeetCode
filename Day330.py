# Problem : Largest Submatrix With Rearrangements
# Problem Statement : You are given a binary matrix matrix of size m x n, and you are allowed to rearrange the columns of the matrix in any order.
# Return the area of the largest submatrix within matrix where every element of the submatrix is 1 after reordering the columns optimally.
from typing import List


class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m, n, ans = len(matrix), len(matrix[0]), 0

        for j in range(n):
            for i in range(1, m):
                matrix[i][j] += matrix[i - 1][j] if matrix[i][j] else 0

        for i in range(m):
            matrix[i].sort(reverse=True)
            for j in range(n):
                ans = max(ans, (j + 1) * matrix[i][j])
        return ans
