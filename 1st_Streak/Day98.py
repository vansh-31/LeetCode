# Problem : Clone Graph
# Problem Statement : Given a reference of a node in a connected undirected graph.
# Return a deep copy (clone) of the graph.
# Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':

        def dfs(node, visited) -> 'Node':
            if not node:
                return node
            if node in visited:
                return visited[node]

            cloneNode = Node(node.val)
            visited[node] = cloneNode

            for neighbor in node.neighbors:
                cloned_nbr = dfs(neighbor, visited)
                if cloned_nbr:
                    cloneNode.neighbors.append(cloned_nbr)
            return cloneNode

        visited = {}
        return dfs(node, visited)