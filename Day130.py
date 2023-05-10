# Problem : Spiral Matrix II
# Problem Statement : Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.
class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        matrix = [[0 for i in range(n)] for j in range(n)]
        sr,sc,er,ec = 0,0,n-1,n-1
        num = 1
        while sr <= er and sc <= ec:
            # First Row
            if sr <= er and sc <= ec:
                for col in range(sc,ec+1):
                    matrix[sr][col] = num
                    num+=1
                sr+=1
            
            # Last Column
            if sr <= er and sc <= ec:
                for row in range(sr,er+1):
                    matrix[row][ec] = num
                    num+=1
                ec-=1
            
            # Last Row
            if sr <= er and sc <= ec:
                for col in range(ec,sc-1,-1):
                    matrix[er][col] = num
                    num+=1
                er-=1
            
            # First Column
            if sr <= er and sc <= ec:
                for row in range(er,sr-1,-1):
                    matrix[row][sc] = num
                    num+=1
                sc+=1
        return matrix