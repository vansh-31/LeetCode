# Problem : Find the Safest Path in a Grid
# Problem Statement : You are given a 0-indexed 2D matrix grid of size n x n, where (r, c) represents:
# A cell containing a thief if grid[r][c] = 1
# An empty cell if grid[r][c] = 0
# You are initially positioned at cell (0, 0). In one move, you can move to any adjacent cell in the grid, including cells containing thieves.
# The safeness factor of a path on the grid is defined as the minimum manhattan distance from any cell in the path to any thief in the grid.
# Return the maximum safeness factor of all paths leading to cell (n - 1, n - 1).
# An adjacent cell of cell (r, c), is one of the cells (r, c + 1), (r, c - 1), (r + 1, c) and (r - 1, c) if it exists.
# The Manhattan distance between two cells (a, b) and (x, y) is equal to |a - x| + |b - y|, where |val| denotes the absolute value of val.
from collections import deque


class Solution:
    def maximumSafenessFactor(self, grid: list[list[int]]) -> int:
        n = len(grid)
        queue = deque(
            [(i, j, 1) for i in range(n) for j in range(n) if grid[i][j] == 1]
        )
        while queue:
            x, y, count = queue.popleft()
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if 0 <= x + dx < n and 0 <= y + dy < n and grid[x + dx][y + dy] == 0:
                    grid[x + dx][y + dy] = count + 1
                    queue.append((x + dx, y + dy, count + 1))  # type: ignore
        l, r = 1, n + 1
        mid = (l + r + 1) // 2
        while l < r:
            level = [(0, 0)]
            seen = {(0, 0)}
            check = False
            while level:
                nextlevel = []
                for i, j in level:
                    if (i, j) == (n - 1, n - 1):
                        check = True
                        break
                    for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        if (
                            0 <= i + di < n
                            and 0 <= j + dj < n
                            and (i + di, j + dj) not in seen
                            and grid[i + di][j + dj] >= mid
                        ):
                            seen.add((i + di, j + dj))
                            nextlevel.append((i + di, j + dj))
                level = nextlevel
            if check:
                l = mid
            else:
                r = mid - 1
            mid = (l + r + 1) // 2
        return min(mid, grid[0][0]) - 1
