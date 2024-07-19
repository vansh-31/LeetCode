# Problem : Lucky Numbers in a Matrix
# Problem Statement : Given an m x n matrix of distinct numbers, return all lucky numbers in the matrix in any order.
# A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.
class Solution:
    def luckyNumbers(self, matrix: list[list[int]]) -> list[int]:
        colMax = set(map(max, zip(*matrix)))
        for row in matrix:
            mn = min(row)
            if mn in colMax:
                return [mn]
        return []
