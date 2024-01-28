# Problem : Number of Submatrices That Sum to Target
# Problem Statement : Given a matrix and a target, return the number of non-empty submatrices that sum to target.
# A submatrix x1, y1, x2, y2 is the set of all cells matrix[x][y] with x1 <= x <= x2 and y1 <= y <= y2.
# Two submatrices (x1, y1, x2, y2) and (x1', y1', x2', y2') are different if they have some coordinate that is different: for example, if x1 != x1'.
from collections import defaultdict
from typing import List


class Solution:
    def numSubmatrixSumTarget(self, mat: List[List[int]], target: int) -> int:
        m, n = len(mat), len(mat[0])
        for i in range(m):
            for j in range(1, n):
                mat[i][j] += mat[i][j - 1]
            mat[i] = [0] + mat[i]
        ans = 0
        d = defaultdict(int)
        for col1 in range(n):
            for col2 in range(col1 + 1, n + 1):
                temp = 0
                d[0] = 1
                for r in range(m):
                    temp += mat[r][col2] - mat[r][col1]
                    if temp - target in d:
                        ans += d[temp - target]
                    d[temp] += 1
                d.clear()
        return ans
