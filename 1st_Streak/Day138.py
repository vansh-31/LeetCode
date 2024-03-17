# Problem : Minimum Number of Vertices to Reach All Nodes
# Problem Statement : Given a directed acyclic graph, with n vertices numbered from 0 to n-1, and an array edges where edges[i] = [fromi, toi] represents a directed edge from node fromi to node toi.
# Find the smallest set of vertices from which all nodes in the graph are reachable. It's guaranteed that a unique solution exists.
# Notice that you can return the vertices in any order.
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: list[list[int]]) -> list[int]:
        indeg = [0 for i in range(n)]
        for edge in edges:
            indeg[edge[1]] += 1
        ans = []
        for node in range(n):
            if indeg[node]==0:
                ans.append(node)
        return ans