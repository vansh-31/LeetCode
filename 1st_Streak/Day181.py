# Problem : Last Day Where You Can Still Cross
# Problem Statement : There is a 1-based binary matrix where 0 represents land and 1 represents water. You are given integers row and col representing the number of rows and columns in the matrix, respectively.
# Initially on day 0, the entire matrix is land. However, each day a new cell becomes flooded with water. You are given a 1-based 2D array cells, where cells[i] = [ri, ci] represents that on the ith day, the cell on the rith row and cith column (1-based coordinates) will be covered with water (i.e., changed to 1).
# You want to find the last day that it is possible to walk from the top to the bottom by only walking on land cells. You can start from any cell in the top row and end at any cell in the bottom row. You can only travel in the four cardinal directions (left, right, up, and down).
# Return the last day where it is possible to walk from the top to the bottom by only walking on land cells.
import collections
from typing import List
class Solution:
    def isPossible(self, row, col, cells, day):
        grid = [[0] * col for _ in range(row)]
        queue = collections.deque()
        for r, c in cells[:day]:
            grid[r - 1][c - 1] = 1
        for i in range(col):
            if not grid[0][i]:
                queue.append((0, i))
                grid[0][i] = -1
        while queue:
            r, c = queue.popleft()
            if r == row - 1:
                return True
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 0:
                    grid[nr][nc] = -1
                    queue.append((nr, nc))
        return False
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        left, right = 1, row * col
        
        while left < right:
            mid = right - (right - left) // 2
            if self.isPossible(row, col, cells, mid):
                left = mid
            else:
                right = mid - 1
        return left