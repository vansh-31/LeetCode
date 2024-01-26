# Problem : Out of Boundary Paths
# Problem Statement : There is an m x n grid with a ball. The ball is initially at the position [startRow, startColumn]. You are allowed to move the ball to one of the four adjacent cells in the grid (possibly out of the grid crossing the grid boundary). You can apply at most maxMove moves to the ball.
# Given the five integers m, n, maxMove, startRow, startColumn, return the number of paths to move the ball out of the grid boundary. Since the answer can be very large, return it modulo 109 + 7.
class Solution:
    def findPaths(
        self, m: int, n: int, maxMove: int, startRow: int, startColumn: int
    ) -> int:
        M = 10**9 + 7
        dp = [
            [[-1 for _ in range(maxMove + 1)] for _ in range(n + 1)]
            for _ in range(m + 1)
        ]

        def solve(row, col, move):
            if row >= m or row < 0 or col >= n or col < 0:
                return 1
            if move <= 0:
                return 0
            if dp[row][col][move] != -1:
                return dp[row][col][move]
            up = (solve(row - 1, col, move - 1)) % M
            left = (solve(row, col - 1, move - 1)) % M
            down = (solve(row + 1, col, move - 1)) % M
            right = (solve(row, col + 1, move - 1)) % M
            dp[row][col][move] = (up + down + left + right) % M
            return dp[row][col][move]

        return solve(startRow, startColumn, maxMove)
