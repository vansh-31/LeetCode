// Problem : Gas Station
// Problem Statement : There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

// You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

// Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique
#include <bits/stdc++.h>
#define ll long long
#define pb push_back
#define MOD 1000000007
#define PI 3.14
using namespace std;
class Solution
{
public:
    int canCompleteCircuit(vector<int> &gas, vector<int> &cost)
    {
        int deficit = 0;
        int Petrol = 0;
        int start = 0;
        int n = gas.size();
        for (int i = 0; i < n; i++)
        {
            if (gas[i] + Petrol >= cost[i])
            {
                Petrol += gas[i] - cost[i];
            }
            else
            {
                deficit += gas[i] + Petrol - cost[i];
                start = i + 1;
                Petrol = 0;
            }
        }
        if (Petrol + deficit >= 0)
        {
            return start;
        }
        return -1;
    }
};
int main()
{

    return 0;
}