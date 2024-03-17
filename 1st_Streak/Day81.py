# Problem : Minimum Score of a Path Between Two Cities
# Problem Statement : You are given a positive integer n representing n cities numbered from 1 to n. You are also given a 2D array roads where roads[i] = [ai, bi, distancei] indicates that there is a bidirectional road between cities ai and bi with a distance equal to distancei. The cities graph is not necessarily connected.
# The score of a path between two cities is defined as the minimum distance of a road in this path.
# Return the minimum possible score of a path between cities 1 and n.
# Note:
# A path is a sequence of roads between two cities.
# It is allowed for a path to contain the same road multiple times, and you can visit cities 1 and n multiple times along the path.
# The test cases are generated such that there is at least one path between 1 and n.
from queue import Queue
class Solution:
    def minScore(self, n: int, roads: list[list[int]]) -> int:
        adj = [[] for x in range(n+1)]
        for x in roads:
            adj[x[0]].append([x[1],x[2]])
            adj[x[1]].append([x[0],x[2]])
        vis = [0] * (n+1)
        q = Queue()
        q.put(1)
        vis[1] = 1
        ans = 10001
        while not q.empty():
            u = q.get()
            for v,dist in adj[u]:
                ans = min(ans,dist)
                if not vis[v]:
                    vis[v] = 1
                    q.put(v)
        return ans