// Problem : Delete Columns to Make Sorted
// Problem Statement : You are given an array of n strings strs, all of the same length.

// The strings can be arranged such that there is one on each line, making a grid.

// For example, strs = ["abc", "bce", "cae"] can be arranged as follows:
// abc
// bce
// cae
// You want to delete the columns that are not sorted lexicographically. In the above example (0-indexed), columns 0 ('a', 'b', 'c') and 2 ('c', 'e', 'e') are sorted, while column 1 ('b', 'c', 'a') is not, so you would delete column 1.
// Return the number of columns that you will delete.
#include <bits/stdc++.h>
#define ll long long
#define pb push_back
#define MOD 1000000007
#define PI 3.14
using namespace std;
class Solution
{
public:
    int minDeletionSize(vector<string> &strs)
    {
        int count = 0;
        for (int col = 0; col < strs[0].size(); col++)
        {
            bool isSorted = true;
            for (int row = 0; row < strs.size() - 1; row++)
            {
                if (strs[row][col] > strs[row + 1][col])
                {
                    isSorted = false;
                    break;
                }
            }
            if (!isSorted)
            {
                count++;
            }
        }
        return count;
    }
};
int main()
{

    return 0;
}