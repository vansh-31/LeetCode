# Problem : Magic Squares In Grid
# Problem Statement : A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column, and both diagonals all have the same sum.
# Given a row x col grid of integers, how many 3 x 3 contiguous magic square subgrids are there?
# Note: while a magic square can only contain numbers from 1 to 9, grid may contain numbers up to 15.
class Solution:
    def numMagicSquaresInside(self, grid: list[list[int]]) -> int:
        def valid(row, column):
            seen = set()
            c = [0] * 3
            r = [0] * 3
            for i in range(3):
                for j in range(3):
                    number = grid[row + i][column + j]
                    if number > 9 or number < 1 or number in seen:
                        return 0
                    seen.add(number)
                    c[j] += number
                    r[i] += number
            rowSum = r[0] == r[1] == r[2]
            colSum = c[0] == c[1] == c[2]
            diagonalSum = (
                grid[row][column] + grid[row + 2][column + 2]
                == grid[row][column + 2] + grid[row + 2][column]
            )
            return 1 if diagonalSum and rowSum and colSum else 0

        rows, columns = len(grid), len(grid[0])
        count = 0
        for row in range(rows - 2):
            for column in range(columns - 2):
                count += valid(row, column)
        return count
