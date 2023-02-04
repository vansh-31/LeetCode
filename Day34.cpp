// Problem : Zigzag Conversion
// Problem Statement : The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
// P   A   H   N
// A P L S I I G
// Y   I   R
#include<bits/stdc++.h>
#define ll long long
#define pb push_back
#define MOD 1000000007
#define PI 3.14
using namespace std;
class Solution {
public:

    string convert(string s, int numRows) {
    
    if(numRows <= 1) return s;

    vector<string>v(numRows, ""); 

    int j = 0, dir = -1;

    for(int i = 0; i < s.length(); i++)
    {

        if(j == numRows - 1 || j == 0) dir *= (-1); 
		 
        v[j] += s[i];

        if(dir == 1) j++;

        else j--;
    }

    string res;

    for(auto &it : v) res += it; 

    return res;

    }
};

int main()
{
    
    return 0;
}