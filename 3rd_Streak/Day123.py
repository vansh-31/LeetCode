# Problem : Find the City With the Smallest Number of Neighbors at a Threshold Distance
# Problem Statement : There are n cities numbered from 0 to n-1. Given the array edges where edges[i] = [fromi, toi, weighti] represents a bidirectional and weighted edge between cities fromi and toi, and given the integer distanceThreshold.
# Return the city with the smallest number of cities that are reachable through some path and whose distance is at most distanceThreshold, If there are multiple such cities, return the city with the greatest number.
# Notice that the distance of a path connecting cities i and j is equal to the sum of the edges' weights along that path.
class Solution:
    def findTheCity(
        self, n: int, edges: list[list[int]], distanceThreshold: int
    ) -> int:
        dist = [[float("inf")] * n for _ in range(n)]
        for i in range(n):
            dist[i][i] = 0
        for u, v, w in edges:
            dist[u][v] = w
            dist[v][u] = w
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        reachable_cities = [0] * n
        for i in range(n):
            for j in range(n):
                if i != j and dist[i][j] <= distanceThreshold:
                    reachable_cities[i] += 1
        min_reachable = float("inf")
        result_city = -1
        for i in range(n):
            if reachable_cities[i] <= min_reachable:
                if reachable_cities[i] < min_reachable or i > result_city:
                    min_reachable = reachable_cities[i]
                    result_city = i
        return result_city
