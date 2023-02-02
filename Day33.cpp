// Problem : Verifying an Alien Dictionary
// Problem : In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.
// Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographically in this alien language.

#include <bits/stdc++.h>
#define ll long long
#define pb push_back
#define MOD 1000000007
#define PI 3.14
using namespace std;
class Solution
{
public:
    bool greaterthan(string s1, string s2, unordered_map<char, int> &m)
    {
        int i = 0;
        int j = 0;
        while (i < s1.size() && j < s2.size())
        {
            if (m[s1[i]] < m[s2[j]])
            {
                return false;
            }
            if (m[s1[i]] > m[s2[j]])
            {
                return true;
            }
            i++;
            j++;
        }
        if (i < s1.size())
        {
            return true;
        }
        return false;
    }
    bool isAlienSorted(vector<string> &words, string order)
    {
        unordered_map<char, int> m;
        for (int i = 0; i < 26; i++)
        {
            m[order[i]] = i;
        }
        for (int i = 0; i < words.size() - 1; i++)
        {
            if (greaterthan(words[i], words[i + 1], m))
            {
                return false;
            }
        }
        return true;
    }
};
int main()
{

    return 0;
}