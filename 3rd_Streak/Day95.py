# Problem : Maximum Total Importance of Roads
# Problem Statement : You are given an integer n denoting the number of cities in a country. The cities are numbered from 0 to n - 1.
# You are also given a 2D integer array roads where roads[i] = [ai, bi] denotes that there exists a bidirectional road connecting cities ai and bi.
# You need to assign each city with an integer value from 1 to n, where each value can only be used once. The importance of a road is then defined as the sum of the values of the two cities it connects.
# Return the maximum total importance of all roads possible after assigning the values optimally.
from collections import defaultdict
from typing import List


class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        connections = defaultdict(int)
        for a, b in roads:
            connections[a] += 1
            connections[b] += 1
        sorted_cities = sorted(connections.keys(), key=lambda x: -connections[x])
        values = [0] * n
        for i, city in enumerate(sorted_cities):
            values[city] = n - i
        total_importance = 0
        for a, b in roads:
            total_importance += values[a] + values[b]
        return total_importance
