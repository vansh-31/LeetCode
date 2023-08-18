# Problem : Maximal Network Rank
# Problem Statement : There is an infrastructure of n cities with some number of roads connecting these cities. Each roads[i] = [ai, bi] indicates that there is a bidirectional road between cities ai and bi.
# The network rank of two different cities is defined as the total number of directly connected roads to either city. If a road is directly connected to both cities, it is only counted once.
# The maximal network rank of the infrastructure is the maximum network rank of all pairs of different cities.
# Given the integer n and the array roads, return the maximal network rank of the entire infrastructure.
from typing import List
class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        deg = [0] * n
        for road in roads:
            deg[road[0]] += 1
            deg[road[1]] += 1
        road_set = set(tuple(road) for road in roads)
        max_rank = 0
        for u in range(n):
            for v in range(u + 1, n):
                rank = deg[u] + deg[v]
                if (u, v) in road_set or (v, u) in road_set:
                    rank -= 1
                max_rank = max(rank, max_rank)
        return max_rank
