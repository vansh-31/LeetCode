# Problem : Second Minimum Time to Reach Destination
# Problem Statement : A city is represented as a bi-directional connected graph with n vertices where each vertex is labeled from 1 to n (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself. The time taken to traverse any edge is time minutes.
# Each vertex has a traffic signal which changes its color from green to red and vice versa every change minutes. All signals change at the same time. You can enter a vertex at any time, but can leave a vertex only when the signal is green. You cannot wait at a vertex if the signal is green.
# The second minimum value is defined as the smallest value strictly larger than the minimum value.
# For example the second minimum value of [2, 3, 4] is 3, and the second minimum value of [2, 2, 4] is 4.
# Given n, edges, time, and change, return the second minimum time it will take to go from vertex 1 to vertex n.
# Notes:
# You can go through any vertex any number of times, including 1 and n.
# You can assume that when the journey starts, all signals have just turned green.
from collections import defaultdict
from heapq import heappop, heappush
import sys
from typing import List


class Solution:
    def secondMinimum(
        self, n: int, edges: List[List[int]], time: int, change: int
    ) -> int:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        dist1 = [sys.maxsize] * (n + 1)
        dist2 = [sys.maxsize] * (n + 1)
        freq = [0] * (n + 1)
        min_heap = [(0, 1)]
        dist1[1] = 0
        while min_heap:
            timeTaken, node = heappop(min_heap)
            freq[node] += 1
            if freq[node] == 2 and node == n:
                return timeTaken
            if (timeTaken // change) % 2 == 1:
                timeTaken = change * (timeTaken // change + 1) + time
            else:
                timeTaken += time
            for neighbor in adj[node]:
                if freq[neighbor] == 2:
                    continue
                if dist1[neighbor] > timeTaken:
                    dist2[neighbor] = dist1[neighbor]
                    dist1[neighbor] = timeTaken
                    heappush(min_heap, (timeTaken, neighbor))
                elif dist2[neighbor] > timeTaken and dist1[neighbor] != timeTaken:
                    dist2[neighbor] = timeTaken
                    heappush(min_heap, (timeTaken, neighbor))
        return 0
