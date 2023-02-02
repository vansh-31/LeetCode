// Problem : Detect Capital
// Problem Statement : We define the usage of capitals in a word to be right when one of the following cases holds:
// All letters in this word are capitals, like "USA".
// All letters in this word are not capitals, like "leetcode".
// Only the first letter in this word is capital, like "Google".
// Given a string word, return true if the usage of capitals in it is right.
#include<bits/stdc++.h>
#define ll long long
#define pb push_back
#define MOD 1000000007
#define PI 3.14
using namespace std;
class Solution {
public:
    bool detectCapitalUse(string word)
    {
        int count = 0;
        int n = word.size();
        for(int i = 0; i < n; i++)
        {
            if(word[i]>=65 && word[i] <= 90)
            {
                count++;
            }
        }
        if(count == 0 || count == n)
        {
            return true;
        }
        if(count == 1 && (word[0] >= 65 && word[0] <= 90))
        {
            return true;
        }
        return false;
    }
};
int main()
{
    
    return 0;
}