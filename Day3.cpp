// Problem : Median of Two Sorted Arrays
// Problem Statement : Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
#include <bits/stdc++.h>
#define ll long long
#define pb push_back
#define MOD 1000000007
#define PI 3.14
using namespace std;
class Solution
{
public:
    double findMedianSortedArrays(vector<int> &nums1, vector<int> &nums2)
    {
        int m = nums1.size();
        int n = nums2.size();
        int i = 0;
        int j = 0;
        vector<int> ans;
        while (i < m && j < n)
        {
            if (nums1[i] <= nums2[j])
            {
                ans.push_back(nums1[i++]);
            }
            else
            {
                ans.push_back(nums2[j++]);
            }
        }
        while (i < m)
        {
            ans.push_back(nums1[i++]);
        }
        while (j < n)
        {
            ans.push_back(nums2[j++]);
        }
        if (ans.size() % 2 == 1)
        {
            return ans[ans.size() / 2];
        }
        else
        {
            double median = ans[ans.size() / 2];
            median += ans[(ans.size() - 1) / 2];
            return median / 2;
        }
    }
};
int main()
{

    return 0;
}