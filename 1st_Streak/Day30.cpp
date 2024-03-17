// Problem : N-th Tribonacci Number
// Problem Statement : The Tribonacci sequence Tn is defined as follows: 

// T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

// Given n, return the value of Tn.

#include <bits/stdc++.h>
#define ll long long
#define pb push_back
#define MOD 1000000007
#define PI 3.14
using namespace std;
class Solution
{
public:
    int tribonacci(int n)
    {
        if (n == 0)
        {
            return 0;
        }
        if (n <= 2)
        {
            return 1;
        }
        int zero = 0;
        int one = 1;
        int two = 1;
        int temp;
        for (int i = 3; i <= n; i++)
        {
            temp = zero + one + two;
            zero = one;
            one = two;
            two = temp;
        }
        return two;
    }
};
int main()
{

    return 0;
}