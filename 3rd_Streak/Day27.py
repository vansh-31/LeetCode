# Problem : Find if Path Exists in Graph
# Problem Statement : There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.
# You want to determine if there is a valid path that exists from vertex source to vertex destination.
# Given edges and the integers n, source, and destination, return true if there is a valid path from source to destination, or false otherwise.
from typing import List
from collections import defaultdict


class Solution:
    def validPath(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        seen = set()
        G = defaultdict(list)
        for src, dest in edges:
            G[src].append(dest)
            G[dest].append(src)

        def dfs(node):
            seen.add(node)
            if node == destination:
                return True
            for neighbor in G[node]:
                if neighbor not in seen:
                    if dfs(neighbor):
                        return True
            return False

        return dfs(source)
