// Problem : Minimum Number of Arrows to Burst Balloons
// Problem Statement : There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D integer array points where points[i] = [xstart, xend] denotes a balloon whose horizontal diameter stretches between xstart and xend. You do not know the exact y-coordinates of the balloons.
// Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis. A balloon with xstart and xend is burst by an arrow shot at x if xstart <= x <= xend. There is no limit to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.
// Given the array points, return the minimum number of arrows that must be shot to burst all balloons.
#include <bits/stdc++.h>
#define ll long long
#define pb push_back
#define MOD 1000000007
#define PI 3.14
using namespace std;
class Solution
{
public:
    int findMinArrowShots(vector<vector<int>> &points)
    {
        int arrows = 1;
        sort(points.begin(), points.end());
        int start = points[0][0];
        int end = points[0][1];
        for (int i = 1; i < points.size(); i++)
        {
            if (points[i][0] >= start && points[i][0] <= end)
            {
                end = min(end, points[i][1]);
            }
            else
            {
                arrows++;
                end = points[i][1];
            }
            start = points[i][0];
        }
        return arrows;
    }
};
int main()
{

    return 0;
}