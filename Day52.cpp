// Problem : Single Element in a Sorted Array
// Problem Statement : You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.
// Return the single element that appears only once.
// Your solution must run in O(log n) time and O(1) space.
#include <bits/stdc++.h>
#define ll long long
#define pb push_back
#define MOD 1000000007
#define PI 3.14
using namespace std;
class Solution
{
public:
    int singleNonDuplicate(vector<int> &nums)
    {
        int st = 0, end = nums.size() / 2;
        int ans = -1;
        while (st <= end)
        {
            int mid = (st + end) / 2;
            int ind = mid * 2;
            if (ind + 1 >= nums.size() or nums[ind] != nums[ind + 1])
            {
                end = mid - 1;
                ans = nums[ind];
            }
            else
            {
                st = mid + 1;
            }
        }
        return ans;
    }
};
int main()
{

    return 0;
}