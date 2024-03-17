# Problem : Path With Minimum Effort
# Problem Statement : You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns, where heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell, (0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.
# A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.
# Return the minimum effort required to travel from the top-left cell to the bottom-right cell.
from typing import List
from heapq import heappush, heappop


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]):
        rows, cols = len(heights), len(heights[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        dist = [[float("inf") for _ in range(cols)] for _ in range(rows)]
        dist[0][0] = 0
        minHeap = [(0, 0, 0)]

        while minHeap:
            effort, x, y = heappop(minHeap)

            if x == rows - 1 and y == cols - 1:
                return effort

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < rows and 0 <= ny < cols:
                    new_effort = max(effort, abs(heights[x][y] - heights[nx][ny]))

                    if new_effort < dist[nx][ny]:
                        dist[nx][ny] = new_effort
                        heappush(minHeap, (new_effort, nx, ny))  # type: ignore
