// Problem : Add Binary
// Problem Statement : Given two binary strings a and b, return their sum as a binary string.
#include <bits/stdc++.h>
#define ll long long
#define pb push_back
#define MOD 1000000007
#define PI 3.14
using namespace std;
class Solution
{
public:
    string addBinary(string a, string b)
    {
        int i = a.length() - 1;
        int j = b.length() - 1;
        string ans;
        int carry = 0;

        while (i >= 0 || j >= 0 || carry)
        {
            if (i >= 0)
            {
                carry += a[i] - '0';
                i--;
            }
            if (j >= 0)
            {
                carry += b[j] - '0';
                j--;
            }
            ans += (carry % 2 + '0');
            carry = carry / 2;
        }
        reverse(ans.begin(), ans.end());
        return ans;
    }
};
int main()
{

    return 0;
}