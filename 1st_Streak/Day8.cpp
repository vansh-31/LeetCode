// Problem : Minimum Rounds to Complete All Tasks
// Problem Statement : You are given a 0-indexed integer array tasks, where tasks[i] represents the difficulty level of a task. In each round, you can complete either 2 or 3 tasks of the same difficulty level.
// Return the minimum rounds required to complete all the tasks, or -1 if it is not possible to complete all the tasks.
#include <bits/stdc++.h>
#define ll long long
#define pb push_back
#define MOD 1000000007
#define PI 3.14
using namespace std;
class Solution
{
public:
    int minimumRounds(vector<int> &tasks)
    {
        unordered_map<int, int> m;
        int ans = 0;
        for (int i = 0; i < tasks.size(); i++)
        {
            m[tasks[i]]++;
        }
        for (auto i : m)
        {
            if (i.second < 2)
            {
                return -1;
            }
            int count = i.second;
            if (count % 3 == 0)
            {
                ans += (count / 3);
            }
            else if (count % 3 == 2)
            {
                ans += (count / 3) + 1;
            }
            else
            {
                ans += 2;
                count -= 4;
                if (count != 0)
                    ans += (count / 3);
            }
        }
        return ans;
    }
};
int main()
{

    return 0;
}