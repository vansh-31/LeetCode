# Problem : Spiral Matrix
# Problem Statement : Given an m x n matrix, return all elements of the matrix in spiral order.
class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        sr,sc,er,ec = 0,0,len(matrix)-1,len(matrix[0])-1
        ans = []
        while sr <= er and sc <= ec:
            # First Row
            if sr <= er and sc <= ec:
                for col in range(sc,ec+1):
                    ans.append( matrix[sr][col] )
                sr+=1
            
            # Last Column
            if sr <= er and sc <= ec:
                for row in range(sr,er+1):
                    ans.append( matrix[row][ec] )
                ec-=1
            
            # Last Row
            if sr <= er and sc <= ec:
                for col in range(ec,sc-1,-1):
                    ans.append( matrix[er][col] )
                er-=1
            
            # First Column
            if sr <= er and sc <= ec:
                for row in range(er,sr-1,-1):
                    ans.append( matrix[row][sc] )
                sc+=1
        return ans