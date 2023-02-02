// Problem : Course Schedule
// Problem Statement : There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
// For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
// Return true if you can finish all courses. Otherwise, return false
#include <bits/stdc++.h>
#define ll long long
#define pb push_back
#define MOD 1000000007
#define PI 3.14
using namespace std;
class Solution
{
public:
    bool dfs(int node, vector<vector<int>> &adj, vector<bool> &visited, vector<bool> &RecStack)
    {
        visited[node] = true;
        RecStack[node] = true;

        for (auto nbr : adj[node])
        {
            if (!visited[nbr])
            {
                if (dfs(nbr, adj, visited, RecStack))
                    return true;
            }
            else if (RecStack[nbr])
            {
                return true;
            }
        }
        // cout<<"NODE: "<<node<<endl;
        RecStack[node] = false;
        // cout<<RecStack[node]<<endl;
        return false;
    }
    bool canFinish(int Courses, vector<vector<int>> &pre)
    {
        vector<vector<int>> adj(Courses);
        for (int i = 0; i < pre.size(); i++)
        {
            adj[pre[i][0]].push_back(pre[i][1]);
        }
        vector<bool> visited(Courses, false);
        vector<bool> RecStack(Courses, false);

        for (int i = 0; i < Courses; i++)
        {
            if (!visited[i])
            {
                if (dfs(i, adj, visited, RecStack))
                {
                    return false;
                }
            }
        }
        return true;
    }
};
int main()
{

    return 0;
}