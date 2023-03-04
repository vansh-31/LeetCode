// Problem : Count Subarrays With Fixed Bounds
// Problem Statement : You are given an integer array nums and two integers minK and maxK.

// A fixed-bound subarray of nums is a subarray that satisfies the following conditions:

// The minimum value in the subarray is equal to minK.
// The maximum value in the subarray is equal to maxK.
// Return the number of fixed-bound subarrays.

// A subarray is a contiguous part of an array.
#include <bits/stdc++.h>
#define ll long long
#define pb push_back
#define MOD 1000000007
#define PI 3.14
using namespace std;
class Solution {
public:
    long long countSubarrays(vector<int>& nums, int minK, int maxK) {
        int n = nums.size();
        int leftBound = -1;
        int lastMin = -1, lastMax = -1;
        long long count = 0;
        
        for (int i = 0; i < n; i++) {
            if (nums[i] >= minK && nums[i] <= maxK) {
                lastMin = (nums[i] == minK) ? i : lastMin;
                lastMax = (nums[i] == maxK) ? i : lastMax;

                count += max(0, min(lastMin, lastMax) - leftBound);
            } else {
                leftBound = i;
                lastMin = -1;
                lastMax = -1;
            }
        }
        return count;
    }
};
int main()
{

    return 0;
}