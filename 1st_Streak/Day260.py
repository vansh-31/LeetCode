# Problem : Shortest Path Visiting All Nodes
# Problem Statement : You have an undirected, connected graph of n nodes labeled from 0 to n - 1. You are given an array graph where graph[i] is a list of all the nodes connected with node i by an edge.
# Return the length of the shortest path that visits every node. You may start and stop at any node, you may revisit nodes multiple times, and you may reuse edges.
from collections import deque, namedtuple


class Solution:
    def shortestPathLength(self, graph):
        n = len(graph)
        all_mask = (1 << n) - 1
        visited = set()
        Node = namedtuple("Node", ["node", "mask", "cost"])

        q = deque()
        for i in range(n):
            mask_value = 1 << i
            this_node = Node(i, mask_value, 1)
            q.append(this_node)
            visited.add((i, mask_value))

        while q:
            curr = q.popleft()

            if curr.mask == all_mask:
                return curr.cost - 1

            for adj in graph[curr.node]:
                both_visited_mask = curr.mask | (1 << adj)
                this_node = Node(adj, both_visited_mask, curr.cost + 1)

                if (adj, both_visited_mask) not in visited:
                    visited.add((adj, both_visited_mask))
                    q.append(this_node)

        return -1
