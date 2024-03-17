// Problem : Two Sum
// Problem Statement : Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
// You may assume that each input would have exactly one solution, and you may not use the same element twice.
// You can return the answer in any order.
#include <bits/stdc++.h>
#define ll long long
#define pb push_back
#define MOD 1000000007
#define PI 3.14
using namespace std;
class Solution
{
public:
    vector<int> twoSum(vector<int> &A, int x)
    {
        vector<int> B = A;
        int beg = 0;
        int end = A.size() - 1;
        int a = INT_MIN, b = INT_MIN;
        sort(A.begin(), A.end());
        while (beg < end)
        {
            if (A[beg] + A[end] == x)
            {
                a = A[beg];
                b = A[end];
                break;
            }
            else if (A[beg] + A[end] > x)
            {
                end--;
            }
            else
            {
                beg++;
            }
        }
        int j = INT_MIN, k = INT_MIN;
        cout << a << " " << b << endl;
        for (int i = 0; i < B.size(); i++)
        {
            cout << B[i] << " ";
            if (j == INT_MIN && a == B[i])
            {
                j = i;
                continue;
            }
            if (k == INT_MIN && b == B[i])
            {
                k = i;
            }
        }
        return {j, k};
    }
};
int main()
{

    return 0;
}