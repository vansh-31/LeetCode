// Problem : Count Odd Numbers in an Interval Range
// Problem Statement : Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).
#include <bits/stdc++.h>
#define ll long long
#define pb push_back
#define MOD 1000000007
#define PI 3.14
using namespace std;
class Solution
{
public:
    int countOdds(int l, int h)
    {
        return ((h + 1) / 2) - (l / 2);
    }
};
int main()
{

    return 0;
}