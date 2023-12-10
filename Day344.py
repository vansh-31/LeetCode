# Problem : Transpose Matrix
# Problem Statement : Given a 2D integer array matrix, return the transpose of matrix.
# The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.
class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        return [ [ matrix[j][i] for j in range(len(matrix)) ] for i in range(len(matrix[0])) ]