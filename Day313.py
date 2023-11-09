# Problem : Count Number of Homogenous Substrings
# Problem Statement : Given a string s, return the number of homogenous substrings of s. Since the answer may be too large, return it modulo 109 + 7.
# A string is homogenous if all the characters of the string are the same.
# A substring is a contiguous sequence of characters within a string.
class Solution:
    def countHomogenous(self, s: str) -> int:
        mod=10**9+7
        prev='X'
        count=0
        ans=0
        for c in s:
            if c!=prev:
                ans=(ans+count*(count+1)//2)% mod
                count=1
            else:
                count+=1
            prev=c
        ans=(ans+count*(count+1)//2)% mod
        return ans