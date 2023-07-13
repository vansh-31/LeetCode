# Problem : Course Schedule
# Problem Statement : There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.
from typing import List
class Solution:
    def canFinish(self, n: int, G: List[List[int]]) -> bool:
        visited = [False] * n
        recStack = [False] * n
        adj = [[] for _ in range(n)]
        for edge in G:
            adj[edge[0]].append(edge[1])
        def dfs(node):
            visited[node] = recStack[node] = True
            for nbr in adj[node]:
                if not visited[nbr]:
                    if dfs(nbr):
                        return True
                if recStack[nbr]:
                    return True
            recStack[node] = False
            return False
        for node in range(n):
            if not visited[node]:
                if dfs(node):
                    return False
        return True