// Problem : Word Pattern
// Problem Statement : Given a pattern and a string s, find if s follows the same pattern.
// Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.
#include<bits/stdc++.h>
#define ll long long
#define pb push_back
#define MOD 1000000007
#define PI 3.14
using namespace std;
class Solution {
public:
    string getword(string &s,int &i)
    {
        if(i==s.length())
        {
            return "";
        }
        if(s[i]==' ')
        {
            i++;
        }
        string ans = "";
        while(s[i]!=' ' && i < s.length())
        {
            ans.push_back(s[i++]);
        }
        return ans;
    }
    bool wordPattern(string pattern, string s)
    {
        int i = 0;
        int j = 0;
        unordered_map<char,string> m;
        unordered_map<string,char> n;
        while(i < s.length() && j < pattern.length())
        {
            char ch = pattern[j++];
            string word = getword(s,i);

            if(m.find(ch) == m.end() && n.find(word) == n.end())
            {
                m[ch] = word;
                n[word] = ch;
                continue;
            }
            
            if(m[ch] != word)
            {
                return false;
            }
            if(n[word]!=ch)
            {
                return false;
            }
        }
        if(i == s.length() && j == pattern.length())
            return true;
        return false;
    }
};
int main()
{
    
    return 0;
}