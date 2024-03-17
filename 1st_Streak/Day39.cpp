// Problem : Jump Game II
// Problem Statement : You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

// Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

// 0 <= j <= nums[i] and
// i + j < n
// Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].
#include <bits/stdc++.h>
#define ll long long
#define pb push_back
#define MOD 1000000007
#define PI 3.14
using namespace std;
class Solution
{
public:
    int solve(vector<int> &nums, int n, int index)
    {
        if (index == n)
        {
            return 0;
        }
        if (index > n or nums[index] == 0)
        {
            return 10000000;
        }
        int ans = 10000000;
        for (int i = index + 1; i <= index + nums[index]; i++)
        {
            ans = min(ans, 1 + solve(nums, n, i));
        }
        return ans;
    }
    int solveMem(vector<int> &nums, int n, int index, vector<int> &dp)
    {
        if (index == n)
        {
            return 0;
        }
        if (index > n)
        {
            return 10000000;
        }
        if (dp[index] != -1)
        {
            return dp[index];
        }
        int ans = 10000000;
        for (int i = index + 1; i <= index + nums[index]; i++)
        {
            ans = min(ans, 1 + solveMem(nums, n, i, dp));
        }
        return dp[index] = ans;
    }
    int solveTab(vector<int> &nums, int n)
    {
        vector<int> dp(n, 10000000);
        dp[n-1] = 0;
        for (int index = n - 1; index >= 0; index--)
        {
            for (int i = index + 1; i <= index + nums[index]; i++)
            {
                if (i < n)
                {
                    dp[index] = min(dp[index], 1 + dp[i]);
                }
            }
        }
        return dp[0];
    }
    int jump(vector<int> &nums)
    {
        // return solve(nums,nums.size()-1,0);
        // vector<int> dp(nums.size(),-1);
        // return solveMem(nums,nums.size()-1,0,dp);
        return solveTab(nums,nums.size());
    }
};
int main()
{

    return 0;
}