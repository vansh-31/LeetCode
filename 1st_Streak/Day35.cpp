// Problem : Permutation in String
// Problem Statement : Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
// In other words, return true if one of s1's permutations is the substring of s2.
#include<bits/stdc++.h>
#define ll long long
#define pb push_back
#define MOD 1000000007
#define PI 3.14
using namespace std;
class Solution {
public:
    bool contains(vector<int> freqs,int i,int j,string s2)
    {
        while(i<=j)
        {
            freqs[s2[i]-'a']--;
            i++;
        }
        for(int i = 0; i < 26; i++ )
        {
            if(freqs[i]!=0)
            {
                return false;
            }
        }
        return true;
    }
    bool checkInclusion(string s1, string s2)
    {
        vector<int> freqs(26,0);
        int n = s1.size();
        int m = s2.size();
        for(int i = 0; i < n; i++ )
        {
            freqs[s1[i]-'a']++;
        }
        int i = 0;
        int j = n-1;
        while( j < m )
        {
            if( contains(freqs,i,j,s2))
            {
                return true;
            }
            i++;
            j++;   
        }
        return false;
    }
};
int main()
{
    
    return 0;
}