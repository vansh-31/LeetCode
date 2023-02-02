// Problem : House Robber
// Problem Statement : You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

// Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
#include <bits/stdc++.h>
#define ll long long
#define pb push_back
#define MOD 1000000007
#define PI 3.14
using namespace std;
class Solution
{
public:
    int solveSO(vector<int> &nums)
    {
        if (nums.size() == 1)
        {
            return nums[0];
        }
        if (nums.size() == 2)
        {
            return max(nums[0], nums[1]);
        }
        int n = nums.size();
        int prev = 0;
        int curr = nums[0];
        for (int i = 1; i < n; i++)

        {
            int include = prev + nums[i];
            int exclude = curr;
            prev = curr;
            curr = max(include, exclude);
        }
        return curr;
    }
    int maximumNonAdjacentSum(vector<int> &nums)
    {
        return solveSO(nums);
    }
    int rob(vector<int> &houses)
    {
        return maximumNonAdjacentSum(houses);
    }
};
int main()
{

    return 0;
}