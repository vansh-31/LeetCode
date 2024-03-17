# Problem : Removing Stars From a String
# Problem Statement :  You are given a string s, which contains stars *.
# In one operation, you can:
# Choose a star in s.
# Remove the closest non-star character to its left, as well as remove the star itself.
# Return the string after all stars have been removed.
# Note:
# The input will be generated such that the operation is always possible.
# It can be shown that the resulting string will always be unique.
class Solution:
    def removeStars(self, s: str) -> str:
        i = len(s)
        ans = ""
        count = 0
        while i >0:
            i -=1
            if s[i]=="*":
                count+=1
                continue
            if count > 0:
                count -= 1
                continue
            ans += s[i]
        return ans[::-1]
                