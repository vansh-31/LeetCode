// Problem : Maximum Ice Cream Bars
// Problem Statement : It is a sweltering summer day, and a boy wants to buy some ice cream bars.
// At the store, there are n ice cream bars. You are given an array costs of length n, where costs[i] is the price of the ith ice cream bar in coins. The boy initially has coins coins to spend, and he wants to buy as many ice cream bars as possible.
// Note: The boy can buy the ice cream bars in any order.
// Return the maximum number of ice cream bars the boy can buy with coins coins.
// You must solve the problem by counting sort.
#include <bits/stdc++.h>
#define ll long long
#define pb push_back
#define MOD 1000000007
#define PI 3.14
using namespace std;
class Solution
{
public:
    int maxIceCream(vector<int> &costs, int coins)
    {
        int count = 0;
        sort(costs.begin(), costs.end());
        unsigned int n = costs.size();
        for (int i = 0; i < n; i++)
        {
            if (coins >= costs[i])
            {
                count++;
                coins -= costs[i];
            }
            else
            {
                return count;
            }
        }
        return count;
    }
};
int main()
{

    return 0;
}
