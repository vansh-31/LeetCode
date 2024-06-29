# Problem : All Ancestors of a Node in a Directed Acyclic Graph
# Problem Statement : You are given a positive integer n representing the number of nodes of a Directed Acyclic Graph (DAG). The nodes are numbered from 0 to n - 1 (inclusive).
# You are also given a 2D integer array edges, where edges[i] = [fromi, toi] denotes that there is a unidirectional edge from fromi to toi in the graph.
# Return a list answer, where answer[i] is the list of ancestors of the ith node, sorted in ascending order.
# A node u is an ancestor of another node v if u can reach v via a set of edges.
from typing import List
from collections import deque


class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = [[] for _ in range(n)]
        inDeg = [0] * n
        for e in edges:
            graph[e[0]].append(e[1])
            inDeg[e[1]] += 1
        q = deque()
        for i in range(n):
            if inDeg[i] == 0:
                q.append(i)
        ancestors = [set() for _ in range(n)]
        while q:
            u = q.popleft()
            for v in graph[u]:
                inDeg[v] -= 1
                ancestors[v].add(u)
                ancestors[v].update(ancestors[u])
                if inDeg[v] == 0:
                    q.append(v)
        ans = [[] for _ in range(n)]
        for i in range(n):
            ans[i] = sorted(list(ancestors[i]))
        return ans
