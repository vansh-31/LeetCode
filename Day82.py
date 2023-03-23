# Problem : Number of Operations to Make Network Connected
# Problem Statement : There are n computers numbered from 0 to n - 1 connected by ethernet cables connections forming a network where connections[i] = [ai, bi] represents a connection between computers ai and bi. Any computer can reach any other computer directly or indirectly through the network.
# You are given an initial computer network connections. You can extract certain cables between two directly connected computers, and place them between any pair of disconnected computers to make them directly connected.
# Return the minimum number of times you need to do this in order to make all the computers connected. If it is not possible, return -1.
class Solution:
    def makeConnected(self, n: int, connections: list[list[int]]) -> int:
        if len(connections) < n-1:
            return -1
        vis = [0] * n
        adj = [[] for i in range(n)]
        for connection in connections:
            adj[connection[0]].append(connection[1])
            adj[connection[1]].append(connection[0])
        print(vis)
        def dfs(u,parent):
            vis[u] = 1
            for v in adj[u]:
                if v == parent:
                    continue
                if not vis[v]:
                    dfs(v,u)
        count = 0
        for i in range(n):
            if not vis[i]:
                count +=1
                dfs(i,-1)
        return count-1