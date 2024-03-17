# Problem : Pascal's Triangle II
# Problem Statement : Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
class Solution:
    def getRow(self, n: int) -> list[int]:
        pascal = [ [1] ]
        for i in range(1,n+1):
            pascal.append( [0] * (len(pascal[i-1]) + 1) )
            for j in range( len(pascal[i])  ):
                up1 = pascal[i-1][j-1] if j > 0 else 0
                up2 = pascal[i-1][j] if j < len(pascal[i-1]) else 0
                pascal[i][j] = up1 + up2
        return pascal[-1]