# Problem : Find Valid Matrix Given Row and Column Sums
# Problem Statement : You are given two arrays rowSum and colSum of non-negative integers where rowSum[i] is the sum of the elements in the ith row and colSum[j] is the sum of the elements of the jth column of a 2D matrix. In other words, you do not know the elements of the matrix, but you do know the sums of each row and column.
# Find any matrix of non-negative integers of size rowSum.length x colSum.length that satisfies the rowSum and colSum requirements.
# Return a 2D array representing any matrix that fulfills the requirements. It's guaranteed that at least one matrix that fulfills the requirements exists.
class Solution:
    def restoreMatrix(self, rowSum: list[int], colSum: list[int]) -> list[list[int]]:
        c, r = len(colSum), len(rowSum)
        mat = [[0 for i in range(c)] for i in range(r)]
        for i in range(r):
            for j in range(c):
                rsum, csum = rowSum[i], colSum[j]
                minn = min(rsum, csum)
                mat[i][j] = minn
                rowSum[i] -= minn
                colSum[j] -= minn
        return mat
