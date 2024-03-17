# Problem : Design Graph With Shortest Path Calculator
# Problem Statement : There is a directed weighted graph that consists of n nodes numbered from 0 to n - 1. The edges of the graph are initially represented by the given array edges where edges[i] = [fromi, toi, edgeCosti] meaning that there is an edge from fromi to toi with the cost edgeCosti.
# Implement the Graph class:
# Graph(int n, int[][] edges) initializes the object with n nodes and the given edges.
# addEdge(int[] edge) adds an edge to the list of edges where edge = [from, to, edgeCost]. It is guaranteed that there is no edge between the two nodes before adding this one.
# int shortestPath(int node1, int node2) returns the minimum cost of a path from node1 to node2. If no path exists, return -1. The cost of a path is the sum of the costs of the edges in the path.
from typing import List
from heapq import heappush, heappop


class Graph:
    def __init__(self, n: int, edges: List[List[int]]):
        self.n = n
        self.adj = [[] for _ in range(n)]
        for u, v, w in edges:
            self.adj[u].append((v, w))

    def addEdge(self, edge: List[int]) -> None:
        self.adj[edge[0]].append((edge[1], edge[2]))

    def shortestPath(self, node1: int, node2: int) -> int:
        DIST = [10000000] * self.n
        DIST[node1] = 0
        pq = [(0, node1)]
        while pq:
            u = heappop(pq)[1]
            for nbr in self.adj[u]:
                v, w = nbr
                if DIST[v] > DIST[u] + w:
                    DIST[v] = DIST[u] + w
                    heappush(pq, (DIST[v], v))
        if DIST[node2] == 10000000:
            DIST[node2] = -1
        return DIST[node2]


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)
