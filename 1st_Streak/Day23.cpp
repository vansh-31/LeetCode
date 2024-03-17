// Problem : Find the Town Judge
// Problem : In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.
// If the town judge exists, then:
// The town judge trusts nobody.
// Everybody (except for the town judge) trusts the town judge.
// There is exactly one person that satisfies properties 1 and 2.
// You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi. If a trust relationship does not exist in trust array, then such a trust relationship does not exist.
// Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.
#include <bits/stdc++.h>
#define ll long long
#define pb push_back
#define MOD 1000000007
#define PI 3.14
using namespace std;
class Solution
{
public:
    int findJudge(int n, vector<vector<int>> &trust)
    {
        int m = trust.size();
        vector<vector<int>> adj(n + 1);
        vector<int> Indeg(n + 1, 0);
        for (int i = 0; i < m; i++)
        {
            int u = trust[i][0];
            int v = trust[i][1];

            Indeg[v]++;

            adj[u].push_back(v);
        }
        for (int i = 1; i <= n; i++)
        {
            if (Indeg[i] == n - 1)
            {
                if (adj[i].size() == 0)
                {
                    return i;
                }
            }
        }
        return -1;
    }
};
int main()
{

    return 0;
}