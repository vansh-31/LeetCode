// Problem : Best Time to Buy and Sell Stock
// Problem Statement : You are given an array prices where prices[i] is the price of a given stock on the ith day.
// You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
// Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
#include <bits/stdc++.h>
#define ll long long
#define pb push_back
#define MOD 1000000007
#define PI 3.14
using namespace std;
class Solution
{
public:
    int maxProfit(vector<int> &prices)
    {
        int ans = 0;
        int low = prices[0];
        for (int i = 1; i < prices.size(); i++)
        {
            low = min(low,prices[i]);
            ans = max(ans,prices[i]-low);
        }
        return ans;
    }
};
int main()
{

    return 0;
}