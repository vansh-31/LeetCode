# Problem : Minimum Height Trees
# Problem Statement : A tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.
# Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where edges[i] = [ai, bi] indicates that there is an undirected edge between the two nodes ai and bi in the tree, you can choose any node of the tree as the root. When you select a node x as the root, the result tree has height h. Among all possible rooted trees, those with minimum height (i.e. min(h))  are called minimum height trees (MHTs).
# Return a list of all MHTs' root labels. You can return the answer in any order.
# The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.
from collections import defaultdict, deque
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return [i for i in range(n)]

        adj = defaultdict(list)
        edge_count = defaultdict(int)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
            edge_count[a] += 1
            edge_count[b] += 1

        q = deque(n for n in adj if len(adj[n]) == 1)
        visited = set(q)

        while len(visited) < n:
            length = len(q)
            for _ in range(length):
                node = q.popleft()
                for neighbor in adj[node]:
                    if neighbor not in visited:
                        edge_count[neighbor] -= 1
                        if edge_count[neighbor] == 1:
                            q.append(neighbor)
                            visited.add(neighbor)
        return q # type: ignore
