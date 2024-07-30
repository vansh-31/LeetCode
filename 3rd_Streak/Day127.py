# Problem : Minimum Deletions to Make String Balanced
# Problem Statement : You are given a string s consisting only of characters 'a' and 'b'​​​​.
# You can delete any number of characters in s to make s balanced. s is balanced if there is no pair of indices (i,j) such that i < j and s[i] = 'b' and s[j]= 'a'.
# Return the minimum number of deletions needed to make s balanced.
class Solution(object):
    def minimumDeletions(self, s):
        ans, countB = 0, 0
        for ch in s:
            if ch == "a":
                ans = min(ans + 1, countB)
            else:
                countB += 1
        return ans
