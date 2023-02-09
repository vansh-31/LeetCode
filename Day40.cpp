// Problem : Naming a Company
// Problem Statement : You are given an array of strings ideas that represents a list of names to be used in the process of naming a company. The process of naming a company is as follows:

// Choose 2 distinct names from ideas, call them ideaA and ideaB.
// Swap the first letters of ideaA and ideaB with each other.
// If both of the new names are not found in the original ideas, then the name ideaA ideaB (the concatenation of ideaA and ideaB, separated by a space) is a valid company name.
// Otherwise, it is not a valid name.
// Return the number of distinct valid names for the company.
#include <bits/stdc++.h>
#define ll long long
#define pb push_back
#define MOD 1000000007
#define PI 3.14
using namespace std;
class Solution
{
public:
    long long distinctNames(vector<string> &ideas)
    {
        unordered_map<string, bool> isPresent;
        for (auto str : ideas)
        {
            isPresent[str] = true;
        }
        int ans = 0;
        for (int i = 0; i < ideas.size() - 1; i++)
        {
            string s1 = ideas[i];
            for (int j = i + 1; j < ideas.size(); j++)
            {
                string s2 = ideas[j];
                if ((isPresent.find(s1[0] + s2.substr(1)) == isPresent.end()) && (isPresent.find(s2[0] + s1.substr(1)) == isPresent.end()))
                {
                    ans +=2;
                }
            }
        }
        return ans;
    }
};
int main()
{

    return 0;
}