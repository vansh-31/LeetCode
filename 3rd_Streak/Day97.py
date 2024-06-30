# Problem : Remove Max Number of Edges to Keep Graph Fully Traversable
# Problem Statement : Alice and Bob have an undirected graph of n nodes and three types of edges:
# Type 1: Can be traversed by Alice only.
# Type 2: Can be traversed by Bob only.
# Type 3: Can be traversed by both Alice and Bob.
# Given an array edges where edges[i] = [typei, ui, vi] represents a bidirectional edge of type typei between nodes ui and vi, find the maximum number of edges you can remove so that after removing the edges, the graph can still be fully traversed by both Alice and Bob. The graph is fully traversed by Alice and Bob if starting from any node, they can reach all other nodes.
# Return the maximum number of edges you can remove, or return -1 if Alice and Bob cannot fully traverse the graph.
class Solution:
    def maxNumEdgesToRemove(self, n, edges):
        def find(x, parent):
            if parent[x] != x:
                parent[x] = find(parent[x], parent)
            return parent[x]

        def union(x, y, parent):
            parent[find(x, parent)] = find(y, parent)

        dsu1 = list(range(n + 1))
        dsu2 = list(range(n + 1))
        count = 0
        edges.sort(key=lambda x: x[0], reverse=True)
        for edge in edges:
            if edge[0] == 3:
                if find(edge[1], dsu1) == find(edge[2], dsu1) and find(
                    edge[1], dsu2
                ) == find(edge[2], dsu2):
                    count += 1
                    continue
                union(edge[1], edge[2], dsu1)
                union(edge[1], edge[2], dsu2)
            elif edge[0] == 1:
                if find(edge[1], dsu1) == find(edge[2], dsu1):
                    count += 1
                union(edge[1], edge[2], dsu1)
            else:
                if find(edge[1], dsu2) == find(edge[2], dsu2):
                    count += 1
                union(edge[1], edge[2], dsu2)

        for i in range(1, n + 1):
            find(i, dsu1)
            find(i, dsu2)

        for i in range(2, n + 1):
            if dsu1[i] != dsu1[1] or dsu2[i] != dsu2[1]:
                return -1

        return count
