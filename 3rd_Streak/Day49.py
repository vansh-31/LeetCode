# Problem : 
# Problem Statement : 
class Solution:
    def matrixScore(self, grid: list[list[int]]) -> int:
        m,n = len(grid),len(grid[0])
        cols = [0] * n
        msb = True
        for i in range(m):
            if grid[i][0] == 0:
                msb = False
            for j in range(n):
                if not msb:
                    grid[i][j] = int(not grid[i][j])
                cols[j] += grid[i][j]
            msb = True
        for col,val in enumerate(cols):
            if val < m/2:
                for row in grid:
                    row[col] = int(not row[col])
        ans = 0
        for row in grid:
            ans += sum([2**i * val for i,val in enumerate(row[::-1])])
        return ans