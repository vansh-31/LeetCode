// Problem : Shortest Path with Alternating Colors
// Problem Statement : You are given an integer n, the number of nodes in a directed graph where the nodes are labeled from 0 to n - 1. Each edge is red or blue in this graph, and there could be self-edges and parallel edges.
// You are given two arrays redEdges and blueEdges where:

// redEdges[i] = [ai, bi] indicates that there is a directed red edge from node ai to node bi in the graph, and
// blueEdges[j] = [uj, vj] indicates that there is a directed blue edge from node uj to node vj in the graph.
// Return an array answer of length n, where each answer[x] is the length of the shortest path from node 0 to node x such that the edge colors alternate along the path, or -1 if such a path does not exist.
#include<bits/stdc++.h>
#define ll long long
#define pb push_back
#define MOD 1000000007
#define PI 3.14
using namespace std;
enum class Color { kInit, kRed, kBlue };

class Solution {
 public:
  vector<int> shortestAlternatingPaths(int n, vector<vector<int>>& redEdges,
                                       vector<vector<int>>& blueEdges) {
    vector<int> ans(n, -1);
    vector<vector<pair<int, Color>>> graph(n);  // graph[u] := [(v, edgeColor)]
    queue<pair<int, Color>> q{{{0, Color::kInit}}};  // [(u, prevColor)]

    for (const vector<int>& edge : redEdges) {
      const int u = edge[0];
      const int v = edge[1];
      graph[u].emplace_back(v, Color::kRed);
    }

    for (const vector<int>& edge : blueEdges) {
      const int u = edge[0];
      const int v = edge[1];
      graph[u].emplace_back(v, Color::kBlue);
    }

    for (int step = 0; !q.empty(); ++step)
      for (int sz = q.size(); sz > 0; --sz) {
        const auto [u, prevColor] = q.front();
        q.pop();
        ans[u] = ans[u] == -1 ? step : ans[u];
        for (auto& [v, edgeColor] : graph[u]) {
          if (v == -1 || edgeColor == prevColor)
            continue;
          q.emplace(v, edgeColor);
          v = -1;  // Mark (u, v) as used.
        }
      }

    return ans;
  }
};
int main()
{
    
    return 0;
}