// Problem : Search Insert Position
// Problem Statement Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
// You must write an algorithm with O(log n) runtime complexity.
#include <bits/stdc++.h>
#define ll long long
#define pb push_back
#define MOD 1000000007
#define PI 3.14
using namespace std;
class Solution
{
public:
    int searchInsert(vector<int> &nums, int target)
    {
        return lower_bound(nums.begin(), nums.end(), target) - nums.begin();
    }
};
int main()
{

    return 0;
}