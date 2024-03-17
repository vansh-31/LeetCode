// Problem : Capacity To Ship Packages Within D Days
// Problem Statement : A conveyor belt has packages that must be shipped from one port to another within days days.
// The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.
// Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days.
#include<bits/stdc++.h>
#define ll long long
#define pb push_back
#define MOD 1000000007
#define PI 3.14
using namespace std;
class Solution {
 public:
  int shipWithinDays(vector<int>& weights, int days) {
    int l = *max_element(begin(weights), end(weights));
    int r = accumulate(begin(weights), end(weights), 0);

    while (l < r) {
      const int m = (l + r) / 2;
      if (shipDays(weights, m) <= days)
        r = m;
      else
        l = m + 1;
    }

    return l;
  }

 private:
  int shipDays(const vector<int>& weights, int shipCapacity) {
    int days = 1;
    int capacity = 0;
    for (const int weight : weights) {
      if (capacity + weight > shipCapacity) {
        ++days;
        capacity = weight;
      } else {
        capacity += weight;
      }
    }
    return days;
  };
};
int main()
{
    
    return 0;
}