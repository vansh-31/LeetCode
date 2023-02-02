// Problem : Non-decreasing Subsequences
// Problem Statement : Given an integer array nums, return all the different possible non-decreasing subsequences of the given array with at least two elements. You may return the answer in any order.
#include <bits/stdc++.h>
#define ll long long
#define pb push_back
#define MOD 1000000007
#define PI 3.14
using namespace std;
class Solution
{
public:
    void solve(int i, vector<int> &temp, set<vector<int>> &ans, vector<int> &nums, int n)
    {
        if (temp.size() >= 2)
        {
            ans.insert(temp);
        }
        if (i == n)
        {
            return;
        }
        if (temp.empty() || (temp[temp.size() - 1] <= nums[i]))
        {
            temp.push_back(nums[i]);
            solve(i + 1, temp, ans, nums, n);
            temp.pop_back();
        }
        solve(i + 1, temp, ans, nums, n);
    }
    vector<vector<int>> findSubsequences(vector<int> &nums)
    {
        vector<int> temp;
        set<vector<int>> ans_set;
        vector<vector<int>> ans;
        solve(0, temp, ans_set, nums, nums.size());
        for (auto i : ans_set)
        {
            ans.push_back(i);
        }
        return ans;
    }
};
int main()
{

    return 0;
}