// Problem : String Compression
// Problem Statement : Given an array of characters chars, compress it using the following algorithm:

// Begin with an empty string s. For each group of consecutive repeating characters in chars:

// If the group's length is 1, append the character to s.
// Otherwise, append the character followed by the group's length.
// The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

// After you are done modifying the input array, return the new length of the array.

// You must write an algorithm that uses only constant extra space.
#include <bits/stdc++.h>
#define ll long long
#define pb push_back
#define MOD 1000000007
#define PI 3.14
using namespace std;
class Solution
{
public:
    int compress(vector<char> &chars)
    {
        chars.push_back(' ');
        int n = chars.size();
        string s;
        int i = 0;
        while (i < n - 1)
        {
            s.push_back(chars[i]);
            if (chars[i] == chars[i + 1])
            {
                int count = 1;
                while (chars[i] == chars[i + 1] && i < n - 1)
                {
                    i++;
                    count++;
                }
                s += to_string(count);
            }
            i++;
        }
        cout << s << endl;
        chars.clear();
        for (int i = 0; i < s.length(); i++)
        {
            chars.push_back(s[i]);
        }
        return s.length();
    }
};
int main()
{

    return 0;
}