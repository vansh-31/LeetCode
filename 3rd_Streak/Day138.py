# Problem : Regions Cut By Slashes
# Problem Statement : An n x n grid is composed of 1 x 1 squares where each 1 x 1 square consists of a '/', '\', or blank space ' '. These characters divide the square into contiguous regions.
# Given the grid grid represented as a string array, return the number of regions.
# Note that backslash characters are escaped, so a '\' is represented as '\\'.
class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        self.parent[self.find(b)] = self.find(a)


class Solution:
    def regionsBySlashes(self, grid: list[str]) -> int:
        n = len(grid)
        uf = UnionFind(4 * n * n)
        for row in range(n):
            for col in range(n):
                cell = grid[row][col]
                index = 4 * (row * n + col)
                if cell == " ":
                    uf.union(index + 0, index + 1)
                    uf.union(index + 1, index + 2)
                    uf.union(index + 2, index + 3)
                if cell == "/":
                    uf.union(index + 0, index + 3)
                    uf.union(index + 1, index + 2)
                if cell == "\\":
                    uf.union(index + 2, index + 3)
                    uf.union(index + 0, index + 1)
                if row < n - 1:
                    uf.union(index + 2, (index + 4 * n) + 0)
                if col < n - 1:
                    uf.union(index + 1, (index + 4) + 3)
        output = 0
        for i in range(4 * n * n):
            if uf.find(i) == i:
                output += 1
        return output
