# Problem : Largest Color Value in a Directed Graph
# Problem Statement : There is a directed graph of n colored nodes and m edges. The nodes are numbered from 0 to n - 1.
# You are given a string colors where colors[i] is a lowercase English letter representing the color of the ith node in this graph (0-indexed). You are also given a 2D array edges where edges[j] = [aj, bj] indicates that there is a directed edge from node aj to node bj.
# A valid path in the graph is a sequence of nodes x1 -> x2 -> x3 -> ... -> xk such that there is a directed edge from xi to xi+1 for every 1 <= i < k. The color value of the path is the number of nodes that are colored the most frequently occurring color along that path.
# Return the largest color value of any valid path in the given graph, or -1 if the graph contains a cycle.
class Solution:
  def largestPathValue(self, colors, edges):
      n, k = len(colors), 26
      indegrees = [0] * n
      graph = [[] for _ in range(n)]
      for u, v in edges:
          graph[u].append(v)
          indegrees[v] += 1
      zero_indegree = set(i for i in range(n) if indegrees[i] == 0)
      counts = [[0] * k for _ in range(n)]
      for i, c in enumerate(colors):
          counts[i][ord(c) - ord('a')] += 1
      max_count, visited = 0, 0
      while zero_indegree:
          u = zero_indegree.pop()
          visited += 1
          for v in graph[u]:
              for i in range(k):
                  counts[v][i] = max(counts[v][i], counts[u][i] + (ord(colors[v]) - ord('a') == i))
              indegrees[v] -= 1
              if indegrees[v] == 0:
                  zero_indegree.add(v)
          max_count = max(max_count, max(counts[u]))
      return max_count if visited == n else -1