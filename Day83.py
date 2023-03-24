# Problem : Reorder Routes to Make All Paths Lead to the City Zero
# Problem Statement : There are n cities numbered from 0 to n - 1 and n - 1 roads such that there is only one way to travel between two different cities (this network form a tree). Last year, The ministry of transport decided to orient the roads in one direction because they are too narrow.

# Roads are represented by connections where connections[i] = [ai, bi] represents a road from city ai to city bi.

# This year, there will be a big event in the capital (city 0), and many people want to travel to this city.

# Your task consists of reorienting some roads such that each city can visit the city 0. Return the minimum number of edges changed.

# It's guaranteed that each city can reach city 0 after reorder.
class Solution:
    def dfs(self, al, visited, from_node):
        change = 0
        visited[from_node] = True
        for to_node in al[from_node]:
            if not visited[abs(to_node)]:
                change += self.dfs(al, visited, abs(to_node)) + (1 if to_node > 0 else 0)
        return change

    def minReorder(self, n, connections):
        al = [[] for _ in range(n)]
        for c in connections:
            al[c[0]].append(c[1])
            al[c[1]].append(-c[0])
        visited = [False] * n
        return self.dfs(al, visited, 0)