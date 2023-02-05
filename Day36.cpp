// Problem : Find All Anagrams in a String
// Problem Statement : Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.
// An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

#include <bits/stdc++.h>
#define ll long long
#define pb push_back
#define MOD 1000000007
#define PI 3.14
using namespace std;
class Solution
{
public:
    bool freqs_are_equal(vector<int> &Pfreqs, vector<int> &Sfreqs)
    {
        for (int i = 0; i < 26; i++)
        {
            if (Pfreqs[i] != Sfreqs[i])
            {
                return false;
            }
        }
        return true;
    }
    vector<int> findAnagrams(string s, string p)
    {
        int n = s.length();
        int m = p.length();
        if (m > n)
        {
            return {};
        }
        vector<int> Pfreqs(26);
        vector<int> Sfreqs(26);
        vector<int> ans;
        for (int i = 0; i < m; i++)
        {
            Pfreqs[p[i] - 'a']++;
            Sfreqs[s[i] - 'a']++;
        }
        int window_st = 0;
        int window_end = m - 1;
        while (window_end < n - 1)
        {
            if (freqs_are_equal(Pfreqs, Sfreqs))
            {
                ans.push_back(window_st);
            }
            Sfreqs[s[window_st] - 'a']--;
            window_st++;
            window_end++;
            Sfreqs[s[window_end] - 'a']++;
        }
        if (freqs_are_equal(Pfreqs, Sfreqs))
        {
            ans.push_back(window_st);
        }
        return ans;
    }
};
int main()
{

    return 0;
}
