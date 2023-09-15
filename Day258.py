# Problem : Min Cost to Connect All Points
# Problem Statement : You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].
# The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.
# Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.
from typing import List
from heapq import heappush, heappop


def manhattan_distance(p1: List[int], p2: List[int]) -> int:
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]

    def find(self, u):
        if self.parent[u] == u:
            return u
        self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        u = self.find(u)
        v = self.find(v)

        if u == v:
            return False

        if self.rank[u] > self.rank[v]:
            u, v = v, u

        self.parent[u] = v

        if self.rank[u] == self.rank[v]:
            self.rank[v] += 1

        return True


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        uf = UnionFind(n)

        edges = []

        for i in range(n):
            for j in range(i + 1, n):
                distance = manhattan_distance(points[i], points[j])
                heappush(edges, (distance, i, j))

        mst_weight = 0
        mst_edges = 0

        while edges:
            w, u, v = heappop(edges)
            if uf.union(u, v):
                mst_weight += w
                mst_edges += 1
                if mst_edges == n - 1:
                    break

        return mst_weight
