# Problem :  Count Unreachable Pairs of Nodes in an Undirected Graph
# Problem Statement : You are given an integer n. There is an undirected graph with n nodes, numbered from 0 to n - 1. You are given a 2D integer array edges where edges[i] = [ai, bi] denotes that there exists an undirected edge connecting nodes ai and bi.
# Return the number of pairs of different nodes that are unreachable from each other.
class Solution:
    def countPairs(self, n: int, edges: list[list[int]]) -> int:
        if len(edges) == 0:
            return n*(n-1)//2
        adj = [[] for x in range(n)]
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        vis = [False] * n
        components = []
        def dfs(parent,node,temp):
            vis[node] = True
            temp += 1
            for nbr in adj[node]:
                if nbr == parent:
                    continue
                if not vis[nbr]:
                    temp = dfs(node,nbr,temp)
            return temp
        for i in range(n):
            if not vis[i]:
                components.append(dfs(-1,i,0))
        ans = 0
        for i in range(len(components)-1):
            ans += components[i] * sum(components[i+1:])
        return ans