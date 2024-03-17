// Problem : Shuffle the Array
// Problem Statement : Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
// Return the array in the form [x1,y1,x2,y2,...,xn,yn].
#include <bits/stdc++.h>
#define ll long long
#define pb push_back
#define MOD 1000000007
#define PI 3.14
using namespace std;
class Solution
{
public:
    vector<int> shuffle(vector<int> &nums, int n)
    {
        vector<int> ans;
        int i = 0;
        int j = n;
        while(i < n && j < n*2)
        {
            ans.push_back(nums[i++]);
            ans.push_back(nums[j++]);
        }
        return ans;
    }
};
int main()
{

    return 0;
}