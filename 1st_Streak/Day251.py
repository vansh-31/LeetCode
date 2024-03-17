# Problem : Pascal's Triangle
# Problem Statement : Given an integer numRows, return the first numRows of Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
from typing import List
class Solution:
    def generate(self, n: int) -> List[List[int]]:
        pascal = [ [1] ]
        for i in range(1,n):
            pascal.append( [0] * (len(pascal[i-1]) + 1) )
            for j in range( len(pascal[i])  ):
                up1 = pascal[i-1][j-1] if j > 0 else 0
                up2 = pascal[i-1][j] if j < len(pascal[i-1]) else 0
                pascal[i][j] = up1 + up2
        return pascal