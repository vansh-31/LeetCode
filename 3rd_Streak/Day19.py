# Problem : Maximal Rectangle
# Problem Statement : Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.
import collections


class Solution:
    def prev_next_Smaller(self, arr):
        n = len(arr)
        prev = [-1] * n
        next = [n] * n
        stack = collections.deque()
        stack.append(-1)
        for i in range(n):
            while stack[-1] != -1 and arr[stack[-1]] >= arr[i]:
                stack.pop()
            prev[i] = stack[-1]
            stack.append(i)
        stack = collections.deque()
        stack.append(n)
        for i in range(n - 1, -1, -1):
            while stack[-1] != n and arr[stack[-1]] >= arr[i]:
                stack.pop()
            next[i] = stack[-1]
            stack.append(i)
        return [prev, next]

    def largestRectangleArea(self, heights: list[int]) -> int:
        prev, nextt = self.prev_next_Smaller(heights)
        ans = 0
        for i in range(len(heights)):
            height = heights[i]
            width = nextt[i] - prev[i] - 1
            ans = max(ans, height * width)
        return ans

    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        n, m = len(matrix), len(matrix[0])
        # matrix = [ [int(x) for x in row] for row in matrix]
        matrix = [list(map(lambda x: int(x), row)) for row in matrix]  # type: ignore
        ans = self.largestRectangleArea(matrix[0])  # type: ignore
        for i in range(1, n):
            for j in range(m):
                if matrix[i][j] != 0:
                    matrix[i][j] += matrix[i - 1][j]
            ans = max(ans, self.largestRectangleArea(matrix[i]))  # type: ignore
        return ans
