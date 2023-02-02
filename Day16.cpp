// Problem : Insert Interval
// Problem Statement : You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.
// Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).
// Return intervals after the insertion.
#include <bits/stdc++.h>
#define ll long long
#define pb push_back
#define MOD 1000000007
#define PI 3.14
using namespace std;
class Solution
{
public:
    vector<vector<int>> insert(vector<vector<int>> &intervals, vector<int> &newInterval)
    {
        intervals.push_back({newInterval});
        sort(intervals.begin(), intervals.end());
        int j = 0, n = intervals.size();
        for (int i = 1; i < n; i++)
        {
            if (intervals[j][1] >= intervals[i][0])
            {
                intervals[j][1] = max(intervals[j][1], intervals[i][1]);
            }
            else
            {
                j++;
                intervals[j] = intervals[i];
            }
        }
        vector<vector<int>> ans;
        for (int i = 0; i <= j; i++)
        {
            ans.push_back(intervals[i]);
        }
        return ans;
    }
};
int main()
{

    return 0;
}