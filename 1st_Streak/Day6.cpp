// Problem : Longest Substring Without Repeating Characters
// Problem Statement : Given a string s, find the length of the longest substring without repeating characters.
#include <bits/stdc++.h>
#define ll long long
#define pb push_back
#define MOD 1000000007
#define PI 3.14
using namespace std;
class Solution
{
public:
    int lengthOfLongestSubstring(string s)
    {
        int ans = 0;
        int curr = 0;
        unordered_map<char, bool> m;
        queue<char> q;
        int n = s.length();
        for (int i = 0; i < n; i++)
        {
            char ch = s[i];
            if (m.find(ch) == m.end() || m[ch] == false)
            {
                q.push(ch);
                m[ch] = true;
                curr++;
            }
            else
            {
                while (!q.empty() && q.front() != ch)
                {
                    m[q.front()] = false;
                    q.pop();
                    curr--;
                }
                if (!q.empty())
                {
                    q.pop();
                }
                q.push(ch);
            }
            ans = max(ans, curr);
        }
        return ans;
    }
};
int main()
{

    return 0;
}